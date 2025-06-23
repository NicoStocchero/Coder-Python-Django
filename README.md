# Biblioteca de Desarrollo Personal

## Descripción

Aplicación web desarrollada con Django que permite crear y gestionar posts sobre desarrollo personal. Los usuarios pueden crear posts, filtrar por autor y categoría, buscar contenido específico y leer posts completos en una vista detallada.

## Características

- Creación de posts con título, contenido, autor y categoría
- Búsqueda de posts por título
- Filtrado por autor y categoría
- Vista detallada de posts individuales
- Interfaz responsive con Bootstrap
- Panel de administración personalizado
- Navegación intuitiva y diseño moderno
- Animaciones suaves para mejor experiencia de usuario

## Tecnologías Utilizadas

- Python 3.x
- Django 5.x
- widget_tweaks (mejoras en formularios)
- Bootstrap 4.5
- Font Awesome 5.15.4 (iconos)
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
│       ├── base.html     # Plantilla base
│       ├── home.html     # Página principal
│       ├── about.html    # Sobre Mi
│       ├── search.html   # Búsqueda
│       ├── result.html   # Resultados
│       ├── post_*        # list, form, delete, detail
│       ├── author_*      # list, form, delete
│       └── category_*    # list, form, delete
├── users/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── signals.py
│   └── templates/users/
│       ├── login.html
│       ├── signup.html
│       ├── profile.html
│       └──  profile_edit.html
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
- Funcionalidades principales:
  - Ver lista de posts en la página principal
  - Crear nuevos posts
  - Buscar posts por título
  - Filtrar por autor y categoría
  - Ver posts completos en vista detallada
  - Navegar entre diferentes secciones
  - Login, registro y logout de usuarios
  - Vista de perfil con avatar, bio y fecha de nacimiento
  - Edición de perfil personalizada
  - Formularios estilizados con Bootstrap y widget_tweaks
  - Mensajes contextuales con Django messages

## Características de UX/UI

- Diseño responsive y moderno
- Animaciones suaves en interacciones
- Iconos intuitivos
- Navegación clara y consistente
- Formato de fecha legible
- Botones de acción contextuales
- Diseño centrado en la legibilidad

## Autor

Este proyecto fue desarrollado por [Nicolás Stocchero](https://www.linkedin.com/in/nicostocchero/) como parte de la entrega final del curso de Python con Django en Coderhouse.  
Apasionado por crear soluciones digitales que combinan diseño, lógica y experiencia de usuario.

## Información del Curso

- Comisión: 69560
- Alumno: Nicolás Stocchero

## Licencia

Este proyecto es parte del curso de Python de Coderhouse.
