from pydantic import BaseModel, Field
from utils.language import ISOString
from utils import docs


class Sentence(BaseModel):
    text: str = Field(description=docs.tokenize__text)
    language: ISOString = Field(description=docs.tokenize__language)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "text": "Welcome to PictoMaker!",
                "language": "en",
            }
        }
