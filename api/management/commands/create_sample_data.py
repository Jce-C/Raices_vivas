
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from api.models import Category, Product, BlogPost
from decimal import Decimal
from django.utils.text import slugify

User = get_user_model()

class Command(BaseCommand):
    help = 'Create sample data for development'

    def handle(self, *args, **options):
        # Create superuser
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@raicesvivas.com',
                password='admin123',
                first_name='Administrador',
                last_name='Principal'
            )
            self.stdout.write(self.style.SUCCESS('Superuser created: admin/admin123'))

        # Create categories
        categories_data = [
            {
                'name': 'Mochilas',
                'description': 'Mochilas tradicionales Wayuu tejidas a mano con técnicas ancestrales',
                'image_url': 'https://cdn.pixabay.com/photo/2019/07/15/18/47/bag-4339942_1280.jpg'
            },
            {
                'name': 'Hamacas',
                'description': 'Hamacas cómodas y resistentes perfectas para el descanso',
                'image_url': 'https://cdn.pixabay.com/photo/2017/08/06/12/52/hammock-2590424_1280.jpg'
            },
            {
                'name': 'Sombreros',
                'description': 'Sombreros elegantes tejidos con fibras naturales',
                'image_url': 'https://cdn.pixabay.com/photo/2016/04/21/16/15/hat-1343410_1280.jpg'
            },
            {
                'name': 'Accesorios',
                'description': 'Pulseras, collares y otros accesorios únicos',
                'image_url': 'https://cdn.pixabay.com/photo/2017/08/01/11/48/jewelry-2564277_1280.jpg'
            },
            {
                'name': 'Textiles',
                'description': 'Mantas, tapices y otros textiles decorativos',
                'image_url': 'https://cdn.pixabay.com/photo/2017/03/29/04/47/industry-2185133_1280.jpg'
            }
        ]

        categories = {}
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={
                    'description': cat_data['description'],
                    'image_url': cat_data['image_url']
                }
            )
            categories[cat_data['name']] = category
            if created:
                self.stdout.write(f'Created category: {category.name}')

        # Create products
        products_data = [
            # Mochilas
            {
                'name': 'Mochila Wayuu Colorida Grande',
                'description': 'Hermosa mochila Wayuu tejida a mano con patrones tradicionales en colores vibrantes. Perfecta para el uso diario, combina tradición y funcionalidad. Cada pieza es única y cuenta la historia de nuestros artesanos.',
                'price': Decimal('120000'),
                'image_url': 'https://cdn.pixabay.com/photo/2019/07/15/18/47/bag-4339942_1280.jpg',
                'category': 'Mochilas',
                'artisan_name': 'María Uriana',
                'materials': 'Algodón, hilo acrílico',
                'dimensions': '35cm x 30cm',
                'weight': '400g',
                'colors': ['Rojo', 'Azul', 'Verde', 'Amarillo'],
                'stock_quantity': 15,
                'is_featured': True
            },
            {
                'name': 'Mochila Wayuu Mediana Clásica',
                'description': 'Mochila de tamaño mediano con diseños geométricos tradicionales. Ideal para llevar lo esencial con estilo único. Tejida con técnicas ancestrales transmitidas de generación en generación.',
                'price': Decimal('85000'),
                'image_url': 'https://cdn.pixabay.com/photo/2020/03/25/12/28/bag-4966249_1280.jpg',
                'category': 'Mochilas',
                'artisan_name': 'Carmen Ipuana',
                'materials': 'Algodón puro',
                'dimensions': '28cm x 25cm',
                'weight': '300g',
                'colors': ['Rosa', 'Morado', 'Turquesa'],
                'stock_quantity': 20,
                'is_featured': False
            },
            {
                'name': 'Mochila Wayuu Mini',
                'description': 'Pequeña pero con gran personalidad. Perfecta para ocasiones especiales o como accesorio elegante. Cada detalle está cuidadosamente tejido a mano.',
                'price': Decimal('65000'),
                'image_url': 'https://cdn.pixabay.com/photo/2017/08/01/11/48/jewelry-2564277_1280.jpg',
                'category': 'Mochilas',
                'artisan_name': 'Rosa Epiayú',
                'materials': 'Algodón, hilos metalizados',
                'dimensions': '20cm x 18cm',
                'weight': '200g',
                'colors': ['Dorado', 'Plata', 'Bronce'],
                'stock_quantity': 12,
                'is_featured': True
            },
            
            # Hamacas
            {
                'name': 'Hamaca Wayuu Grande Familiar',
                'description': 'Hamaca espaciosa tejida con algodón resistente. Perfecta para relajarse en familia. Su tejido tradicional garantiza comodidad y durabilidad excepcional.',
                'price': Decimal('180000'),
                'image_url': 'https://cdn.pixabay.com/photo/2017/08/06/12/52/hammock-2590424_1280.jpg',
                'category': 'Hamacas',
                'artisan_name': 'José Pushaina',
                'materials': 'Algodón 100%',
                'dimensions': '300cm x 150cm',
                'weight': '2kg',
                'colors': ['Natural', 'Beige', 'Crema'],
                'stock_quantity': 8,
                'is_featured': True
            },
            {
                'name': 'Hamaca Individual Colorida',
                'description': 'Hamaca individual con hermosos patrones en colores vibrantes. Ideal para espacios pequeños sin sacrificar el confort tradicional Wayuu.',
                'price': Decimal('95000'),
                'image_url': 'https://cdn.pixabay.com/photo/2018/05/30/00/24/thunderstorm-3441687_1280.jpg',
                'category': 'Hamacas',
                'artisan_name': 'Ana Gouriyu',
                'materials': 'Algodón, hilos de colores',
                'dimensions': '250cm x 100cm',
                'weight': '1.2kg',
                'colors': ['Multicolor', 'Arcoíris'],
                'stock_quantity': 10,
                'is_featured': False
            },
            
            # Sombreros
            {
                'name': 'Sombrero Wayuu Elegante',
                'description': 'Sombrero tradicional tejido con fibras naturales. Perfecto para protegerse del sol con estilo auténtico. Cada sombrero es una obra de arte única.',
                'price': Decimal('75000'),
                'image_url': 'https://cdn.pixabay.com/photo/2016/04/21/16/15/hat-1343410_1280.jpg',
                'category': 'Sombreros',
                'artisan_name': 'Pedro Jusayú',
                'materials': 'Palma iraca, algodón',
                'dimensions': 'Talla única ajustable',
                'weight': '150g',
                'colors': ['Natural', 'Café', 'Negro'],
                'stock_quantity': 18,
                'is_featured': True
            },
            {
                'name': 'Sombrero Decorativo',
                'description': 'Sombrero con detalles decorativos únicos. Combina funcionalidad y arte tradicional Wayuu en una pieza excepcional.',
                'price': Decimal('90000'),
                'image_url': 'https://cdn.pixabay.com/photo/2017/08/07/14/02/people-2604149_1280.jpg',
                'category': 'Sombreros',
                'artisan_name': 'Elena Sijona',
                'materials': 'Palma iraca, cuentas decorativas',
                'dimensions': 'Talla única',
                'weight': '180g',
                'colors': ['Decorado multicolor'],
                'stock_quantity': 6,
                'is_featured': False
            },
            
            # Accesorios
            {
                'name': 'Collar Wayuu Tradicional',
                'description': 'Collar artesanal con cuentas de colores y patrones geométricos tradicionales. Una pieza que conecta con las raíces ancestrales Wayuu.',
                'price': Decimal('45000'),
                'image_url': 'https://cdn.pixabay.com/photo/2017/08/01/11/48/jewelry-2564277_1280.jpg',
                'category': 'Accesorios',
                'artisan_name': 'Luz Ipuana',
                'materials': 'Cuentas de vidrio, hilo encerado',
                'dimensions': '60cm largo',
                'weight': '50g',
                'colors': ['Multicolor tradicional'],
                'stock_quantity': 25,
                'is_featured': True
            },
            {
                'name': 'Pulsera Tejida Wayuu',
                'description': 'Pulsera tejida a mano con hilos de colores vibrantes. El accesorio perfecto para llevar un pedazo de la cultura Wayuu contigo.',
                'price': Decimal('25000'),
                'image_url': 'https://cdn.pixabay.com/photo/2016/12/06/18/40/bracelet-1887292_1280.jpg',
                'category': 'Accesorios',
                'artisan_name': 'Carmen Uriana',
                'materials': 'Hilos de algodón',
                'dimensions': 'Ajustable',
                'weight': '15g',
                'colors': ['Rosa', 'Azul', 'Verde', 'Amarillo'],
                'stock_quantity': 40,
                'is_featured': False
            }
        ]

        for product_data in products_data:
            category = categories[product_data['category']]
            product, created = Product.objects.get_or_create(
                name=product_data['name'],
                defaults={
                    'description': product_data['description'],
                    'price': product_data['price'],
                    'image_url': product_data['image_url'],
                    'category': category,
                    'artisan_name': product_data['artisan_name'],
                    'materials': product_data['materials'],
                    'dimensions': product_data['dimensions'],
                    'weight': product_data['weight'],
                    'colors': product_data['colors'],
                    'stock_quantity': product_data['stock_quantity'],
                    'is_featured': product_data['is_featured']
                }
            )
            if created:
                self.stdout.write(f'Created product: {product.name}')

        # Create blog posts
        blog_posts_data = [
            {
                'title': 'La tradición Wayuu: Más que artesanía',
                'content': '''
                <h2>Un legado ancestral</h2>
                <p>La cultura Wayuu ha mantenido vivas sus tradiciones durante siglos. Cada mochila, cada hamaca, cada accesorio que creamos lleva consigo la historia de nuestro pueblo.</p>
                
                <h3>El arte del tejido</h3>
                <p>Nuestras artesanas aprenden desde niñas el arte del tejido. Es más que una técnica: es una forma de transmitir conocimiento, historias y amor de generación en generación.</p>
                
                <h3>Patrones con significado</h3>
                <p>Cada patrón tiene un significado especial. Los colores y formas no son aleatorios, sino que representan elementos de nuestra cosmovisión: el mar, el desierto, los animales sagrados.</p>
                
                <p>Cuando compras una pieza Wayuu, no solo adquieres un producto hermoso y funcional, sino que te conviertes en parte de nuestra historia y ayudas a preservar nuestra cultura.</p>
                ''',
                'excerpt': 'Descubre el profundo significado cultural detrás de cada pieza artesanal Wayuu y cómo nuestras tradiciones se mantienen vivas.',
                'featured_image': 'https://cdn.pixabay.com/photo/2019/07/15/18/47/bag-4339942_1280.jpg',
                'author': 'María Elena Uriana',
                'is_published': True,
                'is_recent_post': True
            },
            {
                'title': 'Cómo cuidar tu mochila Wayuu',
                'content': '''
                <h2>Consejos para mantener tu mochila como nueva</h2>
                <p>Las mochilas Wayuu son piezas duraderas, pero con el cuidado adecuado pueden durar toda la vida.</p>
                
                <h3>Limpieza</h3>
                <ul>
                    <li>Lava a mano con agua fría</li>
                    <li>Usa jabón neutro</li>
                    <li>No uses blanqueador</li>
                    <li>Seca a la sombra</li>
                </ul>
                
                <h3>Almacenamiento</h3>
                <p>Guarda tu mochila en un lugar seco y ventilado. Si no la vas a usar por mucho tiempo, rellénala con papel para mantener su forma.</p>
                
                <h3>Uso diario</h3>
                <p>Evita sobrecargarla más allá de su capacidad. Recuerda que cada mochila está tejida a mano con amor y merece ser tratada con cuidado.</p>
                ''',
                'excerpt': 'Aprende los mejores consejos para cuidar y mantener tu mochila Wayuu en perfectas condiciones durante años.',
                'featured_image': 'https://cdn.pixabay.com/photo/2020/03/25/12/28/bag-4966249_1280.jpg',
                'author': 'Carmen Ipuana',
                'is_published': True,
                'is_recent_post': True
            },
            {
                'title': 'El proceso de tejido: De la fibra al arte',
                'content': '''
                <h2>Un proceso que requiere paciencia y maestría</h2>
                <p>El tejido de una mochila Wayuu puede tomar entre 15 y 30 días, dependiendo del tamaño y la complejidad del diseño.</p>
                
                <h3>Selección de materiales</h3>
                <p>Todo comienza con la selección cuidadosa del algodón. Preferimos algodón de alta calidad que garantice durabilidad y suavidad.</p>
                
                <h3>Preparación del hilo</h3>
                <p>Los hilos se preparan y tiñen con colores vibrantes. Muchas veces utilizamos tintes naturales que nuestros ancestros han usado durante generaciones.</p>
                
                <h3>El tejido</h3>
                <p>Cada mochila se teje en espiral, desde la base hacia arriba. Es un proceso meditativo que requiere concentración total.</p>
                
                <h3>Los detalles finales</h3>
                <p>La correa se teje por separado y puede tomar varios días adicionales. Cada detalle es importante para crear una pieza perfecta.</p>
                ''',
                'excerpt': 'Conoce paso a paso el meticuloso proceso de creación de nuestras mochilas, desde la selección de materiales hasta los toques finales.',
                'featured_image': 'https://cdn.pixabay.com/photo/2017/03/29/04/47/industry-2185133_1280.jpg',
                'author': 'José Pushaina',
                'is_published': True,
                'is_recent_post': False
            },
            {
                'title': 'Wayuu Taya: El territorio ancestral',
                'content': '''
                <h2>La Guajira: Nuestra casa ancestral</h2>
                <p>El pueblo Wayuu habita en la península de La Guajira, un territorio que se extiende entre Colombia y Venezuela. Este es nuestro hogar ancestral.</p>
                
                <h3>Un paisaje único</h3>
                <p>Entre el desierto y el mar Caribe, nuestro territorio nos ha enseñado a ser resilientes y creativos. La aridez del desierto contrasta con la inmensidad azul del mar.</p>
                
                <h3>Conexión con la naturaleza</h3>
                <p>Nuestras creaciones reflejan los colores y formas de nuestro entorno: el azul del mar, el dorado del desierto, el verde de los cactus.</p>
                
                <h3>Preservando el territorio</h3>
                <p>A través de nuestro trabajo artesanal, no solo preservamos nuestras tradiciones, sino que también cuidamos nuestro territorio ancestral.</p>
                ''',
                'excerpt': 'Explora la conexión profunda entre el pueblo Wayuu y su territorio ancestral en La Guajira.',
                'featured_image': 'https://cdn.pixabay.com/photo/2018/05/30/00/24/thunderstorm-3441687_1280.jpg',
                'author': 'Pedro Jusayú',
                'is_published': True,
                'is_recent_post': False
            },
            {
                'title': 'Colores sagrados: El significado de cada tonalidad',
                'content': '''
                <h2>Cada color cuenta una historia</h2>
                <p>En la cultura Wayuu, los colores no son solo estética, sino que tienen significados profundos conectados con nuestra cosmovisión.</p>
                
                <h3>El azul del mar</h3>
                <p>Representa la inmensidad, la paz y la conexión con nuestros ancestros que navegan en el más allá.</p>
                
                <h3>El rojo de la tierra</h3>
                <p>Simboliza la fuerza, la vida y la conexión con Mma (la Tierra), nuestra madre sagrada.</p>
                
                <h3>El amarillo del sol</h3>
                <p>Representa la energía vital, la sabiduría y la luz que guía nuestro camino.</p>
                
                <h3>El verde de la esperanza</h3>
                <p>Simboliza la vida nueva, la esperanza y la armonía con la naturaleza.</p>
                
                <p>Cuando eliges los colores de tu mochila, estás eligiendo las energías que quieres llevar contigo.</p>
                ''',
                'excerpt': 'Descubre el profundo significado espiritual y cultural de los colores utilizados en nuestras creaciones artesanales.',
                'featured_image': 'https://cdn.pixabay.com/photo/2017/08/01/11/48/jewelry-2564277_1280.jpg',
                'author': 'Elena Sijona',
                'is_published': True,
                'is_recent_post': True
            }
        ]

        for post_data in blog_posts_data:
            slug = slugify(post_data['title'])
            # Ensure unique slug
            original_slug = slug
            counter = 1
            while BlogPost.objects.filter(slug=slug).exists():
                slug = f"{original_slug}-{counter}"
                counter += 1

            blog_post, created = BlogPost.objects.get_or_create(
                title=post_data['title'],
                defaults={
                    'slug': slug,
                    'content': post_data['content'],
                    'excerpt': post_data['excerpt'],
                    'featured_image': post_data['featured_image'],
                    'author': post_data['author'],
                    'is_published': post_data['is_published'],
                    'is_recent_post': post_data['is_recent_post']
                }
            )
            if created:
                self.stdout.write(f'Created blog post: {blog_post.title}')

        self.stdout.write(self.style.SUCCESS('Sample data created successfully!'))
