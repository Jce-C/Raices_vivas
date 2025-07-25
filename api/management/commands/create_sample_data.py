from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from api.models import Category, Product, BlogPost
from decimal import Decimal

User = get_user_model()


class Command(BaseCommand):
    help = 'Create sample data for the Wayuu Artesania project'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')

        # Create superuser if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@raicesvivas.com',
                password='admin123',
                first_name='Admin',
                last_name='User'
            )
            self.stdout.write('Superuser created: admin/admin123')

        # Create categories
        categories_data = [
            {
                'name': 'Mochilas Wayuu',
                'description': 'Mochilas tradicionales tejidas a mano por artesanas Wayuu',
                'image_url': 'https://picsum.photos/400/300?random=1'
            },
            {
                'name': 'Sombreros Wayuu',
                'description': 'Sombreros tradicionales hechos con técnicas ancestrales',
                'image_url': 'https://picsum.photos/400/300?random=2'
            },
            {
                'name': 'Hamacas',
                'description': 'Hamacas coloridas para el descanso',
                'image_url': 'https://picsum.photos/400/300?random=3'
            },
            {
                'name': 'Joyas Wayuu',
                'description': 'Collares, pulseras y aretes tradicionales',
                'image_url': 'https://picsum.photos/400/300?random=4'
            }
        ]

        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults=cat_data
            )
            if created:
                self.stdout.write(f'Created category: {category.name}')

        # Create products
        products_data = [
            {
                'name': 'Mochila Wayuu Tradicional',
                'description': 'Hermosa mochila tejida a mano por artesanas Wayuu con patrones tradicionales.',
                'price': Decimal('180000'),
                'image_url': 'https://picsum.photos/400/300?random=10',
                'category': 'Mochilas Wayuu',
                'artisan_name': 'María Uriana',
                'materials': 'Algodón, Hilo acrílico',
                'colors': ['Rojo', 'Azul', 'Verde', 'Amarillo'],
                'is_featured': True,
                'stock_quantity': 10
            },
            {
                'name': 'Sombrero Vueltiao Wayuu',
                'description': 'Sombrero tradicional tejido con técnicas ancestrales.',
                'price': Decimal('120000'),
                'image_url': 'https://picsum.photos/400/300?random=11',
                'category': 'Sombreros Wayuu',
                'artisan_name': 'Carmen Pushaina',
                'materials': 'Caña flecha',
                'colors': ['Natural', 'Negro'],
                'is_featured': True,
                'stock_quantity': 15
            },
            {
                'name': 'Hamaca Wayuu Grande',
                'description': 'Hamaca amplia y cómoda con diseños coloridos.',
                'price': Decimal('350000'),
                'image_url': 'https://picsum.photos/400/300?random=12',
                'category': 'Hamacas',
                'artisan_name': 'Rosa Epieyu',
                'materials': 'Algodón',
                'colors': ['Multicolor', 'Azul y Blanco'],
                'is_featured': True,
                'stock_quantity': 5
            },
            {
                'name': 'Collar Wayuu Tradicional',
                'description': 'Collar hecho con chaquiras y semillas naturales.',
                'price': Decimal('85000'),
                'image_url': 'https://picsum.photos/400/300?random=13',
                'category': 'Joyas Wayuu',
                'artisan_name': 'Ana Epiayú',
                'materials': 'Chaquiras, Semillas',
                'colors': ['Multicolor', 'Turquesa'],
                'is_featured': False,
                'stock_quantity': 20
            },
            {
                'name': 'Mochila Wayuu Mini',
                'description': 'Mochila pequeña perfecta para ocasiones especiales.',
                'price': Decimal('95000'),
                'image_url': 'https://picsum.photos/400/300?random=14',
                'category': 'Mochilas Wayuu',
                'artisan_name': 'Luisa Sijona',
                'materials': 'Algodón',
                'colors': ['Rosa', 'Morado', 'Naranja'],
                'is_featured': False,
                'stock_quantity': 12
            }
        ]

        for prod_data in products_data:
            category = Category.objects.get(name=prod_data['category'])
            product, created = Product.objects.get_or_create(
                name=prod_data['name'],
                defaults={
                    **prod_data,
                    'category': category
                }
            )
            if created:
                self.stdout.write(f'Created product: {product.name}')

        # Create blog posts
        blog_posts_data = [
            {
                'title': 'La Tradición Wayuu',
                'slug': 'tradicion-wayuu',
                'content': 'La cultura Wayuu es rica en tradiciones que se han transmitido por generaciones...',
                'excerpt': 'Conoce la rica historia detrás de las artesanías Wayuu',
                'featured_image': 'https://picsum.photos/800/400?random=20',
                'author': 'Raíces Vivas',
                'is_published': True
            },
            {
                'title': 'Técnicas Ancestrales de Tejido',
                'slug': 'tecnicas-ancestrales',
                'content': 'Las técnicas de tejido Wayuu han sido perfeccionadas durante siglos...',
                'excerpt': 'Las técnicas de tejido se han transmitido por generaciones',
                'featured_image': 'https://picsum.photos/800/400?random=21',
                'author': 'Raíces Vivas',
                'is_published': True
            }
        ]

        for post_data in blog_posts_data:
            post, created = BlogPost.objects.get_or_create(
                slug=post_data['slug'],
                defaults=post_data
            )
            if created:
                self.stdout.write(f'Created blog post: {post.title}')

        self.stdout.write(
            self.style.SUCCESS('Successfully created sample data!')
        )