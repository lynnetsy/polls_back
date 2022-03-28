# Polls Backend

Este proyecto es una API construida con el microframework Flask,
expone 2 endpoints:

* POST `/api/v1/polls`: Este endpoint sirve para almacenar en la db las respuestas de una encuesta.
* GET `/api/v1/polls/stats`: Este endpoint devuelve en formato JSON estadísticas obtenidas de las respuestas de la encuesta.

## Requerimientos

* GIT
* DOCKER

## Imagen docker
https://hub.docker.com/r/lynnete/polls

## Instalacion y ejecucion

1. Clonar este repositorio en local
```
git@github.com:lynnetsy/polls_back.git
```
2. Crear y configurar el archivo de entorno
```
cp .env.example .env
```
3. Construir la imagen docker
```
docker-compose build
```
4. Ejecutar el archivo docker-compose
```
docker-compose up -d
```
5. Acceder a la imagen docker
```
docker-compose exec polls_flask sh
```
6. Ejecutar migraciones
```
flask db stamp
flask db migrate
flask db upgrade
```
7. Ejecutar seeders.
```
flask seed run --root ms/db/seeders
```
8. Consumir el API en alguna herramienta como Postman usando el host `http://localhost:8080`


