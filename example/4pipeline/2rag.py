from src.pipline.rag_pipeline import RAGPipeline

# Run:  python -m example.4pipeline.2rag

username = "administrator"
dataset_name = "test"

pipeline = RAGPipeline(
    temperature=0.7,
    max_tokens=4096,
    username=username,
    dataset_name=dataset_name,
)

user_input = 'What is the Schwarz Crystal?'

# 1. Response with stream
print("Response with stream")
print("Response: ", end="", flush=True)
for chunk in pipeline.query_stream(user_input):
    print(chunk, end="", flush=True)
print("")


# 2. Response without stream
print("Response without stream")
print("Response: ", pipeline.query(user_input))