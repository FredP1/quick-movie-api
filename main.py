from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/movies/", response_model=schemas.Movies)
def create_movie(movie: schemas.MoviesCreate, db: Session = Depends(get_db)):
    db_movie = crud.get_movie_by_title(db, email=movie.title)
    if db_movie:
        raise HTTPException(status_code=400, detail="Movie already in DB")
    return crud.create_movie(db=db, movie=movie)

@app.get("/movies/id/{movie_id}", response_model=schemas.Movies)
def read_movie(movie_id: int, db: Session = Depends(get_db)):
    db_movie = crud.get_movie(db, movie_id=movie_id)
    if not db_movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie

@app.get("/movies/{movie_title}", response_model=schemas.Movies)
def read_movie(movie_title: str, db: Session = Depends(get_db)):
    db_movie = crud.get_movie_by_title(db, title=movie_title)
    if not db_movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie