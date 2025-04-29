from pydantic import BaseModel

class MoviesBase(BaseModel):
    title: str
    release_year: str

class MoviesCreate(MoviesBase):
    pass

class Movies(MoviesBase):
    id: int

    class Config:
        orm_mode = True
