from src.service.kg.kg_reference import construct_kg_ref

username = "administrator"
dataset_name = "test"

# Run:  python -m example.2kg.1kg_ref
print("Constructing KG...")
kg = construct_kg_ref(username, dataset_name)