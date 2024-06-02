from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

app.title = "Mi aplicación con FastAPI"

app.version = "0.0.1"


movies = [
    {
        "id": 1,
        "title": "El Padrino",
        "overview": "El envejecido patriarca de una dinastía del crimen organizado transfiere el control de su imperio clandestino a su hijo reacio.",
        "year": 1972,
        "rating": 9.2,
        "category": "Crimen",
    },
    {
        "id": 2,
        "title": "El Caballero de la Noche",
        "overview": "Cuando el peligro conocido como el Joker surge de su misterioso pasado, causa estragos y caos en las personas de Gotham.",
        "year": 2008,
        "rating": 9.0,
        "category": "Acción",
    },
    {
        "id": 3,
        "title": "Pulp Fiction",
        "overview": "Las vidas de dos asesinos a sueldo, un boxeador, la esposa de un gángster y una pareja de bandidos se entrelazan en cuatro relatos de violencia y redención.",
        "year": 1994,
        "rating": 8.9,
        "category": "Crimen",
    },
    {
        "id": 4,
        "title": "La Lista de Schindler",
        "overview": "En la Polonia ocupada por los alemanes durante la Segunda Guerra Mundial, el industrial Oskar Schindler gradualmente se preocupa por su fuerza laboral judía.",
        "year": 1993,
        "rating": 8.9,
        "category": "Biografía",
    },
    {
        "id": 5,
        "title": "El Señor de los Anillos: El Retorno del Rey",
        "overview": "Gandalf y Aragorn lideran el Mundo de los Hombres contra el ejército de Sauron para desviar su mirada de Frodo y Sam mientras se acercan al Monte del Destino con el Anillo Único.",
        "year": 2003,
        "rating": 8.9,
        "category": "Aventura",
    },
    {
        "id": 6,
        "title": "Forrest Gump",
        "overview": "Las presidencias de Kennedy y Johnson, la guerra de Vietnam, el escándalo de Watergate y otros eventos históricos se desarrollan desde la perspectiva de un hombre de Alabama con un CI de 75.",
        "year": 1994,
        "rating": 8.8,
        "category": "Drama",
    },
    {
        "id": 7,
        "title": "Inception",
        "overview": "Un ladrón que roba secretos corporativos a través del uso de tecnología para compartir sueños recibe la tarea inversa de plantar una idea en la mente de un C.E.O.",
        "year": 2010,
        "rating": 8.8,
        "category": "Acción",
    },
    {
        "id": 8,
        "title": "Matrix",
        "overview": "Un hacker informático aprende de misteriosos rebeldes sobre la verdadera naturaleza de su realidad y su papel en la guerra contra sus controladores.",
        "year": 1999,
        "rating": 8.7,
        "category": "Acción",
    },
    {
        "id": 9,
        "title": "Gladiador",
        "overview": "Un ex general romano busca venganza contra el corrupto emperador que asesinó a su familia y lo envió a la esclavitud.",
        "year": 2000,
        "rating": 8.5,
        "category": "Acción",
    },
    {
        "id": 10,
        "title": "Interestelar",
        "overview": "Un equipo de exploradores viaja a través de un agujero de gusano en el espacio en un intento de asegurar la supervivencia de la humanidad.",
        "year": 2014,
        "rating": 8.6,
        "category": "Aventura",
    },
]


@app.get("/", tags=["Home"])
def message():
    return HTMLResponse("<h1>Hello, world</h1>")


@app.get("/movies", tags=["Movies"])
def get_movies():
    return movies


@app.get("/movies", tags=["Movies"])
@app.get("/movies/{id}")
def get_movie(id: int):
    for item in movies:
        if item["id"] == id:
            return item
    return []


@app.get("/movies/", tags=["Movies"])
def get_movies_by_categories(category: str, year: int):
    return category, year
