from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from auth.router import user_router, auth_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["Content-Type", "Authorization", "Set-Cookie", "Access-Control-Allow-Origin","Access-Control-Allow-Headers"],
)

app.include_router(user_router)
app.include_router(auth_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}