from fastapi import FastAPI, HTTPException
from models.request_models import VideoURL, ChatRequest
from services.youtube_services import process_youtube_video
from services.rag_service import ask_question
import uvicorn
import config

app = FastAPI()

@app.post("/process_video")
async def process_video(data: VideoURL):
    try:
        await process_youtube_video(data.url)
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        answer = await ask_question(request.message)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# To run uvicorn server directly if needed
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


