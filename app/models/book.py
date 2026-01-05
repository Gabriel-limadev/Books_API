from sqlmodel import Field, SQLModel

class Book(SQLModel, table=True):
    __tablename__ = "books"
    id: int = Field(primary_key=True)
    title: str = Field(index=True)
    price: float = Field()
    rating: int = Field(index=True)
    availability: int = Field()
    category: str = Field(index=True)
    image: str = Field()