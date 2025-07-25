"""
Django management command to create sample data for Wayuu Artesania
Equivalent to the create_sample_data function from Flask version
"""
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from api.models import Category, Product, BlogPost
from api.utils import get_sample_products, get_sample_blog_posts
from decimal import Decimal

User = get_user_model()


class Command(BaseCommand):
    help = 'Create sample data for Wayuu Artesania'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')
        
        # Create categories if they don't exist
        if Category.objects.count() == 0:
            categories_data = [
                {'name': 'Mochilas', 'description': 'Mochilas tradicionales Wayuu'},
                {'name': 'Bolsos', 'description': 'Bolsos artesanales'},
                {'name': 'Hamacas', 'description': 'Hamacas tejidas a mano'},
                {'name': 'Accesorios', 'description': 'Accesorios únicos'}
            ]
            
            for cat_data in categories_data:
                category = Category.objects.create(
                    name=cat_data['name'],
                    description=cat_data['description']
                )
                self.stdout.write(f'Created category: {category.name}')
        
        # Create sample products if they don't exist
        if Product.objects.count() == 0:
            sample_products = get_sample_products()
            for product_data in sample_products:
                try:
                    category = Category.objects.get(name=product_data['category'])
                    product = Product.objects.create(
                        name=product_data['name'],
                        description=product_data['description'],
                        price=product_data['price'],
                        image_url=product_data['image_url'],
                        category=category,
                        artisan_name=product_data['artisan_name'],
                        materials=product_data['materials'],
                        colors=product_data['colors'],
                        dimensions=product_data.get('dimensions', ''),
                        weight=product_data.get('weight', ''),
                        stock_quantity=10,
                        is_featured=True if 'Mochila' in product_data['name'] else False
                    )
                    self.stdout.write(f'Created product: {product.name}')
                except Category.DoesNotExist:
                    self.stdout.write(f'Category {product_data["category"]} not found')
        
        # Create sample blog posts if they don't exist
        if BlogPost.objects.count() == 0:
            sample_posts = get_sample_blog_posts()
            for post_data in sample_posts:
                blog_post = BlogPost.objects.create(
                    title=post_data['title'],
                    slug=post_data['slug'],
                    content=post_data['content'],
                    excerpt=post_data['excerpt'],
                    featured_image=post_data['featured_image'],
                    author=post_data['author'],
                    is_published=post_data['is_published']
                )
                self.stdout.write(f'Created blog post: {blog_post.title}')
        
        # Create admin user if it doesn't exist
        if not User.objects.filter(is_superuser=True).exists():
            admin_user = User.objects.create_superuser(
                username='admin',
                email='admin@wayuuartesania.com',
                password='admin123',
                first_name='Admin',
                last_name='User'
            )
            self.stdout.write('Created admin user: admin/admin123')
        
        self.stdout.write(self.style.SUCCESS('Sample data created successfully!'))
