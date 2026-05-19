import json
import colorsys
import networkx as nx
from pyvis.network import Network
from pathlib import Path


def run_step4(username: str, dataset_name: str, file_id: str):
    """
    Function: Generates an interactive HTML knowledge graph from the processed triplets, styling nodes by degree and highlighting predicted edges.

    Input:
    - username (str): The username of the workspace.
    - dataset_name (str): The name of the dataset.
    - file_id (str): The unique identifier for the file directory.

    Output:
    - None (Saves the visualization to 'final_graph.html').
    """
    current_dir = Path(__file__).resolve().parent
    project_root = current_dir.parent.parent.parent
    path = project_root / "users" / username / dataset_name / "data_clean" / file_id

    with open(path / "03_final.json", "r", encoding="utf-8") as f:
        triplets = json.load(f)

    G = nx.DiGraph()
    for t in triplets:
        G.add_edge(t["source"], t["target"], label=t["relation"])

    net = Network(height="900px", width="100%", bgcolor="#f8f9fa", font_color="#2c3e50", directed=True)
    degrees = dict(G.degree())
    if not degrees: return

    max_d = max(degrees.values()) or 1
    min_d = min(degrees.values()) or 1

    for n in G.nodes():
        deg = degrees.get(n, 1)
        node_size = 15 + (deg * 3)

        fraction = 0.5 if max_d == min_d else (deg - min_d) / (max_d - min_d)
        hue = 0.66 * (1.0 - fraction)
        r, g, b = [int(x * 255) for x in colorsys.hls_to_rgb(hue, 0.5, 0.9)]

        net.add_node(n, label=n, size=node_size,
                     color=f"rgba({r}, {g}, {b}, 0.6)",
                     borderWidth=2, shape="dot", shadow=True,
                     title=f"Entity: {n}\nConnections: {deg}")

    for src, tgt, data in G.edges(data=True):
        rel_text = data.get("label", "")
        is_highlight = rel_text in ["[PREDICTED]", "is model of"]
        edge_color = "#e74c3c" if is_highlight else "rgba(144, 164, 174, 0.5)"

        net.add_edge(src, tgt, label=rel_text,
                     color={"color": edge_color, "highlight": "rgba(44, 62, 80, 0.9)"},
                     width=2.5 if is_highlight else 1.5, arrows="to", shadow=True,
                     font={"size": 11, "align": "middle", "color": "#7f8c8d", "strokeWidth": 2,
                           "strokeColor": "#ffffff"})

    net.force_atlas_2based(gravity=-70, central_gravity=0.015, spring_length=180, spring_strength=0.06)
    net.write_html(str(path / "final_graph.html"))

    print("[INFO] Step 4: HTML graph visualization generated successfully.")