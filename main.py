from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api import router

app = FastAPI()
app.include_router(router)

# 允许所有来源访问，更具体的配置可以根据需求进行修改
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源访问，也可以指定特定的来源，如 ["http://localhost", "https://example.com"]
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有 HTTP 方法访问
    allow_headers=["*"],  # 允许所有头部访问
)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app)
