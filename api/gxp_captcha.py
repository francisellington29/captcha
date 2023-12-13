from fastapi import APIRouter

from services.gxp import api as gxp_api
from services.utils import current_time

router = APIRouter()


def mybalance(api_key):
    gxp_api.key = api_key
    balance = gxp_api.get_balance()
    return balance

@router.get("/")
def get_balance(api_key: str):
    balance = mybalance(api_key)
    now = current_time()
    print(f'{now} **balance:{balance}**')
    return {"balance": balance, "time":now}


@router.get("/hcaptcha/")
def solve_hcaptcha(api_key: str, url: str, sitekey: str):
    gxp_api.key = api_key
    data = {
        "method": "hcaptcha",
        "pageurl": url,
        "sitekey": sitekey
    }
    hcaptcha = gxp_api.run(data)
    balance = mybalance(api_key)
    now = current_time()
    print(f'{now} **hcaptcha:{hcaptcha}** **balance:{balance}**')
    return {"balance": balance, "time":now, "hcaptcha": hcaptcha, }


@router.get("/recaptcha2/")
def solve_recaptcha(api_key: str, url: str, sitekey: str):
    gxp_api.key = api_key
    data = {
        "method": "userrecaptcha",
        "pageurl": url,
        "sitekey": sitekey
    }
    recaptcha = gxp_api.run(data)
    balance = mybalance(api_key)
    now = current_time()
    print(f'{now} **recaptcha:{recaptcha}** **balance:{balance}**')
    return {"balance": balance, "time":now, "recaptcha": recaptcha}

