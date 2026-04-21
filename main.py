from fastapi import FastAPI
from user.router import router

app = FastAPI()

# 라우터 등록
app.include_router(router)