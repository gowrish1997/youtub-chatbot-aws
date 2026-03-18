from youtube_transcript_api import YouTubeTranscriptApi
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_pinecone import PineconeVectorStore
from utils.helper import download_embeddings
from config import PINECONE_INDEX

async def process_youtube_video(url):

    video_id = url.split("v=")[-1].split("&")[0]
    loader = YouTubeTranscriptApi().list(video_id)
        # Fix for the 'subscriptable' error from before
    raw_data = loader.find_transcript(["en"]).fetch()

    full_text = " ".join([entry.text for entry in raw_data])

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    docs = splitter.create_documents([full_text])

    embeddings = download_embeddings()

    PineconeVectorStore.from_documents(
        docs,
        embeddings,
        index_name=PINECONE_INDEX
    )
