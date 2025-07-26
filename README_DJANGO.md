
# Raíces Vivas - E-commerce de Artesanías Wayuu

## Descripción del Proyecto

Raíces Vivas es una plataforma e-commerce desarrollada en Django que conecta artesanas Wayuu con compradores interesados en auténticas artesanías colombianas. La plataforma permite a las artesanas mostrar y vender sus productos mientras preserva y promueve la cultura Wayuu.

## Estado Actual del Proyecto

### ✅ Funcionalidades Implementadas

1. **Homepage Completa**
   - Navegación flotante especial para la página principal
   - Secciones de héroe, productos destacados, artesanas
   - Galería de fotos con mosaico animado
   - Blog posts destacados

2. **Sistema de Productos**
   - Catálogo completo de productos
   - Páginas de detalle de productos
   - Sistema de filtros y búsqueda
   - Gestión de inventario

3. **Blog Integrado**
   - Sistema de publicaciones
   - Páginas de detalle de blog
   - Categorización de contenido
   - Renderizado de HTML seguro

4. **Carrito de Compras**
   - Añadir/quitar productos
   - Actualización de cantidades
   - Cálculo automático de totales

5. **Sistema de Usuarios**
   - Registro e inicio de sesión
   - Perfiles de usuario
   - Gestión de pedidos

6. **Panel Administrativo**
   - Gestión de productos
   - Gestión de blog posts
   - Gestión de usuarios y pedidos

### 🚧 En Desarrollo

1. **Sistema de Pagos**
   - Integración con pasarelas de pago
   - Procesamiento de transacciones

2. **Gestión de Pedidos Avanzada**
   - Estados de pedidos
   - Notificaciones por email

### 🎨 Características de Diseño

- **Paleta de Colores Wayuu**: Inspirada en la cultura tradicional
- **Diseño Responsivo**: Funciona en móviles, tablets y desktop
- **Animaciones Suaves**: Efectos de scroll y hover
- **Navegación Intuitiva**: Diseño centrado en el usuario

## Tecnologías Utilizadas

- **Backend**: Django 4.2.7
- **Base de Datos**: SQLite (desarrollo)
- **Frontend**: HTML5, CSS3, JavaScript ES6+
- **Framework CSS**: Bootstrap 5
- **Iconos**: Font Awesome
- **Fuentes**: Google Fonts (Poppins, Playfair Display)

## Estructura del Proyecto

```
wayuu_artesania/
├── api/                    # App principal con modelos y vistas
│   ├── models.py          # Modelos de datos
│   ├── views.py           # Vistas de API
│   ├── template_views.py  # Vistas de templates
│   └── urls.py            # URLs de la API
├── templates/             # Templates HTML
│   ├── index.html         # Página principal
│   ├── shop.html          # Tienda
│   ├── product.html       # Detalle de producto
│   ├── blog.html          # Blog
│   └── ...
├── static/                # Archivos estáticos
│   ├── css/style.css      # Estilos principales
│   ├── js/main.js         # JavaScript principal
│   └── images/            # Imágenes del sitio
└── wayuu_artesania/       # Configuración Django
    └── settings.py        # Configuración del proyecto
```

## Instalación y Configuración

### Requisitos
- Python 3.8+
- Django 4.2.7
- SQLite

### Pasos de Instalación

1. **Clonar el repositorio** (en Replit ya está configurado)

2. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar migraciones**:
   ```bash
   python manage.py migrate
   ```

4. **Crear datos de muestra**:
   ```bash
   python manage.py create_sample_data
   ```

5. **Crear superusuario**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Ejecutar servidor**:
   ```bash
   python manage.py runserver 0.0.0.0:3000
   ```

## Personalización del Contenido

### Cambiar Textos de la Página Principal

Los textos principales se encuentran en `templates/index.html`:

#### Sección Hero:
- **Título**: Líneas 51-54
- **Descripción**: Líneas 55-58

#### Sección "Un Tesoro de Saberes":
- **Título**: Líneas 95-98
- **Contenido**: Líneas 99-108

#### Sección Productos Destacados:
- **Título**: Líneas 125-128
- **Descripción**: Líneas 129-133

#### Sección Artesanas:
- **Título**: Líneas 166-169
- **Descripción**: Líneas 170-174

### Cambiar Imágenes

#### Imágenes del Hero y Fondo:
```html
<!-- Línea 24: Imagen de fondo del hero -->
background: url('TU_IMAGEN_AQUI');

<!-- Línea 67: Imagen del hero -->
<img src="TU_IMAGEN_AQUI" alt="Artesanías Wayuu">
```

#### Imágenes del Mosaico:
En las líneas 320-380, puedes cambiar las URLs de las imágenes del mosaico.

#### Imágenes de Artesanas:
En las líneas 180-280, puedes personalizar las fotos y descripciones de las artesanas.

### Variables CSS Personalizables

En `static/css/style.css` (líneas 7-21):
```css
:root {
    --primary-color: #C58B44;      /* Color principal */
    --secondary-color: #D49C55;    /* Color secundario */
    --accent-color: #B8860B;       /* Color de acento */
    --wayuu-red: #CD5C5C;          /* Rojo Wayuu */
    --wayuu-blue: #4682B4;         /* Azul Wayuu */
    --wayuu-green: #228B22;        /* Verde Wayuu */
}
```

## Configuración de Base de Datos

El proyecto usa SQLite por defecto. Para cambiar a PostgreSQL o MySQL, modificar `settings.py`.

## Despliegue en Replit

1. El proyecto está configurado para ejecutarse en Replit
2. Puerto configurado: 3000
3. Comando de ejecución: `python manage.py runserver 0.0.0.0:3000`

## Contribución

Para contribuir al proyecto:
1. Fork el repositorio
2. Crear una rama para tu feature
3. Hacer commit de los cambios
4. Enviar pull request

## Soporte

Para soporte técnico o preguntas sobre el proyecto, contacta al equipo de desarrollo.

---

**Raíces Vivas** - Preservando la cultura Wayuu a través del comercio digital.
