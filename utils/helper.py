from langchain_openai import OpenAIEmbeddings
from config import OPENAI_API_KEY

def download_embeddings():
    """
    Download and return the OpenAI embeddings model with 384 dimensions.
    """
    embeddings = OpenAIEmbeddings(
        api_key=OPENAI_API_KEY,
        model="text-embedding-3-small",
        dimensions=384
    )
    return embeddings