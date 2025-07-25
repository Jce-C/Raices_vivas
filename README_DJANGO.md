# Wayuu Artesania - Django REST Framework

Este proyecto ha sido migrado de Flask a Django REST Framework para proporcionar una API moderna y escalable para la plataforma de artesanías Wayuu.

## Características

- **API REST completa** con Django REST Framework
- **Autenticación por tokens** para usuarios
- **Gestión de productos** con categorías, imágenes y stock
- **Carrito de compras** con persistencia por usuario
- **Sistema de órdenes** completo con seguimiento
- **Blog** para contenido cultural
- **Formulario de contacto**
- **Panel de administración** de Django

## Instalación

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2. Configurar variables de entorno

Copia el archivo `.env.example` a `.env` y configura las variables:

```bash
cp .env.example .env
```

Edita el archivo `.env` con tu configuración:

```
SECRET_KEY=tu-clave-secreta-aqui
DEBUG=True
DATABASE_URL=postgresql://user:password@localhost/raices_vivas
```

### 3. Ejecutar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Crear datos de ejemplo

```bash
python manage.py create_sample_data
```

### 5. Ejecutar el servidor

```bash
python manage.py runserver
```

El servidor estará disponible en `http://localhost:8000`

## Endpoints de la API

### Autenticación
- `POST /api/auth/register/` - Registro de usuario
- `POST /api/auth/login/` - Inicio de sesión
- `POST /api/auth/logout/` - Cerrar sesión
- `GET /api/auth/profile/` - Perfil del usuario

### Productos
- `GET /api/products/` - Listar productos
- `GET /api/products/{id}/` - Detalle de producto
- `GET /api/products/featured/` - Productos destacados
- `POST /api/products/` - Crear producto (admin)

### Categorías
- `GET /api/categories/` - Listar categorías
- `GET /api/categories/{id}/` - Detalle de categoría

### Carrito
- `GET /api/cart/` - Ver carrito del usuario
- `POST /api/cart/` - Agregar al carrito
- `PUT /api/cart/{id}/` - Actualizar cantidad
- `DELETE /api/cart/{id}/` - Eliminar del carrito
- `DELETE /api/cart/clear/` - Vaciar carrito

### Órdenes
- `GET /api/orders/` - Listar órdenes del usuario
- `POST /api/orders/` - Crear nueva orden
- `GET /api/orders/{id}/` - Detalle de orden

### Blog
- `GET /api/blog/` - Listar posts del blog
- `GET /api/blog/{slug}/` - Detalle de post

### Contacto
- `POST /api/contact/` - Enviar mensaje de contacto

## Autenticación

La API utiliza autenticación por tokens. Después del login, incluye el token en las cabeceras:

```
Authorization: Token tu_token_aqui
```

## Panel de Administración

Accede al panel de administración en `http://localhost:8000/admin/`

Usuario por defecto:
- Username: `admin`
- Password: `admin123`

## Filtros y Búsqueda

### Productos
- Filtrar por categoría: `/api/products/?category=1`
- Buscar por nombre: `/api/products/?search=mochila`
- Ordenar por precio: `/api/products/?ordering=price`
- Productos destacados: `/api/products/?is_featured=true`

### Blog
- Buscar posts: `/api/blog/?search=wayuu`
- Ordenar por fecha: `/api/blog/?ordering=-created_at`

## Diferencias con la versión Flask

1. **Estructura de URLs**: Ahora todas las rutas están bajo `/api/`
2. **Autenticación**: Usa tokens en lugar de sesiones
3. **Respuestas JSON**: Todas las respuestas son en formato JSON
4. **Paginación**: Automática en todas las listas
5. **Filtros**: Más opciones de filtrado y búsqueda
6. **Admin**: Panel de administración integrado de Django

## Desarrollo

Para desarrollo, puedes usar SQLite en lugar de PostgreSQL:

```
DATABASE_URL=sqlite:///db.sqlite3
```

## Estructura del Proyecto

```
wayuu_artesania/
├── manage.py
├── requirements.txt
├── wayuu_artesania/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── api/
    ├── models.py
    ├── serializers.py
    ├── views.py
    ├── urls.py
    ├── admin.py
    ├── utils.py
    └── management/
        └── commands/
            └── create_sample_data.py
```

## Próximos Pasos

1. Configurar CORS para frontend
2. Implementar paginación personalizada
3. Agregar validaciones adicionales
4. Configurar envío de emails
5. Implementar sistema de pagos
6. Agregar tests unitarios
