from fastapi import APIRouter

from routers.v1.tokenize import router as tokenize_api
from routers.v1.generate import router as generate_api

router = APIRouter()

router.include_router(tokenize_api, prefix="/tokenize", tags=["tokens"])
router.include_router(generate_api, prefix="/generate", tags=["generations"])
