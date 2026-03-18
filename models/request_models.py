from pydantic import BaseModel

class VideoURL(BaseModel):
    url: str

class ChatRequest(BaseModel):
    message: str
