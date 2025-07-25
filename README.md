# ChibchaWeb

Proyecto web desarrollado con Django, con estructura modular separando `backend` y `frontend`. Esta app permite registrar clientes que alojan sitios web, y guarda su información personal, tarjeta y dirección.

---

# Requisitos
- Python 3.10 o superior
- Git
- (Opcional pero recomendado) Visual Studio Code

# Crear y activar el entorno virtual:
- python -m venv venv  en terminal
- venv\Scripts\activate   en cmd

# Instalar dependencias
- pip install django

# Aplicar migraciones
- ython manage.py makemigrations
- python manage.py migrate

# Crear superusuario (opcional para admin)
 -python manage.py createsuperuser

# Ejecutar el servidor
- python manage.py runserver

# Direcciones hasta ahora
 http://127.0.0.1:8000/registrar → formulario de registro de clientes

http://127.0.0.1:8000/admin → panel de administración (requiere superusuario)

# Notas adicionales
La base de datos usada es SQLite (se crea automáticamente).

El entorno virtual y archivos temporales están excluidos vía .gitignore.

Los templates están separados en la carpeta frontend/templates/.