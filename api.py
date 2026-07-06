from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

movies = []

class Movie(BaseModel):
    title: str

@app.get("/")
def home():
    return {"message": "Movie API is running"}

@app.post("/movies")
def add_movie(movie: Movie):
    movies.append(movie.title)
    return {
        "message": "Movie added successfully",
        "movie": movie.title
    }

@app.get("/movies")
def show_movies():
    return {
        "movies": movies
    }

@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    if movie_id < 1 or movie_id > len(movies):
        return {"message": "Movie not found"}

    return {
        "id": movie_id,
        "title": movies[movie_id - 1]
    }