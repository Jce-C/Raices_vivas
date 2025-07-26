
# 🌟 Raíces Vivas - Plataforma de Artesanías Wayuu

## 📋 Descripción del Proyecto

**Raíces Vivas** es una plataforma web de e-commerce especializada en artesanías tradicionales Wayuu. El proyecto está desarrollado en Django y ofrece una experiencia completa para la venta y promoción de productos artesanales auténticos.

## 🎯 Estado Actual del Proyecto

### ✅ Funcionalidades Implementadas

#### 🏠 **Frontend**
- **Página de Inicio** - Hero section con carrusel de productos destacados
- **Tienda (Shop)** - Catálogo completo con filtros y paginación
- **Página de Producto** - Vista detallada con galería de imágenes
- **Blog** - Sistema de publicaciones con contenido HTML
- **Contacto** - Formulario de contacto funcional
- **Sistema de Usuarios** - Login, registro y perfil
- **Carrito de Compras** - Funcionalidad básica implementada

#### ⚙️ **Backend**
- **Panel de Administración** - Django Admin personalizado
- **API REST** - Endpoints completos para frontend alternativo
- **Base de Datos** - SQLite con modelos completos
- **Autenticación** - Sistema de usuarios con permisos
- **Gestión de Contenido** - CRUD completo para productos y blog

#### 🎨 **Diseño**
- **Responsive Design** - Optimizado para móviles y desktop
- **Bootstrap 5** - Framework CSS moderno
- **Colores Wayuu** - Paleta auténtica con tonos tierra
- **Componentes Personalizados** - Cards, botones y navegación única

### 🔧 **Tecnologías Utilizadas**

```
Backend:
- Django 4.2.7
- Django REST Framework
- SQLite Database
- Python 3.11

Frontend:
- HTML5 + CSS3
- Bootstrap 5
- JavaScript (Vanilla)
- Font Awesome Icons

Hosting:
- Replit (Desarrollo)
- Configurado para despliegue
```

## 📁 Estructura del Proyecto

```
workspace/
├── api/                     # Aplicación principal Django
│   ├── models.py           # Modelos de datos
│   ├── views.py           # Vistas API
│   ├── template_views.py  # Vistas del frontend
│   ├── template_urls.py   # URLs del frontend
│   ├── admin.py           # Configuración admin
│   └── migrations/        # Migraciones de DB
├── templates/              # Templates HTML
│   ├── base.html          # Template base
│   ├── index.html         # Página principal
│   ├── shop.html          # Tienda
│   ├── product.html       # Producto individual
│   ├── blog.html          # Blog
│   └── ...
├── static/                 # Archivos estáticos
│   ├── css/style.css      # Estilos principales
│   ├── js/main.js         # JavaScript
│   └── images/            # Imágenes
└── wayuu_artesania/       # Configuración Django
    ├── settings.py        # Configuraciones
    └── urls.py           # URLs principales
```

## 🚀 Guía de Personalización

### 📝 **Cambiar Textos de la Página Principal**

Los textos principales se encuentran en `templates/index.html`:

```html
<!-- Hero Section -->
<h1 class="display-3 fw-bold text-white mb-4">
    Raíces Vivas <!-- Cambiar título principal -->
</h1>
<p class="lead text-white-75 mb-5">
    Descubre la autenticidad... <!-- Cambiar descripción -->
</p>

<!-- Secciones de contenido -->
<h5 class="card-title">Arte Wayuu Ancestral</h5> <!-- Títulos de cards -->
<p class="card-text">Cada pieza cuenta una historia...</p> <!-- Descripciones -->
```

### 🖼️ **Cambiar Imágenes**

Para personalizar las imágenes, reemplaza las URLs en los templates:

```html
<!-- En index.html -->
<img src="TU_NUEVA_URL_DE_IMAGEN" alt="Descripción" class="card-img-top">

<!-- Para el logo en base.html -->
<img src="{% static 'images/logo_raices_vivas.png' %}" alt="Raíces Vivas">
```

**Ubicaciones de imágenes principales:**
- Logo: `static/images/logo_raices_vivas.png`
- Hero section: Carrusel en `index.html`
- Cards de productos: URLs en la base de datos
- Blog: URLs en los posts del admin

### 🎨 **Cambiar Colores y Estilos**

Los colores principales están en `static/css/style.css`:

```css
:root {
    --primary-color: #C58B44;    /* Cambiar color principal */
    --secondary-color: #D49C55;  /* Color secundario */
    --accent-color: #8B4513;     /* Color de acento */
    --text-dark: #2C3E50;        /* Texto oscuro */
}
```

### 📊 **Gestión de Contenido**

#### **Agregar Productos:**
1. Ir a `/admin/`
2. Login con credenciales de administrador
3. Ir a "Products" → "Add Product"
4. Llenar formulario con:
   - Nombre del producto
   - Descripción
   - Precio
   - URL de imagen
   - Categoría
   - Datos del artesano

#### **Crear Posts de Blog:**
1. En el admin, ir a "Blog posts"
2. "Add Blog post"
3. El contenido admite HTML:
```html
<p>Texto normal</p>
<h3>Subtítulos</h3>
<strong>Texto en negrita</strong>
<img src="URL_IMAGEN" alt="Descripción">
```

## 🔐 **Acceso de Administrador**

```
URL: /admin/
Usuario: admin
Contraseña: [Configurada en el sistema]
```

## 🌐 **URLs Principales**

```
/ - Página principal
/shop/ - Tienda
/product/<id>/ - Producto individual
/blog/ - Blog
/blog/<slug>/ - Post individual
/contact/ - Contacto
/login/ - Iniciar sesión
/register/ - Registro
/cart/ - Carrito
/profile/ - Perfil de usuario
/admin/ - Panel de administración
```

## 🚀 **Cómo Ejecutar el Proyecto**

1. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

2. **Migrar base de datos:**
```bash
python manage.py migrate
```

3. **Crear datos de prueba:**
```bash
python manage.py create_sample_data
```

4. **Ejecutar servidor:**
```bash
python manage.py runserver 0.0.0.0:3000
```

## 📱 **Características Técnicas**

### **Responsive Design**
- Móviles: Menú hamburguesa, cards apiladas
- Tablets: Layout adaptativo
- Desktop: Experiencia completa

### **SEO Optimizado**
- Meta tags configurados
- URLs amigables
- Estructura semántica HTML5

### **Seguridad**
- CSRF protection
- Autenticación segura
- Validación de formularios

## 🔄 **Próximas Mejoras Sugeridas**

1. **Pasarela de Pagos** - Integrar Stripe/PayPal
2. **Sistema de Reviews** - Reseñas de productos
3. **Wishlist** - Lista de deseos
4. **Notificaciones** - Email y en tiempo real
5. **Múltiples Imágenes** - Galería por producto
6. **Filtros Avanzados** - Por precio, color, etc.
7. **Panel Artesano** - Para que suban sus productos

## 🤝 **Soporte y Mantenimiento**

Para modificaciones o mejoras:
1. Hacer backup de la base de datos
2. Probar cambios en entorno de desarrollo
3. Documentar modificaciones
4. Actualizar esta documentación

---

**¡Tu plataforma Raíces Vivas está lista para conectar el arte Wayuu con el mundo! 🌟**
