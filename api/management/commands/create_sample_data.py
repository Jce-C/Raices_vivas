from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from api.models import Category, Product, BlogPost
from decimal import Decimal

User = get_user_model()

class Command(BaseCommand):
    help = 'Create sample data for the application'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')

        # Create categories
        categories_data = [
            {'name': 'Mochilas', 'description': 'Mochilas tradicionales wayuu'},
            {'name': 'Hamacas', 'description': 'Hamacas tejidas a mano'},
            {'name': 'Sombreros', 'description': 'Sombreros artesanales'},
            {'name': 'Accesorios', 'description': 'Pulseras, collares y más'},
        ]

        categories = []
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            categories.append(category)
            if created:
                self.stdout.write(f'Created category: {category.name}')

        # Create products
        products_data = [
            {
                'name': 'Mochila Wayuu Tradicional',
                'description': 'Hermosa mochila wayuu tejida a mano con patrones tradicionales. Cada pieza es única y representa la rica cultura de la comunidad wayuu.',
                'price': Decimal('280000'),
                'category': categories[0],
                'artisan_name': 'María Pushaina',
                'materials': 'Algodón, hilo acrílico',
                'colors': ['Rojo', 'Azul', 'Verde'],
                'is_featured': True,
                'stock_quantity': 15,
                'image_url': 'https://picsum.photos/400/400?random=1',
            },
            {
                'name': 'Hamaca Wayuu Doble',
                'description': 'Cómoda hamaca wayuu para dos personas, tejida con técnicas ancestrales transmitidas de generación en generación.',
                'price': Decimal('450000'),
                'category': categories[1],
                'artisan_name': 'Carmen Uriana',
                'materials': 'Algodón 100%',
                'colors': ['Natural', 'Multicolor'],
                'is_featured': True,
                'stock_quantity': 8,
                'image_url': 'https://picsum.photos/400/400?random=2',
            },
            {
                'name': 'Sombrero Vueltiao',
                'description': 'Sombrero tradicional colombiano tejido en caña flecha, perfecto para protegerse del sol con estilo.',
                'price': Decimal('120000'),
                'category': categories[2],
                'artisan_name': 'José Montiel',
                'materials': 'Caña flecha',
                'colors': ['Natural'],
                'is_featured': False,
                'stock_quantity': 25,
                'image_url': 'https://picsum.photos/400/400?random=3',
            },
            {
                'name': 'Pulsera Wayuu Colorida',
                'description': 'Pulsera tejida con los colores vibrantes característicos de la cultura wayuu.',
                'price': Decimal('35000'),
                'category': categories[3],
                'artisan_name': 'Ana Ipuana',
                'materials': 'Hilo de algodón',
                'colors': ['Multicolor', 'Azul', 'Rosa'],
                'is_featured': False,
                'stock_quantity': 50,
                'image_url': 'https://picsum.photos/400/400?random=4',
            },
        ]

        for product_data in products_data:
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults=product_data
            )
            if created:
                self.stdout.write(f'Created product: {product.name}')

        # Create blog posts
        blog_posts_data = [
            {
                'title': 'La Tradición Wayuu',
                'slug': 'tradicion-wayuu',
                'content': 'La cultura wayuu es rica en tradiciones artesanales...',
                'excerpt': 'Conoce la rica historia detrás de las artesanías wayuu',
                'author': 'Admin',
                'is_published': True,
                'featured_image': 'https://picsum.photos/800/400?random=10',
            },
            {
                'title': 'Técnicas Ancestrales',
                'slug': 'tecnicas-ancestrales',
                'content': 'Las técnicas de tejido wayuu se han transmitido...',
                'excerpt': 'Las técnicas de tejido se han transmitido por generaciones',
                'author': 'Admin',
                'is_published': True,
                'featured_image': 'https://picsum.photos/800/400?random=11',
            },
        ]

        for post_data in blog_posts_data:
            blog_post, created = BlogPost.objects.get_or_create(
                slug=post_data['slug'],
                defaults=post_data
            )
            if created:
                self.stdout.write(f'Created blog post: {blog_post.title}')

        self.stdout.write(self.style.SUCCESS('Sample data created successfully!'))


class Command(BaseCommand):
    help = 'Create sample data for the application'

    def handle(self, *args, **options):
        # Create superuser if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123',
                first_name='Admin',
                last_name='User'
            )
            self.stdout.write(self.style.SUCCESS('Superuser created: admin/admin123'))

        # Create categories
        categories_data = [
            {
                'name': 'Mochilas',
                'description': 'Mochilas tradicionales Wayuu tejidas a mano',
                'image_url': 'https://example.com/mochilas.jpg'
            },
            {
                'name': 'Hamacas',
                'description': 'Hamacas cómodas y coloridas',
                'image_url': 'https://example.com/hamacas.jpg'
            },
            {
                'name': 'Sombreros',
                'description': 'Sombreros tejidos con fibras naturales',
                'image_url': 'https://example.com/sombreros.jpg'
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
                'name': 'Mochila Wayuu Colorida',
                'description': 'Hermosa mochila tejida a mano por artesanas Wayuu',
                'price': Decimal('45000'),
                'image_url': 'https://example.com/mochila1.jpg',
                'stock_quantity': 10,
                'category': Category.objects.get(name='Mochilas'),
                'artisan_name': 'María Uriana',
                'materials': 'Algodón, fibras naturales',
                'is_featured': True
            },
            {
                'name': 'Hamaca Wayuu Grande',
                'description': 'Hamaca espaciosa y cómoda para descansar',
                'price': Decimal('120000'),
                'image_url': 'https://example.com/hamaca1.jpg',
                'stock_quantity': 5,
                'category': Category.objects.get(name='Hamacas'),
                'artisan_name': 'Carmen Ipuana',
                'materials': 'Algodón',
                'is_featured': True
            }
        ]

        for prod_data in products_data:
            category = Category.objects.get(name=prod_data['category'])
            prod_data['category'] = category
            product, created = Product.objects.get_or_create(
                name=prod_data['name'],
                defaults=prod_data
            )
            if created:
                self.stdout.write(f'Created product: {product.name}')

        # Create blog posts
        blog_posts_data = [
            {
                'title': 'La tradición Wayuu',
                'slug': 'tradicion-wayuu',
                'content': 'La cultura Wayuu es rica en tradiciones...',
                'excerpt': 'Conoce más sobre la cultura Wayuu',
                'author': 'Equipo Raíces Vivas',
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

        self.stdout.write(self.style.SUCCESS('Sample data created successfully!'))