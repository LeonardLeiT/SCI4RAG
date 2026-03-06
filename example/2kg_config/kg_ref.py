from src.service.kg.kg_reference import construct_kg_ref, kg_to_networkx
import networkx as nx

username = "administrator"
dataset_name = "Schwarz"

print("Preparing PDF files for MinerU processing...")
kg = construct_kg_ref(username, dataset_name)
# print(kg )

G = kg_to_networkx(kg)
nx.write_gexf(
    G,
    f"users/{username}/{dataset_name}/citation_graph.gexf"
)