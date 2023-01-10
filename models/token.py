from pydantic import BaseModel, Field
from typing import List
from utils.language import POS


class Token(BaseModel):
    text: str = Field(description='Text of token')
    lemma: str = Field(description='Lemmatized token')
    pos: POS = Field(description='Syntactical category')
    arasaac_ids: List[int] = Field(description='IDs of ARASAAC pictograms')

    class Config:
        schema_extra = {
            "example": {
                "text": "habla",
                "lemma": "hablar",
                "pos": "VERB",
                "arasaac_ids": [3345, 6517, 36544]
            }
        }


class Tokens(BaseModel):
    tokens: List[Token] = Field(description='Sentence')
