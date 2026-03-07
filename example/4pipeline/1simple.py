from src.pipline.simple_pipeline import SimplePipeline

# Run:  python -m example.4pipeline.1simple

pipeline = SimplePipeline(
    temperature=0.7,
    max_tokens=4096,
)

user_input = 'Can you search in the web'

# 1. Response with stream
print("Response with stream")
print("Response: ", end="", flush=True)
for chunk in pipeline.query_stream(user_input):
    print(chunk, end="", flush=True)
print("")


# 2. Response without stream
print("Response without stream")
print("Response: ", pipeline.query(user_input))