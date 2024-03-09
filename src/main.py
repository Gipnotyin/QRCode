from fastapi import FastAPI

from auto_info.auto_info import router as auto_router

app = FastAPI(
    title="QRcode"
)

app.include_router(auto_router)

origins = [
    "http://localhost:8000"
]
