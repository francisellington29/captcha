from fastapi import APIRouter

from .gxp_captcha import router as gxp_router
from .nopecha_captcha import router as nopecha_router

router = APIRouter()
router.include_router(gxp_router, prefix='/gxp')
# router.include_router(nopecha_router, prefix='/nopecha')

@router.get('/')
def root():
    return {"hello": 'captcha'}