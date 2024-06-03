from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List
from data import movies

app = FastAPI()

app.title = "Mi aplicación con FastAPI"

app.version = "0.0.1"


class Movie(BaseModel):
    id: int
    title: str
    overview: str
    year: int
    rating: float
    category: str


@app.get("/", tags=["Home"])
def message():
    return HTMLResponse("<h1>Hello, world</h1>")


@app.get("/movies", tags=["Movies"])
def get_movies():
    return movies


@app.get("/movies/{id}", tags=["Movies"])
def get_movie(id: int):
    for item in movies:
        if item["id"] == id:
            return item
    return []


@app.get("/movies/", tags=["Movies"])
def get_movies_by_categories(category: str, year: int):
    return category, year


@app.get("/movies/", tags=["Movies"])
def get_filter_categories(category: str):
    return [movie for movie in movies if movie["category"] == category]


@app.post("/movies", tags=["Movies"], response_model=List[Movie])
def post_movies(movie: Movie):
    movies.append(movie.dict())
    return movies
