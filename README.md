# Blog — Entrega Final

Entrega Final - Curso de Python - CoderHouse  
Alumno: **Nahuel Carrera**

---

## Descripcion del proyecto

Para el proyecto final del curso desarrollé una aplicación web tipo blog usando Django. La idea fue armar algo completo: un sitio donde se pueden publicar articulos, los usuarios se registran con su propio perfil y pueden mandarse mensajes entre ellos. Todo lo construi sobre el proyecto de la entrega anterior, que ya tenia la base del blog con los modelos de Autor, Categoria y Articulo, y lo expandí con autenticacion, perfiles y mensajeria.

El diseño lo trabaje con CSS propio usando una paleta oscura, tipografia Inter de Google Fonts, efectos de glassmorphism en el navbar y animaciones en las cards y transiciones de botones.

---

## Funcionalidades

- Pagina de inicio con las ultimas publicaciones
- Seccion About con informacion del autor del blog
- Listado de articulos con buscador integrado y paginacion
- Vista de detalle de cada articulo con contenido enriquecido (CKEditor)
- Creacion, edicion y borrado de articulos (requiere estar logueado)
- Registro de usuarios con username, email y contrasena
- Login y logout
- Perfil de usuario con nombre, apellido, email, avatar, biografia y fecha de nacimiento
- Edicion de perfil y cambio de contrasena
- Sistema de mensajeria privada entre usuarios con hilo de conversacion
- Panel de administracion con todos los modelos registrados

---

## Requisitos tecnico cumplidos

- Herencia de templates (`base.html` → todas las paginas)
- NavBar completo con accesos condicionales segun si el usuario esta autenticado
- Minimo 2 CBV: `ArticuloListView` (ListView) y `ArticuloDetailView` (DetailView) + `CreateView` y `UpdateView`
- `LoginRequiredMixin` en `ArticuloCreateView` y `ArticuloUpdateView`
- Decorador `@login_required` en la vista `eliminar_articulo`
- Modelo `Articulo` con 2 CharField (titulo, subtitulo), RichTextField (contenido con CKEditor), ImageField (imagen), DateField (fecha_publicacion)
- App `accounts` con modelo `Perfil` para manejo de usuarios
- App `mensajes` con modelo `Mensaje` para mensajeria entre usuarios
- Todos los modelos registrados en el admin
- `requirements.txt` actualizado
- `.gitignore` con `__pycache__/`, `db.sqlite3` y `media/`
- Mensaje "No hay articulos aun" en el listado cuando no hay publicaciones

---

## Estructura del proyecto

```
TuPrimeraPagina+Carrera/
├── mi_blog/                    # Configuracion del proyecto Django
│   ├── settings.py
│   └── urls.py
├── blog/                       # App principal (articulos)
│   ├── models.py               # Autor, Categoria, Articulo (con CKEditor e ImageField)
│   ├── views.py                # CBV: ListView, DetailView, CreateView, UpdateView + @login_required
│   ├── forms.py                # ArticuloForm (ModelForm + CKEditor)
│   ├── urls.py
│   ├── admin.py
│   └── static/blog/css/
│       └── styles.css
├── accounts/                   # App de autenticacion y perfiles
│   ├── models.py               # Perfil (OneToOne con User)
│   ├── views.py                # registro, login, logout, perfil, editar, cambiar password
│   ├── forms.py
│   └── urls.py
├── mensajes/                   # App de mensajeria entre usuarios
│   ├── models.py               # Mensaje (remitente, destinatario, contenido, fecha, leido)
│   ├── views.py                # bandeja, conversacion, nuevo_mensaje
│   ├── forms.py
│   └── urls.py
├── templates/
│   ├── base.html               # Template base con NavBar y mensajes del sistema
│   ├── index.html
│   ├── about.html
│   ├── pages/                  # Templates del blog
│   ├── accounts/               # Templates de autenticacion y perfiles
│   └── mensajes/               # Templates de mensajeria
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

<<<<<<< HEAD
## Como instalar y ejecutar
Clonar el repositorio y entrar a la carpeta:
## 1
git clone <URL_DEL_REPOSITORIO>
## 2
cd TuPrimeraPagina+Carrera
## 3
Crear un entorno virtual y activarlo
## 4
Instalar las dependencias:
## 5
pip install -r requirements.txt
## 6
Aplicar las migraciones:
python manage.py migrate
## 7
Ejecutar el servidor:
python manage.py runserver
## 8
Abrir en el navegador: http://127.0.0.1:8000/
Orden de prueba de funcionalidades
Inicio (/) — Pagina principal con descripcion de las secciones disponibles.
Autores (/crear-autor/) — Registrar al menos un autor antes de crear articulos.
Categorias (/crear-categoria/) — Registrar al menos una categoria antes de crear articulos.
Articulos (/crear-articulo/) — Completar titulo, contenido, seleccionar autor y categoria.
Buscar (/buscar/) — Escribir un titulo o parte del mismo y presionar Buscar.
=======
---

## Instalacion y ejecucion local

1. Clonar el repositorio:
```bash
git clone <url-del-repo>
cd TuPrimeraPagina+Carrera
```

2. Crear y activar el entorno virtual:
```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Aplicar migraciones:
```bash
python manage.py migrate
```

5. Crear un superusuario para el panel de admin:
```bash
python manage.py createsuperuser
```

6. Correr el servidor:
```bash
python manage.py runserver
```

7. Abrir el navegador en `http://127.0.0.1:8000/`

---

## Tecnologias usadas

- Python 3.14
- Django 6.0
- django-ckeditor 6.7 (texto enriquecido)
- Pillow 12.2 (manejo de imagenes)
- SQLite (base de datos)
- HTML + CSS puro (sin frameworks de UI)
- Google Fonts — Inter
>>>>>>> cc2fb08 (entrega final - blog Django con autenticacion, perfiles y mensajeria)
