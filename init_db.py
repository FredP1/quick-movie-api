from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

initial_movies = [
    {"title": "Sinners", "release_year": "2025"},
    {"title": "Warfare", "release_year": "2025"},
    {"title": "12 Angry Men", "release_year": "1957"},
]

def init():
    db: Session = SessionLocal()
    try:
        for movie_data in initial_movies:
            movie = crud.get_movie_by_title(db, movie_data["title"])
            if not movie:
                movie_schema = schemas.MoviesCreate(**movie_data)
                crud.create_movie(db, movie_schema)
        print("Database initialized with my favourite movies hehe.")
    finally:
        db.close()

if __name__ == "__main__":
    init()
