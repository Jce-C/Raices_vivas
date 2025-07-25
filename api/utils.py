"""
Utility functions for Wayuu Artesania API
Converted from Flask utils to Django equivalents
"""
import uuid
import random
import string
from datetime import datetime
from decimal import Decimal


def generate_order_number():
    """Generate a unique order number"""
    timestamp = datetime.now().strftime('%Y%m%d')
    random_suffix = ''.join(random.choices(string.digits, k=4))
    return f"WA{timestamp}{random_suffix}"


def format_currency(amount):
    """Format currency amount for display"""
    return f"${amount:,.2f}"


def get_sample_products():
    """Get sample product data for initial setup"""
    return [
        {
            'name': 'Mochila Wayuu Tradicional',
            'description': 'Hermosa mochila tejida a mano por artesanas Wayuu con patrones tradicionales.',
            'price': Decimal('85000.00'),
            'image_url': 'https://example.com/images/mochila1.jpg',
            'category': 'Mochilas',
            'artisan_name': 'María Pushaina',
            'materials': 'Algodón, fibras naturales',
            'colors': ['Rojo', 'Azul', 'Verde', 'Amarillo'],
            'dimensions': '25cm x 30cm',
            'weight': '200g'
        },
        {
            'name': 'Bolso Wayuu Pequeño',
            'description': 'Elegante bolso pequeño perfecto para ocasiones especiales.',
            'price': Decimal('45000.00'),
            'image_url': 'https://example.com/images/bolso1.jpg',
            'category': 'Bolsos',
            'artisan_name': 'Ana Uriana',
            'materials': 'Algodón, hilo de colores',
            'colors': ['Rosa', 'Morado', 'Blanco'],
            'dimensions': '20cm x 15cm',
            'weight': '150g'
        },
        {
            'name': 'Hamaca Wayuu Familiar',
            'description': 'Hamaca grande tejida a mano, perfecta para toda la familia.',
            'price': Decimal('120000.00'),
            'image_url': 'https://example.com/images/hamaca1.jpg',
            'category': 'Hamacas',
            'artisan_name': 'Carmen Epiayuu',
            'materials': 'Algodón resistente',
            'colors': ['Natural', 'Multicolor'],
            'dimensions': '3m x 1.5m',
            'weight': '1.2kg'
        },
        {
            'name': 'Pulsera Wayuu Artesanal',
            'description': 'Pulsera tejida con patrones geométricos tradicionales.',
            'price': Decimal('15000.00'),
            'image_url': 'https://example.com/images/pulsera1.jpg',
            'category': 'Accesorios',
            'artisan_name': 'Luz Ipuana',
            'materials': 'Hilo de algodón',
            'colors': ['Azul', 'Rojo', 'Verde', 'Amarillo', 'Negro'],
            'dimensions': 'Ajustable',
            'weight': '10g'
        },
        {
            'name': 'Mochila Wayuu Grande',
            'description': 'Mochila de gran tamaño con diseños únicos y colores vibrantes.',
            'price': Decimal('95000.00'),
            'image_url': 'https://example.com/images/mochila2.jpg',
            'category': 'Mochilas',
            'artisan_name': 'Rosa Gouriyu',
            'materials': 'Algodón, fibras naturales',
            'colors': ['Naranja', 'Verde', 'Azul', 'Rojo'],
            'dimensions': '30cm x 35cm',
            'weight': '250g'
        },
        {
            'name': 'Sombrero Wayuu',
            'description': 'Sombrero tradicional tejido a mano, ideal para protegerse del sol.',
            'price': Decimal('35000.00'),
            'image_url': 'https://example.com/images/sombrero1.jpg',
            'category': 'Accesorios',
            'artisan_name': 'Elena Arpushana',
            'materials': 'Fibra de palma',
            'colors': ['Natural', 'Café'],
            'dimensions': 'Talla única',
            'weight': '100g'
        }
    ]


def get_sample_blog_posts():
    """Get sample blog post data for initial setup"""
    return [
        {
            'title': 'La Historia de las Artesanías Wayuu',
            'slug': 'historia-artesanias-wayuu',
            'content': '''
            Las artesanías Wayuu son el resultado de siglos de tradición y cultura. 
            Cada pieza cuenta una historia, cada patrón tiene un significado especial 
            que se transmite de generación en generación.
            
            Los diseños geométricos no son solo decorativos, sino que representan 
            elementos de la naturaleza, animales, y aspectos importantes de la 
            cosmovisión Wayuu.
            ''',
            'excerpt': 'Descubre la rica historia detrás de las artesanías Wayuu y su significado cultural.',
            'featured_image': 'https://example.com/images/blog1.jpg',
            'author': 'Equipo Raíces Vivas',
            'is_published': True
        },
        {
            'title': 'El Arte del Tejido Wayuu',
            'slug': 'arte-tejido-wayuu',
            'content': '''
            El tejido Wayuu es una técnica ancestral que requiere paciencia, 
            habilidad y conocimiento profundo de los patrones tradicionales.
            
            Cada artesana aprende desde pequeña observando a su madre y abuela, 
            desarrollando su propio estilo mientras respeta las tradiciones.
            ''',
            'excerpt': 'Conoce la técnica ancestral del tejido Wayuu y su importancia cultural.',
            'featured_image': 'https://example.com/images/blog2.jpg',
            'author': 'Equipo Raíces Vivas',
            'is_published': True
        }
    ]
