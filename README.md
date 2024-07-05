
# Instrucciones para instalar y usar la API

## Instalación de dependencias
1. Asegúrate de tener Python instalado.
2. Instala Flask, Flask-SQLAlchemy y PyMySQL ejecutando el siguiente comando:
```bash
pip install Flask Flask-SQLAlchemy PyMySQL
```

## Configuración de la base de datos
1. Asegúrate de tener MySQL instalado y ejecutándose.
2. Crea una base de datos en MySQL llamada `MovilesApi`.
3. Modifica la URI de la base de datos en el archivo de la aplicación Flask con tus credenciales MySQL.

## Ejecutar la aplicación
1. Guarda el código de la aplicación Flask en un archivo llamado `app.py`.
2. Ejecuta la aplicación Flask con el siguiente comando:
```bash
python app.py
```
3. La aplicación se ejecutará en `http://127.0.0.1:5000`.

## Uso de los endpoints

### Agregar una nueva rutina (POST /rutine)
- Descripción: Agrega una nueva rutina a la base de datos.
- Endpoint: `/rutine`
- Método: POST
- Body (JSON):
```json
{
  "name": "Nombre de la rutina"
}
```
- Ejemplo usando curl:
```bash
curl -X POST http://127.0.0.1:5000/rutine -H "Content-Type: application/json" -d '{"name": "Mi nueva rutina"}'
```

### Obtener todas las rutinas (GET /rutines)
- Descripción: Obtiene todas las rutinas de la base de datos.
- Endpoint: `/rutines`
- Método: GET
- Ejemplo usando curl:
```bash
curl http://127.0.0.1:5000/rutines
```

### Agregar un nuevo ejercicio a una rutina (POST /exercise)
- Descripción: Agrega un nuevo ejercicio a una rutina específica.
- Endpoint: `/exercise`
- Método: POST
- Body (JSON):
```json
{
  "name": "Nombre del ejercicio",
  "rutine_id": 1
}
```
- Ejemplo usando curl:
```bash
curl -X POST http://127.0.0.1:5000/exercise -H "Content-Type: application/json" -d '{"name": "Ejercicio 1", "rutine_id": 1}'
```

### Obtener todos los ejercicios de una rutina específica (GET /rutine/<int:rutine_id>/exercises)
- Descripción: Obtiene todos los ejercicios asociados a una rutina específica.
- Endpoint: `/rutine/<int:rutine_id>/exercises`
- Método: GET
- Ejemplo usando curl:
```bash
curl http://127.0.0.1:5000/rutine/1/exercises
```

### Agregar un nuevo registro a un ejercicio (POST /register)
- Descripción: Agrega un nuevo registro a un ejercicio específico.
- Endpoint: `/register`
- Método: POST
- Body (JSON):
```json
{
  "kilogram": 50.5,
  "repetitions": 10,
  "series": 3,
  "exercise_id": 1
}
```
- Ejemplo usando curl:
```bash
curl -X POST http://127.0.0.1:5000/register -H "Content-Type: application/json" -d '{"kilogram": 50.5, "repetitions": 10, "series": 3, "exercise_id": 1}'
```

### Obtener todos los registros de un ejercicio específico (GET /exercise/<int:exercise_id>/registers)
- Descripción: Obtiene todos los registros asociados a un ejercicio específico.
- Endpoint: `/exercise/<int:exercise_id>/registers`
- Método: GET
- Ejemplo usando curl:
```bash
curl http://127.0.0.1:5000/exercise/1/registers
```

### Eliminar una rutina (DELETE /rutine/<int:rutine_id>)
- Descripción: Elimina una rutina de la base de datos, incluyendo todos los ejercicios y registros asociados.
- Endpoint: `/rutine/<int:rutine_id>`
- Método: DELETE
- Ejemplo usando curl:
```bash
curl -X DELETE http://127.0.0.1:5000/rutine/1
```

### Actualizar el nombre de un ejercicio (PUT /exercise/<int:exercise_id>)
- Descripción: Actualiza el nombre de un ejercicio específico.
- Endpoint: `/exercise/<int:exercise_id>`
- Método: PUT
- Body (JSON):
```json
{
  "name": "Nuevo nombre"
}
```
- Ejemplo usando curl:
```bash
curl -X PUT http://127.0.0.1:5000/exercise/1 -H "Content-Type: application/json" -d '{"name": "Nuevo nombre"}'
```
