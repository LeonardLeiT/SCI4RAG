def retrieve(query, vector_store, k_value=3):
    """Retrieve information related to a query."""
    retrieved_docs = vector_store.similarity_search(query, k=k_value)
    serialized = "\n\n".join(
        f"Source: {doc.metadata}\nContent: {doc.page_content}"
        for doc in retrieved_docs
    )
    return serialized

def retriever_prompt(query, vector_store, k_value=3):
    """Construct a ChatPromptTemplate using retrieved context."""
    context = retrieve(query, vector_store, k_value)
    
    if context is None:
        context = "Can't find information in dataset."

    system_template = f"""You are a helpful assistant specialized in question-answering tasks.
Use the retrieved context below to answer the user's question.
If the answer is not found in the context, respond with: "The RAG dataset can't find relevant knowledge."
Provide a detailed and comprehensive answer.
If you use information from the context, clearly cite the source.
---------------------
{context}
"""
    return system_template

if __name__ == "__main__":
    context = 'hhhhhhh'
    
    if context is None:
        context = "Can't find information in dataset."

    system_template = (
        "You are a helpful assistant specialized in question-answering tasks.\n"
        "Use the retrieved context below to answer the user's question.\n"
        "If the answer is not found in the context, respond with: "
        "\"The RAG dataset can't find relevant knowledge.\"\n"
        "Provide a detailed and comprehensive answer.\n"
        "If the answer includes information from the context, cite the source clearly.\n"
        "---------------------\n"
        f"{context}"
    )    
    
    print(system_template)