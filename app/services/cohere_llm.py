import os
import cohere

# For local development

# from dotenv import load_dotenv

# load_dotenv()
# cohere_api_key = os.getenv("COHERE_API_KEY")
# co = cohere.Client(cohere_api_key)

COHERE_API_KEY = st.secrets["COHERE_API_KEY"]
co = cohere.Client(COHERE_API_KEY)


def answer_query(question: str, context: str) -> str:
    response = co.chat(
        message=question,
        documents=[{"title": "document", "snippet": context}],
        temperature=0.3
    )
    return response.text
