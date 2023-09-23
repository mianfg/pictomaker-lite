from fastapi import APIRouter
from models.card import Cards
from fastapi import Body, HTTPException
from fastapi.responses import Response
from services.images import PictoImageGenerator
from utils import docs

router = APIRouter()
image_generator = PictoImageGenerator(
    font = "/app/static/fonts/escolar_bold.ttf",
    text_size = 90,
    card_dimensions = (600,750),
    image_margin = 50
)

@router.post(
    "/png",
    summary="Generate PNG",
    description=docs.generate_png,
    status_code=200,
    responses={
        200: {
            "content": {"image/png": {}}
        }
    }
)
async def generate_png(cards: Cards = Body(...)):
    global image_generator

    try:
        io = image_generator.generate_PNG(cards.cards)
        return Response(io.getvalue(), media_type='image/png')
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Unexpected error")

@router.post(
    "/zip",
    summary="Generate ZIP",
    description=docs.generate_zip,
    status_code=200,
    responses={
        200: {
            "content": {"application/x-zip-compressed": {}}
        }
    }
)
async def generate_zip(cards: Cards = Body(...)):
    global image_generator

    io = image_generator.generate_ZIP(cards.cards)
    return Response(io.getvalue(), media_type='application/x-zip-compressed')
    try:
        print(type(cards.cards))
        io = image_generator.generate_PNG(cards.cards)
        return Response(content=io, media_type='image/png')
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Unexpected error")
