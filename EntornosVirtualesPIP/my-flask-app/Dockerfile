# Utiliza la imagen oficial de Python desde el Docker Hub con la versión 3.9-slim
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor en /app
WORKDIR /app

# Copia el contenido del directorio actual al contenedor en /app
COPY . /app

# Instala los paquetes necesarios especificados en requirements.txt
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

# Expone el puerto 5000 para que esté disponible fuera del contenedor
EXPOSE 5000

# Define la variable de entorno FLASK_APP con el valor 'app.py'
ENV FLASK_APP=app.py

# Ejecuta app.py cuando se inicie el contenedor
CMD ["python", "app/app.py"]
