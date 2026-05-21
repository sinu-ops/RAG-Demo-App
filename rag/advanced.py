from rag.llm import generate_text

def hyde_query(original_query: str) -> str:
    """
    Generate a hypothetical answer, then use it as a better retrieval query.
    """
    prompt = f"""Write a short, factual answer to the question below.
The answer will be used only for retrieval.

Question: {original_query}
Hypothetical Answer:"""
    return generate_text(prompt).strip()

def step_back_query(original_query: str) -> str:
    """
    Rewrite the query into a more general, higher-level question.
    """
    prompt = f"""Rewrite the question into a broader, more general query
that would help retrieve background info.

Original question: {original_query}
Step-back query:"""
    return generate_text(prompt).strip()