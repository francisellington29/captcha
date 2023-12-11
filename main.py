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
    balance = api.get_balance()
    return {"hCaptcha": hcaptcha, "balance": balance}


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
    return {"reCaptcha": recaptcha, "balance": balance}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app)
