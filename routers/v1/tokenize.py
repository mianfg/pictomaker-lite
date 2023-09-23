from fastapi import APIRouter
from models.sentence import Sentence
from models.token import Tokens
from fastapi import Body, HTTPException, status
from fastapi.responses import JSONResponse
from services.language import PictoLanguage
from utils import docs

router = APIRouter()
language = PictoLanguage()

@router.post(
    "/",
    summary="Tokenize sentence",
    description=docs.tokenize,
    status_code=200,
    responses={
        200: {
            "model": Tokens,
            "description": "List of tokens"
        }
    },
    tags=["Tokenize"]
)
async def tokenize(sentence: Sentence = Body(...)):
    global language
    tokens = language.tokenize(sentence.text, sentence.language)
    return JSONResponse(status_code=status.HTTP_200_OK, content=tokens)

    try:
        tokens = language.tokenize(sentence.text, sentence.language)
        return JSONResponse(status_code=status.HTTP_200_OK, content=tokens)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Unexpected error")
