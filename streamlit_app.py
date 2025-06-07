import streamlit as st
import re
from app.services.pdf_parser import extract_text
from app.services.cohere_llm import answer_query
from app.services.arxiv_fetcher import search_arxiv

st.set_page_config(page_title="AI Document Q&A Agent", layout="wide")
st.title("📄 AI Document Q&A Agent")

st.write("Upload multiple papers, then ask targeted questions like:")
st.code("What is the conclusion of Paper X?\nSummarize the methodology of Paper Y.\nWhat are the accuracy and F1-score reported in Paper Z?")

# Upload multiple PDFs
uploaded_files = st.file_uploader("Upload one or more PDF files", type=["pdf"], accept_multiple_files=True)
paper_texts = {}

if uploaded_files:
    for file in uploaded_files:
        paper_name = file.name.rsplit(".", 1)[0].lower().replace(" ", "_")  # Normalize
        text = extract_text(file.read())
        paper_texts[paper_name] = text

    st.success(f"{len(paper_texts)} paper(s) uploaded: {', '.join(paper_texts.keys())}")

# Function to identify which paper is referenced in the query
def extract_target_paper(query: str, papers: list[str]) -> str | None:
    for paper in papers:
        pattern = rf"\b{re.escape(paper)}\b"
        if re.search(pattern, query.lower()):
            return paper
    return None

# Ask Question
if paper_texts:
    st.markdown("---")
    st.subheader("🤖 Ask a Question About a Specific Paper")
    query = st.text_input("Enter your question (mention the paper name):")

    if st.button("Get Answer") and query:
        target = extract_target_paper(query, list(paper_texts.keys()))

        if target:
            with st.spinner(f"Answering based on `{target}.pdf`..."):
                response = answer_query(query, paper_texts[target])
            st.markdown(f"**Answer from `{target}`:**")
            st.write(response)
        else:
            st.warning("❗ Could not identify the target paper.")
            st.info(f"Hint: Mention one of: `{', '.join(paper_texts.keys())}` in your query.")

# Arxiv paper search
st.markdown("---")
st.subheader("🔍 Arxiv Paper Search")

arxiv_query = st.text_input("Search for academic papers on Arxiv (e.g., transformers, BERT):")

if st.button("Search Arxiv") and arxiv_query:
    with st.spinner("Searching Arxiv..."):
        results = search_arxiv(arxiv_query)
    if results:
        st.success(f"Found {len(results)} papers:")
        for paper in results:
            st.markdown(f"### {paper['title']}")
            st.write(paper["summary"])
            st.markdown(f"[📄 PDF Link]({paper['pdf_url']})")
    else:
        st.warning("No matching papers found.")
