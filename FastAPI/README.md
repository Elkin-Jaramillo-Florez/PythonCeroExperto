# Uso de FastAPI

FastAPI es un framework web rápido (fast) para construir APIs con Python. Aquí se detallan los comandos básicos para ejecutar una aplicación FastAPI.

## Instalación de Dependencias

Para comenzar, necesitas instalar las bibliotecas necesarias. Se puede hacer utilizando `pip`, el gestor de paquetes de Python. Ejecuta el siguiente comando en tu terminal para instalar FastAPI y Uvicorn:

```bash
pip install fastapi "uvicorn[standard]"
```

## Comando de Ejecución

El siguiente comando se utiliza para ejecutar una aplicación FastAPI:

```bash
uvicorn main:app --reload --port 5000 --host 0.0.0.0
```

Donde:

- `main`: Es el nombre del archivo principal de la aplicación.
- `app`: Es el nombre de la instancia de la aplicación en el archivo principal.
- `--reload`: Habilita el recargado automático para detectar cambios y recargar la aplicación.
- `--port`: Especifica el puerto en el que se ejecutará la aplicación.
- `--host`: Especifica la dirección IP del host en el que se ejecutará la aplicación.
