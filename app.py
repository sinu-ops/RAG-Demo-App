import streamlit as st
st.write("RUNNING FILE:", __file__)

import streamlit as st
from rag.data import load_docs, ensure_docs
from rag.advanced import hyde_query, step_back_query

st.set_page_config(page_title="RAG Learning Demo", layout="wide")

st.title("RAG Learning Demo — Step 1")
if st.button("Regenerate sample docs"):
    ensure_docs()
    st.success("Sample docs ensured.")

docs = load_docs()
st.subheader("Sample Documents")
for d in docs:
    st.markdown(f"**{d['title']}**  \nTags: {', '.join(d['tags'])}")
    st.write(d["text"])
    st.divider()
from rag.llm import generate_text 

st.subheader("Test Gemini")
user_q = st.text_input("Ask Gemini something:")
if st.button("Send to Gemini") and user_q:
    with st.spinner("Calling Gemini..."):
        answer = generate_text(user_q)
    st.markdown("**Gemini Answer:**")
    st.write(answer)


from rag.retrieval import Retriever

st.subheader("RAG Demo (BM25 + Vector + Fusion)")

query = st.text_input("Ask a question about the docs", key="rag_query")
mode = st.selectbox(
    "Retrieval mode",
    ["Normal", "HyDE (hypothetical answer)", "Step-back (generalized)"],
)

if st.button("Run RAG") and query:
    retriever = Retriever(docs)

    if mode == "HyDE (hypothetical answer)":
        expanded_query = hyde_query(query)
        st.markdown("**HyDE query used for retrieval:**")
        st.write(expanded_query)
        search_query = expanded_query
    elif mode == "Step-back (generalized)":
        expanded_query = step_back_query(query)
        st.markdown("**Step-back query used for retrieval:**")
        st.write(expanded_query)
        search_query = expanded_query
    else:
        search_query = query

    fused_docs = retriever.search_fusion(search_query, k=3)

    st.markdown("### Retrieved Context")
    context = ""
    for d in fused_docs:
        st.write(f"**{d['title']}** — {d['text']}")
        context += f"{d['title']}: {d['text']}\n"

    prompt = f"""Answer the question using only the context.

Context:
{context}

Question: {query}
Answer:"""

    with st.spinner("Generating with Gemini..."):
        answer = generate_text(prompt)

    st.markdown("### Final Answer")
    st.write(answer)