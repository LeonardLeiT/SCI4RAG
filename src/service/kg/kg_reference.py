from src.service.document.load_document import load_document_metadata, load_json
from pathlib import Path
import networkx as nx

def construct_kg_ref(username: str, dataset_name: str):
    pdf_files_data = load_document_metadata(username, dataset_name)

    # ---------- pass 1: collect valid DOIs ----------
    valid_dois = set()
    doi_meta = {}

    def authors_to_str(authors):
        if not authors:
            return ""
        if isinstance(authors, list):
            return "; ".join(authors)
        return str(authors)

    for file_id in pdf_files_data:
        doi_path = Path(f"users/{username}/{dataset_name}/data_clean/{file_id}/doi.json")
        if not doi_path.exists():
            continue

        doc_doi_info = load_json(doi_path)
        doi = doc_doi_info.get("doi")
        if doi:
            valid_dois.add(doi)
            doi_meta[doi] = doc_doi_info

    # ---------- pass 2: build graph ----------
    kg = {"nodes": {}, "edges": []}
    seen_edges = set()

    for file_id in pdf_files_data:
        doi_path = Path(f"users/{username}/{dataset_name}/data_clean/{file_id}/doi.json")
        ref_path = Path(f"users/{username}/{dataset_name}/data_clean/{file_id}/references.json")

        if not doi_path.exists() or not ref_path.exists():
            continue
        print(f"Processing {file_id}...")
        doc_doi_info = load_json(doi_path)
        src_doi = doc_doi_info.get("doi")
        if src_doi not in valid_dois:
            continue

        kg["nodes"].setdefault(src_doi, {
            "title": doc_doi_info.get("title"),
            "year": doc_doi_info.get("year"),
            "journal": doc_doi_info.get("journal"),
            "author": authors_to_str(doc_doi_info.get("author")),
            "url": doc_doi_info.get("url"),
            "type": "paper"
        })

        doc_ref_info = load_json(ref_path)

        for _, ref_info in doc_ref_info.items():
            tgt_doi = ref_info.get("doi")
            if tgt_doi not in valid_dois:
                continue

            edge_key = (src_doi, tgt_doi)
            if edge_key in seen_edges:
                continue
            seen_edges.add(edge_key)

            kg["nodes"].setdefault(tgt_doi, {
                "title": ref_info.get("title"),
                "year": ref_info.get("year"),
                "journal": ref_info.get("journal"),
                "author": authors_to_str(ref_info.get("author")),
                "url": ref_info.get("url"),
                "type": "paper"
            })

            kg["edges"].append({
                "source": src_doi,
                "target": tgt_doi,
                "relation": "citation"
            })

    kg["meta"] = {
        "scope": "internal_dataset_only",
        "node_count": len(kg["nodes"]),
        "edge_count": len(kg["edges"]),
        "edge_type": "citation"
    }

    return kg
def kg_to_networkx(kg):
    G = nx.DiGraph()

    for doi, meta in kg["nodes"].items():
        G.add_node(doi, **meta)

    for e in kg["edges"]:
        G.add_edge(
            e["source"],
            e["target"],
            relation=e["relation"]
        )
    return G



if __name__ == "__main__":
    username = "administrator"
    dataset_name = "test"

    print("Preparing PDF files for MinerU processing...")
    kg = construct_kg_ref(username, dataset_name)
    print(kg )

    G = kg_to_networkx(kg)
    nx.write_gexf(
        G,
        f"users/{username}/{dataset_name}/citation_graph.gexf"
    )

