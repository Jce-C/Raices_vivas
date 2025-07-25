import os
import secrets
from datetime import datetime
from flask import current_app

def generate_order_number():
    """Generate a unique order number"""
    timestamp = datetime.now().strftime('%Y%m%d')
    random_part = secrets.token_hex(4).upper()
    return f"RV{timestamp}{random_part}"

def format_currency(amount):
    """Format currency for Colombian Pesos"""
    return f"Rs. {amount:,.2f}"

def get_sample_products():
    """Return sample product data for initial database population"""
    return [
        {
            'name': 'Mochila Wayuu Tradicional',
            'description': 'Hermosa mochila tejida a mano por artesanas Wayuu. Cada mochila cuenta una historia única a través de sus patrones tradicionales.',
            'price': 250000.00,
            'image_url': 'https://pixabay.com/get/gcc4fbe936f59a9e334796d0ab62e78ac445c59e752e2ae0310d15aac5bab6da78f5139d97f4fe56f7c5e6c75a986e91b45fef0834ce0c58409093a908c936fa0_1280.jpg',
            'category': 'Mochilas',
            'artisan_name': 'María Ipuana',
            'materials': 'Algodón, hilos de colores',
            'colors': ['Rojo', 'Azul', 'Verde']
        },
        {
            'name': 'Bolso Wayuu Pequeño',
            'description': 'Bolso artesanal perfecto para el día a día. Tejido con técnicas ancestrales transmitidas de generación en generación.',
            'price': 180000.00,
            'image_url': 'https://pixabay.com/get/g4b54fd0305b34f09a9c9e4907edc1ad37f8c1830b1d3f56e5b2302e91de46535966a6cbe1109e033b5917a7c3b27e66ebeac016eccabcf1201ff846c04c3c106_1280.jpg',
            'category': 'Bolsos',
            'artisan_name': 'Carmen Uriana',
            'materials': 'Algodón, fibras naturales',
            'colors': ['Naranja', 'Rosa', 'Amarillo']
        },
        {
            'name': 'Hamaca Wayuu Doble',
            'description': 'Hamaca tradicional tejida con los mejores materiales. Ideal para descansar y conectar con la tradición.',
            'price': 450000.00,
            'image_url': 'https://pixabay.com/get/g119f86981c3456e4d1ffbbd0e84331a504c39e5f80fac61041debbd790aba7bf8fa118f8e323f238cdc74f33aaadd2d31993823d554ad1cb7a5999469e558a53_1280.jpg',
            'category': 'Hamacas',
            'artisan_name': 'José Pushaina',
            'materials': 'Algodón resistente, cuerdas naturales',
            'colors': ['Natural', 'Azul', 'Verde']
        }
    ]

def get_sample_blog_posts():
    """Return sample blog posts for initial population"""
    return [
        {
            'title': 'La tradición del tejido Wayuu',
            'slug': 'tradicion-tejido-wayuu',
            'content': 'El tejido Wayuu es más que una artesanía, es una expresión cultural que conecta a las mujeres con sus ancestros...',
            'excerpt': 'Descubre la rica tradición del tejido Wayuu y su significado cultural.',
            'featured_image': 'https://pixabay.com/get/g4cb61acb2ecb4d9b926cbd249dfc1cd5df755e543ccf124bdf13f138de12c6f6b2ae4a84352b329aa134ec01344cbed0891ba00c065f5fe20faea775e124af09_1280.jpg',
            'author': 'Equipo Raíces Vivas'
        },
        {
            'title': 'Los colores sagrados de La Guajira',
            'slug': 'colores-sagrados-guajira',
            'content': 'Cada color en las artesanías Wayuu tiene un significado profundo conectado con la naturaleza y la espiritualidad...',
            'excerpt': 'Explora el significado de los colores en la cultura Wayuu.',
            'featured_image': 'https://pixabay.com/get/gd71f9f98ba52cbb79522c47f662a4142cd96cc81246d330f754084d4a08f61208fef9df246cc18af27810cf573047dbce3dee81a092bc6f23e5ab31617c4f6f9_1280.jpg',
            'author': 'Equipo Raíces Vivas'
        }
    ]
