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