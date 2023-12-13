import time
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from gxp import api

app = FastAPI()

# 允许所有来源访问，更具体的配置可以根据需求进行修改
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源访问，也可以指定特定的来源，如 ["http://localhost", "https://example.com"]
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有 HTTP 方法访问
    allow_headers=["*"],  # 允许所有头部访问
)

@app.get("/")
def get_balance(api_key: str):
    api.key = api_key
    balance = api.get_balance()
    print(f'{time.now} balance:{balance}')
    return {"balance": balance}


@app.get("/hcaptcha/")
def solve_hcaptcha(api_key: str, url: str, sitekey: str):
    api.key = api_key
    data = {
        "method": "hcaptcha",
        "pageurl": url,
        "sitekey": sitekey
    }
    hcaptcha = api.run(data)
    balance = api.get_balance()
    print(f'{time.now} **hcaptcha:{hcaptcha}** **balance:{balance}**')
    return {"hcaptcha": hcaptcha, "balance": balance}


@app.get("/recaptcha/")
def solve_recaptcha(api_key: str, url: str, sitekey: str):
    api.key = api_key
    data = {
        "method": "userrecaptcha",
        "pageurl": url,
        "sitekey": sitekey
    }
    recaptcha = api.run(data)
    balance = api.get_balance()
    print(f'{time.now} **recaptcha:{recaptcha}** **balance:{balance}**')
    return {"recaptcha": recaptcha, "balance": balance}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app)
