from pydantic import BaseModel, Field, AnyHttpUrl
from typing import List


class Card(BaseModel):
    text: str = Field(description='Text')
    color: str = Field(description='HTML-encoded color')
    image: AnyHttpUrl = Field(description='URL to image')

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "text": "habla",
                "color": "#50C878",
                "image": "https://api.arasaac.org/api/pictograms/3345"
            }
        }


class Cards(BaseModel):
    cards: List[Card] = Field(description='List of cards')

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "cards": [
                    {
                        "text": "¡Bienvenido",
                        "color": "#2e7d32",
                        "image": "https://api.arasaac.org/api/pictograms/6522"
                    },
                    {
                        "text": "a",
                        "color": "#ff6f00",
                        "image": "https://api.arasaac.org/api/pictograms/7041"
                    },
                    {
                        "text": "PictoMaker!",
                        "color": "#d32f2f",
                        "image": "https://api.arasaac.org/api/pictograms/27337"
                    }
                ]
            }
        }
