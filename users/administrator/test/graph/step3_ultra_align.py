import json
import re
import networkx as nx
from pathlib import Path
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser


def clean_entity(text: str) -> str:
    """
    Function: Cleans entity names by removing common adjectives, handling plurals, and mapping known abbreviations.

    Input:
    - text (str): The raw entity name.

    Output:
    - (str): The standardized entity name in title case.
    """
    t = text.lower().strip()

    prefixes = [r'^high\s+', r'^enhanced\s+', r'^stable\s+', r'^significant\s+',
                r'^superior\s+', r'^intrinsic\s+', r'^extremely\s+', r'^vanishing\s+',
                r'^pure\s+', r'^triply\s+periodic\s+']
    for p in prefixes:
        t = re.sub(p, '', t)

    synonym_map = {
        "thermostability": "thermal stability",
        "curvature": "mean curvature",
        "sc": "schwarz crystal",
        "ctb": "coherent twin boundary",
        "ctbs": "coherent twin boundary",
        "gb": "grain boundary",
        "gbs": "grain boundary",
        "kc": "kelvin crystal",
        "tpms": "minimal surface"
    }
    if t in synonym_map:
        t = synonym_map[t]

    if t.endswith('s') and not t.endswith('ss'):
        t = t[:-1]
    return t.title()


class EntityMapping(BaseModel):
    mapping: dict[str, str] = Field(description="Dictionary: KEY is the alias, VALUE is the canonical name.")


def run_step3(username: str, dataset_name: str, file_id: str, api_key: str):
    """
    Function: Filters noisy nodes, merges synonyms using an LLM, and predicts missing structural links using graph topology.

    Input:
    - username (str): The username of the workspace.
    - dataset_name (str): The name of the dataset.
    - file_id (str): The unique identifier for the file directory.
    - api_key (str): API key for the language model.

    Output:
    - None (Saves the aligned and enriched triplets to '03_final.json').
    """
    current_dir = Path(__file__).resolve().parent
    project_root = current_dir.parent.parent.parent
    path = project_root / "users" / username / dataset_name / "data_clean" / file_id

    with open(path / "02_raw.json", "r", encoding="utf-8") as f:
        raw_triplets = json.load(f)

    pre_cleaned = []
    for t in raw_triplets:
        src = clean_entity(t["source"])
        tgt = clean_entity(t["target"])
        rel = t["relation"].strip().lower()
        if len(src.split()) <= 5 and len(tgt.split()) <= 5 and src != tgt:
            pre_cleaned.append({"source": src, "target": tgt, "relation": rel})

    unique_entities = list(set([t["source"] for t in pre_cleaned] + [t["target"] for t in pre_cleaned]))
    print(f"[INFO] Aligning {len(unique_entities)} unique entities...")

    llm = ChatOpenAI(temperature=0.0, model="deepseek-chat", api_key=api_key, base_url="https://api.deepseek.com")
    parser = JsonOutputParser(pydantic_object=EntityMapping)

    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a data processing tool.
        TASK: Find ALL acronyms and synonyms in this list. Merge them into a single canonical name.
        Example: "Schwarz D Crystal" -> "Schwarz Crystal"
        {format_instructions}"""),
        ("human", "ENTITIES LIST:\n{entities}")
    ])

    try:
        result = (prompt | llm | parser).invoke({
            "entities": json.dumps(unique_entities, ensure_ascii=False),
            "format_instructions": parser.get_format_instructions()
        })
        merge_dict = result.get("mapping", {})
    except:
        merge_dict = {}

    final_triplets = []
    seen = set()
    for t in pre_cleaned:
        src = merge_dict.get(t["source"], t["source"]).strip()
        tgt = merge_dict.get(t["target"], t["target"]).strip()
        rel = t["relation"]
        if src == tgt: continue
        sig = f"{src}|{rel}|{tgt}"
        if sig not in seen:
            seen.add(sig)
            final_triplets.append({"source": src, "target": tgt, "relation": rel})

    G = nx.Graph()
    for t in final_triplets:
        G.add_edge(t["source"], t["target"])

    preds = nx.adamic_adar_index(G)
    predicted = sorted([(u, v, p) for u, v, p in preds], key=lambda x: x[2], reverse=True)
    for u, v, score in predicted[:15]:
        final_triplets.append({"source": u, "target": v, "relation": "[PREDICTED]"})

    domain_fixes = [
        ("S0", "Schwarz Crystal", "is model of"),
        ("S1", "Schwarz Crystal", "is model of"),
        ("S4", "Schwarz Crystal", "is model of"),
        ("Mean Curvature", "Minimal Surface", "defines"),
        ("Polycrystalline Copper", "Copper", "is form of")
    ]
    nodes_in_graph = set(G.nodes())
    for s, t, r in domain_fixes:
        if clean_entity(s) in nodes_in_graph and clean_entity(t) in nodes_in_graph:
            final_triplets.append({"source": clean_entity(s), "target": clean_entity(t), "relation": r})

    with open(path / "03_final.json", "w", encoding="utf-8") as f:
        json.dump(final_triplets, f, ensure_ascii=False, indent=4)

    print("[INFO] Step 3: Entity alignment and link prediction complete.")