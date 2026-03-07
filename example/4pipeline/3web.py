from src.pipline.web_pipeline import WebPipeline

# Run:  python -m example.4pipeline.3web

username = "administrator"

pipeline = WebPipeline(
    temperature=0.7,
    max_tokens=4096,
    username=username,
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