from sqlalchemy.orm import Session
import models, schemas

def get_movie(db: Session, movie_id: int):
    return db.query(models.Movies).filter(models.Movies.id == movie_id).first()

def get_movie_by_title(db: Session, title: str):
    return db.query(models.Movies).filter(models.Movies.title == title).first()

def create_movie(db: Session, movie: schemas.MoviesCreate):
    db_movie = models.Movies(title=movie.title, release_year=movie.release_year)
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie
