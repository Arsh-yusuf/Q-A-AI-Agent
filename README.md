# 📄 AI Document Q&A Agent (Streamlit + Cohere)

An interactive, enterprise-ready AI agent that allows users to upload multiple PDF documents and ask natural language questions about their content — including paper-specific lookups, summarization, and evaluation extraction.

Built using:
- 🧠 [Cohere LLM](https://cohere.com/)
- ⚡ [Streamlit](https://streamlit.io/)
- 📚 Arxiv API (for research paper search)
- 📄 PyMuPDF for accurate PDF parsing

---

## 🚀 Features

- ✅ Upload **multiple PDF documents**
- ✅ Ask contextual questions like:
  - *"What is the conclusion of Paper A?"*
  - *"Summarize the methodology of Paper X."*
  - *"What are the accuracy and F1-score in Paper B?"*
- ✅ Auto-identifies the target paper from your question
- ✅ Built-in Arxiv search for new paper discovery

---

## 🧾 Requirements

- Python 3.8+
- Cohere API Key (free at [cohere.com](https://dashboard.cohere.com/))

---

## 🛠️ Installation

### 1. Clone this repository

```bash
git clone https://github.com/your-username/ai-doc-qa-agent.git
cd ai-doc-qa-agent


2. Install Dependencies

pip install -r requirements.txt

3. Add Cohere API key

Create a .env file in the project root:
COHERE_API_KEY=your_actual_api_key_here

4. Running the App

streamlit run streamlit_app.py

5. Project Structure

ai-doc-qa-agent/
├── app.py                     # Main Streamlit app
├── .env                       # API keys (not committed)
├── requirements.txt           # Python dependencies
├── README.md                  # This file
├── app/
│   ├── __init__.py
│   └── services/
│       ├── pdf_parser.py      # Extracts text from PDFs
│       ├── cohere_llm.py      # Interfaces with Cohere
│       └── arxiv_fetcher.py   # Arxiv search utility


