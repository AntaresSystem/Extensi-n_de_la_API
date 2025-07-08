# API de Gestión de Tareas (ToDo List)

## Requisitos
- Python 3.10+
- Django 5.2.2
- Django REST Framework

## Instalación
1. Clona el repositorio
2. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```
3. Aplica las migraciones:
   ```
   python manage.py migrate
   ```
4. Ejecuta el servidor:
   ```
   python manage.py runserver
   ```

## Endpoints
- Listar y crear tareas: `http://localhost:8000/api/tareas/`

## Panel de administración
- `http://localhost:8000/admin/`

## Autenticación JWT

1. Obtén el token de acceso:
   
   **Con curl:**
   ```bash
   curl -X POST http://localhost:8000/api/token/ \
        -H "Content-Type: application/json" \
        -d '{"username": "tu_usuario", "password": "tu_contraseña"}'
   ```
   
   **Con Postman:**
   - Método: POST
   - URL: http://localhost:8000/api/token/
   - Body: raw, JSON
     ```json
     {
       "username": "tu_usuario",
       "password": "tu_contraseña"
     }
     ```
   - Recibirás un `access` y un `refresh` token.

2. Usa el token para acceder a los endpoints protegidos:
   
   **Con curl:**
   ```bash
   curl -X GET http://localhost:8000/api/tareas/ \
        -H "Authorization: Bearer TU_TOKEN_AQUI"
   ```
   
   **Con Postman:**
   - Método: GET
   - URL: http://localhost:8000/api/tareas/
   - En la pestaña "Authorization", selecciona "Bearer Token" e ingresa tu token de acceso.

3. Crear una tarea (requiere autenticación):
   
   **Con curl:**
   ```bash
   curl -X POST http://localhost:8000/api/tareas/ \
        -H "Authorization: Bearer TU_TOKEN_AQUI" \
        -H "Content-Type: application/json" \
        -d '{"titulo": "Nueva tarea", "descripcion": "Descripción", "completado": false}'
   ```
   
   **Con Postman:**
   - Método: POST
   - URL: http://localhost:8000/api/tareas/
   - Body: raw, JSON
     ```json
     {
       "titulo": "Nueva tarea",
       "descripcion": "Descripción",
       "completado": false
     }
     ```
   - En la pestaña "Authorization", selecciona "Bearer Token" e ingresa tu token de acceso.

## Filtros y paginación
- Puedes filtrar tareas por título o completado:
  - `http://localhost:8000/api/tareas/?completado=true`
  - `http://localhost:8000/api/tareas/?titulo=Trabajo`
- La paginación está habilitada (10 tareas por página por defecto).

## Ejemplos de uso de la API con Postman y JWT

### 1. Obtener token JWT

- **Método:** POST
- **URL:** http://127.0.0.1:8000/api/token/
- **Body:**
```json
{
  "username": "tu_usuario",
  "password": "tu_contraseña"
}
```
- **Respuesta esperada:**
```json
{
  "refresh": "<token_refresh>",
  "access": "<token_access>"
}
```

### 2. Usar el token para autenticarte
- En cada petición protegida, ve a la pestaña "Authorization", selecciona "Bearer Token" y pega el token de acceso.

---

### 3. Listar tareas
- **Método:** GET
- **URL:** http://127.0.0.1:8000/api/tareas/
- **Authorization:** Bearer Token
- **Respuesta esperada:**
```json
{
  "count": 3,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "usuario": "Albert",
      "titulo": "Tarea actualizada",
      "descripcion": "Descripción actualizada",
      "completado": false
    },
    {
      "id": 2,
      "usuario": "Albert",
      "titulo": "Primera tarea - prueba 1",
      "descripcion": "Ejecutar comandos sencillos desde Django y probar un Get en Postman",
      "completado": true
    },
    {
      "id": 5,
      "usuario": "Albert",
      "titulo": "Nueva tarea desde API",
      "descripcion": "Tarea creada mediante Postman",
      "completado": true
    }
  ]
}
```

---

### 4. Filtros
- **Por completado:**
  - GET http://127.0.0.1:8000/api/tareas/?completado=true
- **Por título:**
  - GET http://127.0.0.1:8000/api/tareas/?titulo=prueba

---

### 5. Crear una tarea
- **Método:** POST
- **URL:** http://127.0.0.1:8000/api/tareas/
- **Authorization:** Bearer Token
- **Body:**
```json
{
  "titulo": "Nueva tarea desde API",
  "descripcion": "Tarea creada mediante Postman",
  "completado": false
}
```
- **Respuesta esperada:**
```json
{
  "id": 5,
  "usuario": "Albert",
  "titulo": "Nueva tarea desde API",
  "descripcion": "Tarea creada mediante Postman",
  "completado": false
}
```

---

### 6. Actualizar una tarea
- **Método:** PATCH
- **URL:** http://127.0.0.1:8000/api/tareas/1/
- **Authorization:** Bearer Token
- **Body:**
```json
{
  "titulo": "Tarea actualizada",
  "descripcion": "Descripción actualizada"
}
```
- **Respuesta esperada:**
```json
{
  "id": 1,
  "usuario": "Albert",
  "titulo": "Tarea actualizada",
  "descripcion": "Descripción actualizada",
  "completado": false
}
```

---

### 7. Eliminar una tarea
- **Método:** DELETE
- **URL:** http://127.0.0.1:8000/api/tareas/4/
- **Authorization:** Bearer Token
- **Respuesta esperada:** Código 204 No Content

---

### 8. Acceso sin autenticación
- Si intentas acceder a cualquier endpoint protegido sin token, recibirás:
```json
{
  "detail": "Authentication credentials were not provided."
}
``` 
## Evidencia de la documentación automática con Swagger

A continuación se muestran capturas de pantalla de la API documentada y funcionando en Swagger UI:

![Swagger UI 1](docs/swagger_ui_1.png)
![Swagger UI 2](docs/swagger_ui_2.png)
![Swagger UI 3](docs/swagger_ui_3.png)
![Swagger UI 4](docs/swagger_ui_4.png)
![Swagger UI 5](docs/swagger_ui_5.png)
![Swagger UI 6](docs/swagger_ui_6.png)
![Swagger UI 7](docs/swagger_ui_7.png)
![Swagger UI 8](docs/swagger_ui_8.png)
![Swagger UI 9](docs/swagger_ui_9.png)
![Swagger UI 10](docs/swagger_ui_10.png)
![Swagger UI 11](docs/swagger_ui_11.png)
![Swagger UI 12](docs/swagger_ui_12.png)