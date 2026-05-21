# RAG Demo App (Streamlit + Gemini)

A practical **Retrieval-Augmented Generation (RAG)** demo app built with **Streamlit** and **Google Gemini**.  
It retrieves relevant documents for a user query (Normal / HyDE / Step-back) and generates a grounded answer using the retrieved context.

## Why this project matters
This project demonstrates end-to-end ability to build an LLM application, including:
- **RAG pipeline design** (retrieve → augment prompt → generate)
- **Multiple retrieval strategies** (Normal, HyDE, Step-back)
- **LLM integration** (Gemini API)
- **Error handling / reliability** (e.g., graceful handling of 503 high-demand errors)
- **Clean project structure** (`rag/` module separation)
- **Working UI demo** (Streamlit)

## Features
- **Streamlit UI** for interactive testing
- **RAG modes**
  - **Normal retrieval**: retrieves documents directly based on the user question
  - **HyDE**: generates a hypothetical answer first, then retrieves documents using that representation
  - **Step-back prompting**: retrieves/frames broader context to improve answers for complex questions
- **Displays retrieved context** (so you can verify grounding)
- **Resilient Gemini calls** (retry/backoff or friendly message on overload)

## Tech Stack
- Python
- Streamlit
- Google Gemini (google-genai)
- Vector / retrieval logic (inside `rag/` package)

## Project Structure
```text
.
├── app.py                  # Streamlit entry point
├── rag/
│   ├── llm.py              # Gemini wrapper (generation + retry/error handling)
│   ├── ...                 # Retrieval / RAG logic (varies by your implementation)
├── data/                   # (Optional) documents / dataset used for retrieval
├── requirements.txt        # Python dependencies (recommended)
└── README.md
```

## Getting Started (Local Setup)

### 1) Clone
```bash
git clone https://github.com/sinu-ops/RAG-Demo-App.git
cd RAG-Demo-App
```

### 2) Create & activate a virtual environment (recommended)
**Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3) Install dependencies
```bash
pip install -r requirements.txt
```

### 4) Set environment variable (Gemini API Key)
**Windows (PowerShell):**
```powershell
$env:GEMINI_API_KEY="YOUR_API_KEY_HERE"
```

> Note: Do **not** hardcode API keys in code. Keep them in environment variables.

### 5) Run the app
```bash
streamlit run app.py
```

Open the URL shown in your terminal (usually `http://localhost:8501`).

## How to Demo (Interview-Friendly)
Use these steps to demonstrate clearly:
1. Ask a question that matches your dataset → show the **retrieved documents**.
2. Ask a tricky question and switch between:
   - **Normal**
   - **HyDE**
   - **Step-back**
   Show how retrieval results and final answers change.
3. Mention reliability: “Gemini can return 503 during high demand; I added retry/fallback messaging.”

## Notes / Limitations
- Gemini may sometimes return **503 UNAVAILABLE** during high demand. The app handles this gracefully, but retries may be needed.
- This is a learning/demo project: a production version would add monitoring, caching, evaluation, and secure secret management.

## Future Improvements (Roadmap)
- Add reranking (cross-encoder) for improved retrieval quality
- Add evaluation metrics (Recall@K, MRR) + automated test prompts
- Add caching for repeated queries
- Add Docker + deployment guide

---

If you’re a recruiter/hiring manager: I’d be happy to walk you through the architecture, retrieval strategies, and tradeoffs in a short demo.
