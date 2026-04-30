# TuPrimeraPagina+Carrera

Tercera Entrega - Curso de Python - CoderHouse  
Alumno: **Nahuel Carrera**

## Descripcion del proyecto

Sitio web desarrollado con Django utilizando el patron MVT (Model-View-Template).  
Permite gestionar autores, categorias y articulos, ademas de buscar articulos existentes por titulo.

## Requisitos cumplidos

- [x] Herencia de HTML (`base.html` → todas las paginas heredan de este template)
- [x] 3 clases en models: `Autor`, `Categoria`, `Articulo`
- [x] Un formulario para insertar datos por cada modelo creado
- [x] Un formulario para buscar articulos en la BD por titulo
- [x] README con instrucciones

## Estructura del proyecto

```
TuPrimeraPagina+Carrera/
├── mi_blog/                        # Configuracion del proyecto Django
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── blog/                           # App principal
│   ├── models.py                   # 3 modelos: Autor, Categoria, Articulo
│   ├── views.py                    # Vistas MVT
│   ├── forms.py                    # Formularios de carga y busqueda
│   ├── urls.py                     # Rutas de la app
│   ├── admin.py                    # Registro de modelos en admin
│   └── static/blog/css/
│       └── styles.css              # Hoja de estilos separada
├── templates/                      # Plantillas HTML
│   ├── base.html                   # Template base (herencia)
│   ├── index.html                  # Pagina de inicio
│   └── pages/
│       ├── crear_autor.html
│       ├── crear_categoria.html
│       ├── crear_articulo.html
│       └── buscar_articulos.html
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```