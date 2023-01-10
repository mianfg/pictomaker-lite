from pydantic import BaseModel, Field
from utils.language import ISOString


class Sentence(BaseModel):
    text: str = Field(description='Sentence')
    language: ISOString = Field(description='Language of sentence')

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        schema_extra = {
            "example": {
                "text": "Welcome to PictoMaker!",
                "language": "en",
            }
        }
