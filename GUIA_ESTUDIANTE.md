# 📚 GUÍA PARA ESTUDIANTES - Raíces Vivas

## 🎯 ¿Qué es este proyecto?

**Raíces Vivas** es una tienda online para vender artesanías Wayuu de La Guajira, Colombia. Este proyecto está hecho para que estudiantes puedan aprender sobre desarrollo web.

## 🛠️ Tecnologías que usamos (Nivel Intermedio)

### Backend (Servidor)
- **Flask**: Framework de Python para crear sitios web
- **SQLAlchemy**: Para manejar la base de datos
- **PostgreSQL**: Base de datos donde guardamos la información

### Frontend (Lo que ve el usuario)
- **HTML**: Estructura de las páginas
- **CSS**: Estilos y diseño
- **Bootstrap**: Framework para hacer el diseño responsive
- **JavaScript**: Interactividad básica

## 📁 Estructura del Proyecto (Simplificada)

```
raices-vivas/
├── app.py              # Configuración principal de la app
├── main.py             # Archivo para ejecutar la app
├── routes.py           # Rutas y funciones de las páginas
├── models.py           # Estructura de la base de datos
├── forms.py            # Formularios del sitio
├── templates/          # Plantillas HTML
│   ├── base.html       # Plantilla base
│   ├── index.html      # Página de inicio
│   ├── shop.html       # Tienda
│   └── ...
├── static/             # Archivos estáticos
│   ├── css/           # Estilos CSS
│   ├── js/            # JavaScript
│   └── images/        # Imágenes
└── GUIA_ESTUDIANTE.md  # Esta guía
```

## 🔄 ¿Cómo funciona? (Sin APIs complicadas)

Este proyecto NO usa APIs externas complicadas. Todo es local y simple:

### 1. Base de Datos Local
- Los productos se guardan en PostgreSQL
- Los usuarios y pedidos también
- No hay APIs de pago reales (es para aprender)

### 2. Imágenes
- Usamos URLs de Pixabay (gratuitas)
- También puedes subir imágenes a `static/images/`

### 3. Sin APIs de pago
- El "checkout" solo simula el proceso
- No hay Stripe, PayPal, etc.

## ✏️ Cómo Modificar el Contenido

### 🖼️ Cambiar Imágenes

**Para el logo:**
1. Guarda tu imagen en `static/images/`
2. Ve a `templates/home_nav.html`
3. Busca esta línea:
```html
<img src="{{ url_for('static', filename='images/logo_raices_vivas.png') }}"
```
4. Cambia `logo_raices_vivas.png` por tu archivo

**Para fotos de productos:**
1. Ve a `routes.py`
2. Busca la función `create_sample_data()`
3. Cambia las URLs de las imágenes:
```python
image_url="https://tu-nueva-imagen.jpg"
```

### 📝 Cambiar Textos

**Página de inicio:**
1. Abre `templates/index.html`
2. Busca los textos entre `<h1>`, `<p>`, etc.
3. Modifica directamente:
```html
<h1>TU NUEVO TÍTULO</h1>
<p>Tu nueva descripción aquí</p>
```

**Productos:**
1. Ve a `routes.py`
2. En `create_sample_data()` puedes cambiar:
```python
Product(
    name="Nuevo Producto",
    description="Nueva descripción",
    price=50000,
    # ...
)
```

### 🎨 Cambiar Colores y Estilos

**Colores principales:**
1. Abre `static/css/style.css`
2. Busca las variables CSS:
```css
:root {
    --primary-color: #c58b44;    /* Color principal */
    --secondary-color: #8b4513;  /* Color secundario */
}
```

**Cambiar el fondo de una sección:**
1. En `templates/index.html`
2. Busca la sección que quieres cambiar
3. Modifica la URL de la imagen de fondo:
```css
background: url('tu-nueva-imagen.jpg');
```

### 🏪 Agregar Nuevos Productos

1. Ve a `routes.py`
2. En la función `create_sample_data()`
3. Agrega un nuevo producto:
```python
new_product = Product(
    name="Mi Producto",
    description="Descripción del producto",
    price=75000,
    image_url="https://mi-imagen.jpg",
    category_id=1,  # 1=Mochilas, 2=Hamacas, etc.
    artisan_name="Nombre del Artesano",
    stock_quantity=10
)
db.session.add(new_product)
```

## 🚀 Cómo Ejecutar el Proyecto

1. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

2. **Ejecutar la app:**
```bash
python main.py
```

3. **Ver el sitio:**
- Abre tu navegador
- Ve a `http://localhost:5000`

## 🐛 Problemas Comunes

### Error 500
- Revisa que la base de datos esté funcionando
- Verifica que no haya errores de sintaxis en Python

### Imágenes no cargan
- Verifica que la ruta sea correcta
- Asegúrate de que el archivo exista en `static/images/`

### Estilos no se aplican
- Verifica la ruta en `base.html`
- Revisa que no haya errores en el CSS

## 📚 Para Seguir Aprendiendo

### Temas que puedes explorar:
1. **Más Flask**: Aprende sobre blueprints, sessions
2. **Base de datos**: Migraciones, relaciones más complejas
3. **Frontend**: Vue.js o React para interfaces más dinámicas
4. **Despliegue**: Heroku, DigitalOcean

### Recursos recomendados:
- Flask Documentation: https://flask.palletsprojects.com/
- Bootstrap Documentation: https://getbootstrap.com/
- SQLAlchemy Tutorial: https://docs.sqlalchemy.org/

## 💡 Tips para Estudiantes

1. **Empieza pequeño**: Modifica textos antes que funcionalidades
2. **Usa comentarios**: Agrega comentarios a tu código
3. **Prueba frecuentemente**: Ejecuta la app después de cada cambio
4. **Lee errores**: Los mensajes de error te ayudan a encontrar problemas
5. **Experimenta**: No tengas miedo de romper algo, siempre puedes revertir

¡Diviértete aprendiendo! 🎉