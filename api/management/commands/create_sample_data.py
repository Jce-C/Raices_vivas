
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from api.models import Category, Product, BlogPost
from decimal import Decimal

User = get_user_model()


class Command(BaseCommand):
    help = 'Create sample data for the Wayuu Artesania store'

    def handle(self, *args, **options):
        self.stdout.write('Creando datos de ejemplo...')
        
        # Create admin user
        if not User.objects.filter(username='admin').exists():
            admin_user = User.objects.create_superuser(
                username='admin',
                email='admin@raicesvivas.com',
                password='admin123',
                first_name='Administrador',
                last_name='Raíces Vivas',
                is_admin=True
            )
            self.stdout.write(f'✓ Usuario administrador creado: admin/admin123')

        # Create categories
        categories_data = [
            {
                'name': 'Bolsos y Mochilas',
                'description': 'Hermosos bolsos tejidos a mano con técnicas ancestrales Wayuu',
                'image_url': 'https://pixabay.com/get/g85f5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a_1280.jpg'
            },
            {
                'name': 'Sombreros',
                'description': 'Sombreros tradicionales Wayuu para protegerse del sol guajiro',
                'image_url': 'https://pixabay.com/get/ga9784cd8b4eddb7bfd8bfc3a3343dfabc5d3aeb33ce3cf718235d68f25c4511f9_1280.jpg'
            },
            {
                'name': 'Chinchorros',
                'description': 'Hamacas tradicionales, símbolo de la cultura Wayuu',
                'image_url': 'https://pixabay.com/get/gf8a2b6b8c7f5b7b54f5f9d5e5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a_1280.jpg'
            },
            {
                'name': 'Accesorios',
                'description': 'Pulseras, collares y otros accesorios tradicionales',
                'image_url': 'https://pixabay.com/get/g85f5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a_1280.jpg'
            }
        ]

        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults=cat_data
            )
            if created:
                self.stdout.write(f'✓ Categoría creada: {category.name}')

        # Get categories
        bolsos_cat = Category.objects.get(name='Bolsos y Mochilas')
        sombreros_cat = Category.objects.get(name='Sombreros')
        chinchorros_cat = Category.objects.get(name='Chinchorros')
        accesorios_cat = Category.objects.get(name='Accesorios')

        # Create products
        products_data = [
            # Bolsos y Mochilas
            {
                'name': 'Mochila Wayuu Tradicional',
                'description': 'Hermosa mochila tejida a mano con patrones geométricos tradicionales. Cada diseño cuenta una historia ancestral transmitida de generación en generación.',
                'price': Decimal('120000'),
                'image_url': 'https://pixabay.com/get/g85f5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a_1280.jpg',
                'category': bolsos_cat,
                'artisan_name': 'María Pushaina',
                'materials': 'Algodón, hilo acrílico',
                'dimensions': '25cm x 30cm',
                'colors': ['Rojo', 'Azul', 'Verde', 'Amarillo'],
                'stock_quantity': 5,
                'is_featured': True
            },
            {
                'name': 'Bolso Wayuu Multicolor',
                'description': 'Bolso vibrante con colores que representan la naturaleza de La Guajira: el mar, el desierto y la vegetación.',
                'price': Decimal('95000'),
                'image_url': 'https://pixabay.com/get/ga9784cd8b4eddb7bfd8bfc3a3343dfabc5d3aeb33ce3cf718235d68f25c4511f9_1280.jpg',
                'category': bolsos_cat,
                'artisan_name': 'Carmen Uriana',
                'materials': 'Algodón, hilo acrílico',
                'dimensions': '20cm x 25cm',
                'colors': ['Multicolor'],
                'stock_quantity': 8,
                'is_featured': True
            },
            
            # Sombreros
            {
                'name': 'Sombrero Vueltiao Wayuu',
                'description': 'Sombrero tradicional tejido en caña flecha, perfecto para protegerse del intenso sol guajiro.',
                'price': Decimal('75000'),
                'image_url': 'https://pixabay.com/get/gf8a2b6b8c7f5b7b54f5f9d5e5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a_1280.jpg',
                'category': sombreros_cat,
                'artisan_name': 'José Ipuana',
                'materials': 'Caña flecha',
                'dimensions': 'Talla única',
                'colors': ['Natural'],
                'stock_quantity': 12,
                'is_featured': True
            },
            
            # Chinchorros
            {
                'name': 'Chinchorro Wayuu Grande',
                'description': 'Hamaca tradicional Wayuu, símbolo de hospitalidad y descanso. Tejida con técnicas milenarias.',
                'price': Decimal('350000'),
                'image_url': 'https://pixabay.com/get/g85f5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a_1280.jpg',
                'category': chinchorros_cat,
                'artisan_name': 'Ana Pushaina',
                'materials': 'Algodón',
                'dimensions': '3m x 1.5m',
                'colors': ['Rojo y Blanco', 'Azul y Blanco'],
                'stock_quantity': 3,
                'is_featured': True
            },
            
            # Accesorios
            {
                'name': 'Pulsera Wayuu Ancestral',
                'description': 'Pulsera tejida con patrones que representan elementos de la cosmovisión Wayuu.',
                'price': Decimal('25000'),
                'image_url': 'https://pixabay.com/get/ga9784cd8b4eddb7bfd8bfc3a3343dfabc5d3aeb33ce3cf718235d68f25c4511f9_1280.jpg',
                'category': accesorios_cat,
                'artisan_name': 'Rosa Epiayuu',
                'materials': 'Hilo de algodón',
                'dimensions': 'Ajustable',
                'colors': ['Rojo', 'Azul', 'Verde', 'Amarillo', 'Morado'],
                'stock_quantity': 20,
                'is_featured': False
            },
            {
                'name': 'Collar Wayuu Tradicional',
                'description': 'Collar con cuentas y diseños tradicionales, usado en ceremonias especiales.',
                'price': Decimal('45000'),
                'image_url': 'https://pixabay.com/get/gf8a2b6b8c7f5b7b54f5f9d5e5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a_1280.jpg',
                'category': accesorios_cat,
                'artisan_name': 'Elena Uriana',
                'materials': 'Cuentas, hilo',
                'dimensions': '40cm',
                'colors': ['Multicolor'],
                'stock_quantity': 15,
                'is_featured': False
            }
        ]

        for product_data in products_data:
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults=product_data
            )
            if created:
                self.stdout.write(f'✓ Producto creado: {product.name}')

        # Create blog posts
        blog_posts_data = [
            {
                'title': 'La Historia del Pueblo Wayuu',
                'slug': 'historia-pueblo-wayuu',
                'content': '''Los Wayuu son el pueblo indígena más numeroso de Venezuela y Colombia. Habitan principalmente en la península de La Guajira, un territorio semiárido donde han desarrollado una cultura única adaptada al desierto.

Su sociedad se organiza en clanes matrilineales, donde las mujeres juegan un papel fundamental en la transmisión de la cultura y las tradiciones. Los Wayuu son conocidos por su habilidad en el tejido, especialmente en la creación de mochilas, chinchorros y otros artículos textiles.

La tradición del tejido no es solo una actividad económica, sino una forma de expresión cultural que conecta a las mujeres con sus ancestros y con los espíritus de la naturaleza.''',
                'excerpt': 'Conoce la rica historia y tradiciones del pueblo Wayuu, guardianes de una cultura milenaria.',
                'featured_image': 'https://pixabay.com/get/ga9784cd8b4eddb7bfd8bfc3a3343dfabc5d3aeb33ce3cf718235d68f25c4511f9_1280.jpg',
                'author': 'Equipo Raíces Vivas',
                'is_published': True
            },
            {
                'title': 'El Arte del Tejido Wayuu',
                'slug': 'arte-tejido-wayuu',
                'content': '''El tejido Wayuu es mucho más que una técnica artesanal; es un lenguaje que comunica historias, tradiciones y la cosmovisión de este pueblo ancestral.

Cada patrón tiene un significado específico: algunos representan animales del desierto, otros simbolizan elementos de la naturaleza como el viento, la lluvia o las estrellas. Los colores también tienen importancia simbólica y se eligen cuidadosamente para transmitir mensajes específicos.

El proceso de tejido comienza desde la niñez, cuando las madres enseñan a sus hijas los secretos de esta antigua tradición. Se dice que una mujer Wayuu que no sabe tejer no está preparada para el matrimonio.''',
                'excerpt': 'Descubre los secretos y significados detrás del arte ancestral del tejido Wayuu.',
                'featured_image': 'https://pixabay.com/get/gf8a2b6b8c7f5b7b54f5f9d5e5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a5c5a_1280.jpg',
                'author': 'María Fernanda López',
                'is_published': True
            }
        ]

        for post_data in blog_posts_data:
            blog_post, created = BlogPost.objects.get_or_create(
                slug=post_data['slug'],
                defaults=post_data
            )
            if created:
                self.stdout.write(f'✓ Post del blog creado: {blog_post.title}')

        self.stdout.write(
            self.style.SUCCESS('✅ Datos de ejemplo creados exitosamente!')
        )
        self.stdout.write('👤 Usuario admin: admin / admin123')
        self.stdout.write('🌐 Panel admin: /admin/')
        self.stdout.write('📊 API endpoints: /api/')
