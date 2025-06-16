# Biblioteca de Desarrollo Personal

## Descripción

Aplicación web desarrollada con Django que permite crear y gestionar posts sobre desarrollo personal. Los usuarios pueden crear posts, filtrar por autor y categoría, y buscar contenido específico.

## Características

- Creación de posts con título, contenido, autor y categoría
- Búsqueda de posts por título
- Filtrado por autor y categoría
- Interfaz responsive con Bootstrap
- Panel de administración personalizado

## Tecnologías Utilizadas

- Python 3.x
- Django 4.x
- Bootstrap 4.5
- SQLite (base de datos)

## Estructura del Proyecto

```
├── config/                 # Configuración principal de Django
│   ├── settings.py        # Configuraciones del proyecto
│   ├── urls.py           # URLs principales
│   └── wsgi.py           # Configuración WSGI
├── core/                  # Aplicación principal
│   ├── models.py         # Modelos de datos
│   ├── views.py          # Vistas y lógica
│   ├── forms.py          # Formularios
│   ├── admin.py          # Configuración del admin
│   └── templates/        # Plantillas HTML
├── docs/                  # Documentación
└── .venv/                # Entorno virtual
```

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/NicoStocchero/Coder-Python-Django
cd Coder-Python-Django
```

2. Crear y activar entorno virtual:

```bash
python -m venv .venv
# En Windows:
.venv\Scripts\activate
# En Unix/MacOS:
source .venv/bin/activate
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

4. Aplicar migraciones:

```bash
python manage.py migrate
```

5. Crear superusuario (opcional):

```bash
python manage.py createsuperuser
```

6. Ejecutar el servidor:

```bash
python manage.py runserver
```

## Uso

- Acceder a `http://localhost:8000` para ver la aplicación
- Acceder a `http://localhost:8000/admin` para el panel de administración

## Información del Curso

- Comisión: 69560
- Alumno: Nicolás Stocchero

## Licencia

Este proyecto es parte del curso de Python de Coderhouse.
