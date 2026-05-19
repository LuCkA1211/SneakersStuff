from pydantic import BaseModel, Field

class ProductDescriptionCreateRequest(BaseModel):
    brand: str
    model: str
    color: str
    release_year: int
    category: str
    insertion_date: str

class ProductDescriptionCreateResponse(BaseModel):
    brand: str
    model: str
    color: str
    release_year: int

    model_config = {"from_attributes": True}