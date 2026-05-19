from step1_parse import run_step1
from step2_mine import run_step2
from step3_ultra_align import run_step3
from step4_visualize import run_step4

# ==========================================
# Project Configuration
# ==========================================
# Replace with your actual DeepSeek API key
DEEPSEEK_API_KEY = "sk-"

# Workspace configuration
USERNAME = "administrator"
DATASET = "test"
FILE_ID = "20260206T140845_24126d3a8c"

if __name__ == "__main__":
    print("[INFO] Starting SCI4RAG Knowledge Graph Pipeline...\n" + "-" * 50)

    # Execute pipeline steps sequentially
    run_step1(USERNAME, DATASET, FILE_ID)
    run_step2(USERNAME, DATASET, FILE_ID, DEEPSEEK_API_KEY)
    run_step3(USERNAME, DATASET, FILE_ID, DEEPSEEK_API_KEY)
    run_step4(USERNAME, DATASET, FILE_ID)

    print("-" * 50 + "\n[INFO] Pipeline execution completed. Please open final_graph.html to view the graph.")