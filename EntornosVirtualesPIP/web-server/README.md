## FastAPI

FastAPI es un moderno framework web para construir APIs con Python 3.7+ basado en tipos de Python estándar.

### Requisitos

- Python 3.7+

### Instalación

Para instalar FastAPI y un servidor ASGI, puedes usar pip:

```sh
pip install fastapi "uvicorn[standard]"
```

# Crear una aplicación

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

```

## Correr el servidor

```bash
uvicorn main:app --reload
```

## Despliegue

Para desplegar tu aplicación, puedes usar varios servicios de hosting compatibles con ASGI como:

- Uvicorn
- Daphne
- Hypercorn

```bash
uvicorn main:app
```
