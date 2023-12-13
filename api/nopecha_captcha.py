from fastapi import APIRouter

from services.nopecha import api as nopecha_api
from services.utils import current_time

router = APIRouter()


def mybalance(api_key):
    nopecha_api.key=api_key
    balance = nopecha_api.balance()
    return balance

@router.get("/")
def get_balance(api_key: str):
    balance = mybalance(api_key)
    now = current_time()
    print(f'{now} balance:{balance}')
    return {"now": now, "balance": balance}


@router.get("/hcaptcha/")
def solve_hcaptcha(api_key: str, url: str, sitekey: str):
    nopecha_api.key = api_key
    hcaptcha = nopecha_api.hcaptcha(sitekey,url)
    balance = mybalance(api_key)
    now = current_time()
    print(f'{now} **hcaptcha:{hcaptcha}** **balance:{balance}**')
    return {"now": now, "balance": balance, "hcaptcha": hcaptcha}


@router.get("/recaptcha2/")
def solve_recaptcha2(api_key: str, url: str, sitekey: str):
    nopecha_api.key = api_key
    recaptcha = nopecha_api.recaptcha2(sitekey,url)
    balance = mybalance(api_key)
    now = current_time()
    print(f'{now} **recaptcha:{recaptcha}** **balance:{balance}**')
    return {"now": now, "balance": balance, "recaptcha2": recaptcha}

