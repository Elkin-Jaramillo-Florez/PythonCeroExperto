from fastapi import FastAPI, HTTPException
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


class MovieUpdate(BaseModel):
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


@app.put("/movies/{id}", tags=["Movies"], response_model=List[Movie])
def update_movies(id: int, movie: MovieUpdate):
    for item in movies:
        if item["id"] == id:
            item["title"] = movie.title
            item["overview"] = movie.overview
            item["year"] = movie.year
            item["rating"] = movie.rating
            item["category"] = movie.category
            return movies


@app.delete("/movies/{id}", tags=["Movies"], response_model=List[Movie])
def delete_movie(id: int):
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return movies
