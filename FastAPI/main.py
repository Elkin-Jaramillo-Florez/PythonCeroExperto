from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

app.title = "Mi aplicación con FastAPI"

app.version = "0.0.1"


movies = {
    1: {
        "id": 1,
        "title": "The Godfather",
        "overview": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
        "year": 1972,
        "rating": 9.2,
        "category": "Crime, Drama",
    },
    2: {
        "id": 2,
        "title": "The Dark Knight",
        "overview": "When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham.",
        "year": 2008,
        "rating": 9.0,
        "category": "Action, Crime, Drama",
    },
    3: {
        "id": 3,
        "title": "Pulp Fiction",
        "overview": "The lives of two mob hitmen, a boxer, a gangster's wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
        "year": 1994,
        "rating": 8.9,
        "category": "Crime, Drama",
    },
    4: {
        "id": 4,
        "title": "Schindler's List",
        "overview": "In German-occupied Poland during World War II, industrialist Oskar Schindler gradually becomes concerned for his Jewish workforce.",
        "year": 1993,
        "rating": 8.9,
        "category": "Biography, Drama, History",
    },
    5: {
        "id": 5,
        "title": "The Lord of the Rings: The Return of the King",
        "overview": "Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.",
        "year": 2003,
        "rating": 8.9,
        "category": "Adventure, Drama, Fantasy",
    },
    6: {
        "id": 6,
        "title": "Forrest Gump",
        "overview": "The presidencies of Kennedy and Johnson, the Vietnam War, the Watergate scandal, and other historical events unfold from the perspective of an Alabama man with an IQ of 75.",
        "year": 1994,
        "rating": 8.8,
        "category": "Drama, Romance",
    },
    7: {
        "id": 7,
        "title": "Inception",
        "overview": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.",
        "year": 2010,
        "rating": 8.8,
        "category": "Action, Adventure, Sci-Fi",
    },
    8: {
        "id": 8,
        "title": "The Matrix",
        "overview": "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.",
        "year": 1999,
        "rating": 8.7,
        "category": "Action, Sci-Fi",
    },
    9: {
        "id": 9,
        "title": "Gladiator",
        "overview": "A former Roman General sets out to exact vengeance against the corrupt emperor who murdered his family and sent him into slavery.",
        "year": 2000,
        "rating": 8.5,
        "category": "Action, Adventure, Drama",
    },
    10: {
        "id": 10,
        "title": "Interstellar",
        "overview": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
        "year": 2014,
        "rating": 8.6,
        "category": "Adventure, Drama, Sci-Fi",
    },
}


@app.get("/", tags=["Home"])
def message():
    return HTMLResponse("<h1>Hello, world</h1>")


@app.get("/movies", tags=["Movies"])
def get_movies():
    return movies
