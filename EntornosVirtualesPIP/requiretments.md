# `requirements.txt`

Archivo que gestiona todas la dependencias del env y en la versión requerida

## Generar requirements.txt

```sh
pip freeze > requirements.txt
```

## Revisar que hay dentro del archivo

```sh
cat requirements.txt
```

## Instalar la dependencias del requirements.txt

```sh
pip3 install -r requirements.txt
```

## Preparar archivo para contribución

### App Project

```sh
git clone
```

```sh
cd app
```

```sh
python3 -m venv env
```

```sh
source env/bin/activate
```

```sh
pip3 install -r requirements.txt
```

```sh
python3 main.py
```
