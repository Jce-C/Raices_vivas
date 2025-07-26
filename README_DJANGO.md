
# Raíces Vivas - Plataforma E-commerce Django

Un sistema completo de e-commerce desarrollado en **Django** que conecta artesanas Wayuu con compradores globales, promoviendo la preservación cultural a través del comercio digital.

## 🌟 Características Principales

### 🏠 **Frontend Completo**
- **Homepage Interactiva**: Hero section con diseño responsivo
- **Tienda (Shop)**: Catálogo completo con filtros, búsqueda y paginación
- **Detalle de Producto**: Vista individual con información completa
- **Blog Cultural**: Sistema de gestión de contenido con editor HTML
- **Sistema de Usuarios**: Registro, login, perfil y gestión de sesiones
- **Carrito de Compras**: Funcionalidad completa de e-commerce
- **Panel Administrativo**: Interface personalizada para gestión

### ⚙️ **Backend Robusto**
- **API REST Completa**: Endpoints para todas las funcionalidades
- **Sistema de Autenticación**: Token-based con Django REST Framework
- **Base de Datos Optimizada**: Modelos relacionales bien estructurados
- **Panel Admin Personalizado**: Django Admin con interfaces custom
- **Gestión de Archivos**: Sistema para imágenes y contenido multimedia

### 🎨 **Diseño y UX**
- **Responsive Design**: Optimizado para móvil, tablet y desktop
- **Bootstrap 5**: Framework CSS moderno y componentes personalizados
- **Paleta Wayuu**: Colores auténticos inspirados en la cultura
- **Navegación Intuitiva**: Menús flotantes y estructura clara
- **Animaciones CSS**: Transiciones suaves y efectos visuales

## 🚀 Tecnologías Utilizadas

```
Backend:
├── Django 4.2.7              # Framework web principal
├── Django REST Framework      # API REST
├── SQLite                     # Base de datos (desarrollo)
├── Python 3.11               # Lenguaje principal
└── Gunicorn 21.2.0           # Servidor WSGI (producción)

Frontend:
├── HTML5 + CSS3              # Estructura y estilos
├── Bootstrap 5               # Framework CSS
├── JavaScript ES6+           # Interactividad
├── Font Awesome             # Iconografía
└── Custom CSS Variables     # Tema personalizable

Herramientas:
├── python-decouple          # Gestión de configuración
├── django-cors-headers      # CORS para API
├── django-filter           # Filtros avanzados
└── Replit                  # Hosting y desarrollo
```

## 📁 Estructura Detallada del Proyecto

```
wayuu_artesania/
├── 📁 api/                          # Aplicación principal Django
│   ├── 📄 models.py                 # Modelos: User, Product, Category, etc.
│   ├── 📄 views.py                  # Vistas API con DRF
│   ├── 📄 template_views.py         # Vistas para templates HTML
│   ├── 📄 serializers.py            # Serializadores DRF
│   ├── 📄 admin.py                  # Configuración Django Admin
│   ├── 📄 urls.py                   # URLs de la API
│   ├── 📄 template_urls.py          # URLs para templates
│   ├── 📁 migrations/               # Migraciones de base de datos
│   ├── 📁 management/commands/      # Comandos personalizados
│   └── 📁 templatetags/             # Tags personalizados
├── 📁 templates/                    # Templates HTML
│   ├── 📄 base.html                 # Template base
│   ├── 📄 index.html                # Página principal
│   ├── 📄 shop.html                 # Catálogo de productos
│   ├── 📄 product.html              # Detalle de producto
│   ├── 📄 blog.html                 # Lista de blog posts
│   ├── 📄 cart.html                 # Carrito de compras
│   └── 📄 ...                       # Otros templates
├── 📁 static/                       # Archivos estáticos
│   ├── 📁 css/
│   │   └── 📄 style.css             # Estilos principales
│   ├── 📁 js/
│   │   └── 📄 main.js               # JavaScript principal
│   ├── 📁 images/                   # Imágenes del sitio
│   └── 📁 admin/                    # Estilos admin personalizados
├── 📁 wayuu_artesania/              # Configuración Django
│   ├── 📄 settings.py               # Configuraciones del proyecto
│   ├── 📄 urls.py                   # URLs principales
│   └── 📄 wsgi.py                   # Configuración WSGI
├── 📄 manage.py                     # Comando principal Django
├── 📄 requirements.txt              # Dependencias Python
├── 📄 render.yaml                   # Configuración para Render
└── 📄 db.sqlite3                    # Base de datos SQLite
```

## 🔧 Instalación y Configuración

### 1. **Preparar el Entorno**
El proyecto está configurado para funcionar automáticamente en Replit. Si trabajas localmente:

```bash
# Instalar dependencias
pip install -r requirements.txt
```

### 2. **Configurar la Base de Datos**
```bash
# Aplicar migraciones
python manage.py migrate

# Crear datos de muestra (productos, categorías, blog posts)
python manage.py create_sample_data

# Crear superusuario para el admin
python manage.py createsuperuser
```

### 3. **Ejecutar el Servidor**
```bash
# Desarrollo en Replit
python manage.py runserver 0.0.0.0:3000

# Desarrollo local
python manage.py runserver
```

### 4. **Acceder a la Aplicación**
- **Frontend**: `http://localhost:3000/` (o URL de Replit)
- **Admin Panel**: `http://localhost:3000/admin/`
- **API**: `http://localhost:3000/api/`

## 📖 API Endpoints Completos

### 🔐 **Autenticación**
```
POST /api/auth/register/          # Registro de usuario
POST /api/auth/login/             # Inicio de sesión
POST /api/auth/logout/            # Cerrar sesión
GET  /api/auth/profile/           # Perfil del usuario actual
```

### 🛍️ **Productos y Catálogo**
```
GET  /api/products/               # Lista de productos (con filtros)
GET  /api/products/{id}/          # Detalle de producto específico
GET  /api/products/featured/      # Productos destacados
GET  /api/categories/             # Lista de categorías
GET  /api/categories/{id}/products/ # Productos por categoría
```

### 🛒 **Carrito de Compras**
```
GET    /api/cart/                 # Items del carrito actual
POST   /api/cart/                 # Agregar producto al carrito
PUT    /api/cart/{item_id}/       # Actualizar cantidad
DELETE /api/cart/{item_id}/       # Eliminar item del carrito
DELETE /api/cart/clear/           # Vaciar carrito completo
```

### 📰 **Blog y Contenido**
```
GET  /api/blog/                   # Lista de posts del blog
GET  /api/blog/{slug}/            # Detalle de post específico
GET  /api/blog/featured/          # Posts destacados
```

### 👥 **Artesanas**
```
GET  /api/artisans/               # Lista de artesanas
GET  /api/artisans/{id}/          # Perfil de artesana
GET  /api/artisans/{id}/products/ # Productos de una artesana
```

## 🌐 URLs del Frontend

### 📄 **Páginas Principales**
```
/                                 # Página de inicio
/shop/                           # Catálogo de productos
/shop/category/{slug}/           # Productos por categoría
/product/{id}/                   # Detalle de producto
/blog/                           # Lista de blog posts
/blog/{slug}/                    # Post individual
/contact/                        # Página de contacto
```

### 👤 **Sistema de Usuarios**
```
/login/                          # Iniciar sesión
/register/                       # Registro de usuario
/profile/                        # Perfil del usuario
/cart/                           # Carrito de compras
/checkout/                       # Proceso de compra
/logout/                         # Cerrar sesión
```

### ⚙️ **Administración**
```
/admin/                          # Panel Django Admin
/admin/add-product/              # Agregar producto (staff)
/admin/add-blog-post/            # Agregar post (staff)
```

## 🎨 Guía de Personalización

### 📝 **Modificar Textos**

**Página Principal** (`templates/index.html`):
```html
<!-- Hero Section - Líneas 45-60 -->
<h1 class="display-2 fw-bold text-white mb-4">
    Raíces Vivas <!-- ← Cambiar título principal -->
    <br><span class="text-primary">Artesanías Wayuu</span>
</h1>
<p class="lead text-white mb-4">
    Tu nueva descripción aquí <!-- ← Cambiar descripción -->
</p>

<!-- Secciones de contenido -->
<h2 class="text-center mb-5">
    <span class="text-primary">Nuevo</span> Título de Sección
</h2>
```

**Navegación** (`templates/base.html`):
```html
<!-- Líneas 20-40 -->
<a class="navbar-brand fw-bold" href="{% url 'home' %}">
    <img src="{% static 'images/tu_logo.png' %}" alt="Tu Marca" height="40">
    Tu Marca <!-- ← Cambiar nombre de la marca -->
</a>
```

### 🎨 **Personalizar Colores**

**Variables CSS** (`static/css/style.css`):
```css
/* Líneas 1-15 - Variables de colores */
:root {
    --primary-color: #C58B44;        /* Color principal */
    --secondary-color: #D49C55;      /* Color secundario */
    --accent-color: #8B4513;         /* Color de acento */
    --text-dark: #2C3E50;            /* Texto oscuro */
    --text-light: #6C757D;           /* Texto claro */
    --background-light: #F8F9FA;     /* Fondo claro */
    --border-color: #E9ECEF;         /* Bordes */
}

/* Personalizar colores Bootstrap */
.btn-primary {
    background-color: var(--primary-color);
    border-color: var(--primary-color);
}
```

### 🖼️ **Cambiar Imágenes**

**Logo** (reemplazar archivo):
```bash
# Colocar tu logo en: static/images/logo_raices_vivas.png
# Tamaño recomendado: 200x60px
```

**Hero Section** (`templates/index.html`):
```html
<!-- Línea 67 -->
<img src="https://tu-url-de-imagen.com/hero.jpg" 
     alt="Descripción" 
     class="img-fluid rounded-3 shadow-lg">
```

**Imágenes de fondo** (`static/css/style.css`):
```css
/* Líneas 120-130 */
.hero-section {
    background: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)),
                url('https://tu-url-de-fondo.com/bg.jpg');
    background-size: cover;
    background-position: center;
}
```

## 🗄️ Gestión de Contenido

### 🛍️ **Agregar Productos**

1. **Via Admin Panel**:
   - Ir a `/admin/`
   - Login con credenciales de administrador
   - `Products` → `Add Product`
   - Llenar todos los campos requeridos

2. **Campos del Producto**:
   - **Nombre**: Título del producto
   - **Descripción**: Texto descriptivo (acepta HTML)
   - **Precio**: En pesos colombianos
   - **Imagen**: URL de la imagen principal
   - **Categoría**: Seleccionar categoría existente
   - **Artesana**: Información de quien lo creó
   - **Is Featured**: Marcar para destacar en homepage

### 📰 **Crear Posts de Blog**

1. **Via Admin Panel**:
   - `Blog posts` → `Add Blog post`
   - El contenido acepta HTML completo

2. **Ejemplo de contenido HTML**:
```html
<h2>Título de la Sección</h2>
<p>Párrafo normal con <strong>texto en negrita</strong> y <em>cursiva</em>.</p>

<h3>Subtítulo</h3>
<p>Otro párrafo con <a href="https://ejemplo.com">enlace externo</a>.</p>

<img src="https://ejemplo.com/imagen.jpg" alt="Descripción" 
     style="max-width: 100%; height: auto; border-radius: 8px;">

<ul>
    <li>Elemento de lista 1</li>
    <li>Elemento de lista 2</li>
</ul>
```

### 👥 **Gestionar Artesanas**

1. **Crear perfil de artesana**:
   - `Artisans` → `Add Artisan`
   - Información personal y profesional
   - Historia personal (acepta HTML)
   - Imagen de perfil

2. **Asociar productos**:
   - Al crear productos, seleccionar la artesana
   - Automáticamente aparecerán en su perfil

## 🛠️ Comandos de Desarrollo

### 📊 **Base de Datos**
```bash
# Crear migraciones cuando cambies modelos
python manage.py makemigrations

# Aplicar migraciones a la base de datos
python manage.py migrate

# Resetear base de datos (cuidado: borra todo)
python manage.py flush

# Crear datos de muestra
python manage.py create_sample_data
```

### 👤 **Gestión de Usuarios**
```bash
# Crear superusuario
python manage.py createsuperuser

# Cambiar contraseña de usuario
python manage.py changepassword username

# Crear usuario staff (puede gestionar contenido)
python manage.py shell
>>> from api.models import User
>>> user = User.objects.create_user('staff', 'staff@example.com', 'password')
>>> user.is_staff = True
>>> user.save()
```

### 🔧 **Desarrollo**
```bash
# Acceder al shell de Django (para pruebas)
python manage.py shell

# Verificar configuración del proyecto
python manage.py check

# Recolectar archivos estáticos (para producción)
python manage.py collectstatic

# Ver todas las URLs disponibles
python manage.py show_urls
```

## 🚀 Despliegue y Producción

### 🔧 **Configuración para Replit Deployments**

El proyecto está listo para desplegar en Replit:

1. **Usar Replit Deployments**:
   - Ve a la pestaña "Deployments"
   - Selecciona "Autoscale Deployment"
   - Configura las variables de entorno necesarias
   - Haz clic en "Deploy"

2. **Variables de Entorno Recomendadas**:
```bash
SECRET_KEY=tu-clave-secreta-muy-larga-y-compleja
DEBUG=False
ALLOWED_HOSTS=tu-dominio.replit.app,tu-dominio-personalizado.com
```

### 🌐 **Configuración para Render (Alternativa)**

Si decides usar Render, el archivo `render.yaml` ya está configurado:

```yaml
services:
  - type: web
    name: raices-vivas
    env: python
    buildCommand: "pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate"
    startCommand: "gunicorn wayuu_artesania.wsgi:application"
    envVars:
      - key: SECRET_KEY
        generateValue: true
      - key: DEBUG
        value: "False"
      - key: ALLOWED_HOSTS
        value: "*"
```

## 🔍 Resolución de Problemas

### ❌ **Errores Comunes**

**"no such table" o "relation does not exist"**:
```bash
python manage.py migrate
python manage.py create_sample_data
```

**Los estilos CSS no cargan**:
1. Verificar que `{% load static %}` esté al inicio del template
2. Usar `{% static 'css/style.css' %}` para referenciar archivos
3. Ejecutar `python manage.py collectstatic` si es necesario

**Imágenes no aparecen**:
1. Verificar URLs de imágenes externas
2. Para imágenes locales, colocar en `static/images/`
3. Usar `{% static 'images/nombre.jpg' %}` en templates

**Error 500 en producción**:
1. Verificar `DEBUG = False` en settings
2. Configurar `ALLOWED_HOSTS` correctamente
3. Revisar logs del servidor

### 🔧 **Modo Debug**

Para activar información detallada de errores:

```python
# En wayuu_artesania/settings.py
DEBUG = True
ALLOWED_HOSTS = ['*']  # Solo para desarrollo
```

## 📈 Características Avanzadas

### 🔍 **Sistema de Búsqueda**
- Búsqueda por nombre y descripción de productos
- Filtros por categoría, precio y artesana
- Búsqueda en blog posts

### 📱 **Responsividad**
- **Móvil**: Navegación con menú hamburguesa
- **Tablet**: Layout adaptativo de dos columnas
- **Desktop**: Experiencia completa con sidebar

### 🛡️ **Seguridad**
- CSRF protection habilitado
- Autenticación basada en tokens
- Validación de datos en formularios
- Sanitización de contenido HTML

### ⚡ **Rendimiento**
- Consultas optimizadas con `select_related`
- Paginación en listados largos
- Compresión de archivos estáticos

## 📚 Recursos Adicionales

### 📖 **Documentación**
- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Bootstrap 5 Documentation](https://getbootstrap.com/docs/5.0/)

### 🎓 **Para Estudiantes**
- Ver `GUIA_ESTUDIANTE.md` para ejercicios prácticos
- Revisar `PROYECTO_COMPLETO.md` para descripción detallada
- Explorar el código comentado para entender la estructura

### 🤝 **Contribuir**
Este proyecto está diseñado para fines educativos. Los estudiantes pueden:
- Personalizar completamente el contenido
- Agregar nuevas funcionalidades
- Mejorar el diseño y UX
- Implementar nuevas características

---

**🌟 ¡Tu plataforma Raíces Vivas está lista para conectar el arte Wayuu con el mundo! 🌟**

*Última actualización: Enero 2025*
