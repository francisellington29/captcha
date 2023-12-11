from fastapi import FastAPI
from gxp import api

app = FastAPI()


@app.get("/")
def get_balance(api_key: str):
    api.key = api_key
    balance = api.get_balance()
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
    return {"hCaptcha": hcaptcha}


