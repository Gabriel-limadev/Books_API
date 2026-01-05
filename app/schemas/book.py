from pydantic import BaseModel

class BookResponse(BaseModel):
    id: int
    title: str
    price: float
    rating: int
    availability: int
    category: str
    image: str

    class Config:
        from_attributes = True