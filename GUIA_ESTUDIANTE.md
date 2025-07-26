
# Guía para Estudiantes - Raíces Vivas

## Introducción al Proyecto

Raíces Vivas es un e-commerce desarrollado en Django que promueve las artesanías Wayuu. Este proyecto te permitirá aprender desarrollo web full-stack mientras trabajas en un caso de uso real y significativo.

## Objetivos de Aprendizaje

### Nivel Básico
- [ ] Entender la estructura de un proyecto Django
- [ ] Modificar contenido HTML básico
- [ ] Personalizar estilos CSS
- [ ] Trabajar con templates de Django

### Nivel Intermedio
- [ ] Crear y modificar modelos de Django
- [ ] Implementar vistas basadas en funciones
- [ ] Trabajar con formularios Django
- [ ] Gestionar archivos estáticos

### Nivel Avanzado
- [ ] Implementar autenticación de usuarios
- [ ] Crear APIs REST con Django REST Framework
- [ ] Optimizar consultas de base de datos
- [ ] Implementar sistemas de pago

## Estructura del Proyecto Explicada

### 1. Directorio Principal
```
wayuu_artesania/
├── manage.py              # Comando principal de Django
├── requirements.txt       # Dependencias del proyecto
├── db.sqlite3            # Base de datos SQLite
└── README_DJANGO.md      # Documentación técnica
```

### 2. Aplicación Principal (api/)
```
api/
├── models.py             # Definición de modelos de datos
├── views.py              # Lógica de vistas de API
├── template_views.py     # Vistas que renderizan templates
├── urls.py               # Configuración de URLs
├── admin.py              # Configuración del panel admin
└── migrations/           # Migraciones de base de datos
```

### 3. Templates (templates/)
```
templates/
├── base.html             # Template base
├── index.html            # Página principal
├── shop.html             # Tienda de productos
├── product.html          # Detalle de producto
├── blog.html             # Página de blog
└── ...                   # Otros templates
```

### 4. Archivos Estáticos (static/)
```
static/
├── css/
│   └── style.css         # Estilos principales
├── js/
│   └── main.js           # JavaScript principal
└── images/               # Imágenes del sitio
```

## Tareas de Práctica

### Semana 1: Familiarización
1. **Explorar la página principal**
   - Navegar por todas las secciones
   - Identificar elementos interactivos
   - Probar la responsividad en móvil

2. **Modificar contenido básico**
   - Cambiar el título principal en `templates/index.html` (línea 52)
   - Personalizar la descripción (línea 56)
   - Actualizar información de artesanas (líneas 200-300)

### Semana 2: Personalización Visual
1. **Cambiar colores del tema**
   - Modificar variables CSS en `static/css/style.css` (líneas 7-21)
   - Experimentar con diferentes paletas de colores

2. **Personalizar imágenes**
   - Reemplazar imágenes del hero (línea 67 en index.html)
   - Cambiar fotos del mosaico (líneas 320-380)
   - Actualizar imágenes de artesanas

### Semana 3: Funcionalidad
1. **Agregar nuevos productos**
   - Usar el panel admin en `/admin`
   - Crear productos con imágenes y descripciones
   - Probar la visualización en la tienda

2. **Crear posts de blog**
   - Escribir artículos sobre cultura Wayuu
   - Agregar imágenes destacadas
   - Configurar como posts destacados

### Semana 4: Características Avanzadas
1. **Personalizar el carrito**
   - Modificar el diseño en `templates/cart.html`
   - Agregar validaciones JavaScript

2. **Mejorar la experiencia de usuario**
   - Añadir animaciones CSS
   - Implementar búsqueda en tiempo real
   - Optimizar para móvil

## Cómo Personalizar el Contenido

### 1. Cambiar Textos Principales

**Título del sitio** (línea 52 en `templates/index.html`):
```html
<h1 class="display-2 fw-bold text-white mb-4">
    TU_NUEVO_TÍTULO<br>
    <span class="text-primary">SUBTÍTULO</span>
</h1>
```

**Descripción principal** (línea 56):
```html
<p class="lead text-white mb-4">
    Tu nueva descripción aquí
</p>
```

### 2. Cambiar Imágenes

**Imagen de fondo del hero** (línea 24):
```css
background: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)),
            url('URL_DE_TU_IMAGEN');
```

**Imagen principal del hero** (línea 67):
```html
<img src="URL_DE_TU_IMAGEN" alt="Descripción" class="img-fluid rounded-3 shadow-lg">
```

### 3. Personalizar Colores

En `static/css/style.css` (líneas 7-21):
```css
:root {
    --primary-color: #TU_COLOR;
    --secondary-color: #TU_COLOR;
    --accent-color: #TU_COLOR;
}
```

### 4. Agregar Nuevas Secciones

Para agregar una nueva sección en la página principal:

1. Abre `templates/index.html`
2. Encuentra donde quieres insertar la sección
3. Agrega el HTML siguiendo este patrón:

```html
<!-- Nueva Sección -->
<section class="py-5 bg-light">
    <div class="container">
        <div class="row">
            <div class="col-lg-12 text-center">
                <h2 class="display-5 fw-bold mb-4">
                    TU <span class="text-primary">TÍTULO</span>
                </h2>
                <p class="lead text-muted mb-5">
                    Tu descripción aquí
                </p>
            </div>
        </div>
        <!-- Contenido de tu sección -->
    </div>
</section>
```

## Comandos Útiles de Django

### Gestión de Base de Datos
```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear datos de muestra
python manage.py create_sample_data
```

### Gestión de Usuarios
```bash
# Crear superusuario
python manage.py createsuperuser

# Cambiar contraseña de usuario
python manage.py changepassword username
```

### Desarrollo
```bash
# Ejecutar servidor de desarrollo
python manage.py runserver 0.0.0.0:3000

# Ejecutar shell de Django
python manage.py shell

# Recolectar archivos estáticos
python manage.py collectstatic
```

## Recursos de Aprendizaje

### Documentación Oficial
- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)
- [JavaScript MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

### Tutoriales Recomendados
- Django for Beginners
- CSS Grid y Flexbox
- JavaScript ES6+

## Resolución de Problemas Comunes

### Error: "No such table"
```bash
python manage.py migrate
python manage.py create_sample_data
```

### Los estilos no se cargan
1. Verificar que `{% load static %}` esté al inicio del template
2. Usar `{% static 'css/style.css' %}` para referenciar archivos

### Imágenes no aparecen
1. Verificar que las URLs sean correctas
2. Asegurarse de que las imágenes estén en el directorio `static/images/`

## Proyectos de Extensión

### Fácil
- [ ] Cambiar todos los textos a tu tema preferido
- [ ] Personalizar la paleta de colores
- [ ] Agregar más productos al catálogo

### Intermedio
- [ ] Crear un sistema de reseñas de productos
- [ ] Implementar filtros avanzados en la tienda
- [ ] Agregar un sistema de favoritos

### Avanzado
- [ ] Integrar pagos con Stripe
- [ ] Implementar un chat en vivo
- [ ] Crear un panel de analytics

## Evaluación y Entregables

### Entrega Básica
- Sitio personalizado con tu propio contenido
- Al menos 5 productos creados
- 3 posts de blog escritos
- Documentación de cambios realizados

### Entrega Avanzada
- Funcionalidad nueva implementada
- Tests unitarios escritos
- Optimizaciones de rendimiento
- Deployment en producción

---

¡Disfruta aprendiendo desarrollo web con Django! 🚀
