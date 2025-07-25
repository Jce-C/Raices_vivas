"""
Django models for Wayuu Artesania API
Converted from Flask SQLAlchemy models to Django ORM
"""
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal
import uuid


class User(AbstractUser):
    """Extended User model with additional fields for e-commerce"""
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='api_users',
        related_query_name='api_user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='api_users',
        related_query_name='api_user',
    )

    def get_cart_total(self):
        """Calculate total amount of items in user's cart"""
        total = Decimal('0.00')
        for item in self.cart_items.all():
            total += item.product.price * item.quantity
        return total

    def get_cart_count(self):
        """Get total number of items in user's cart"""
        return sum(item.quantity for item in self.cart_items.all())


class Category(models.Model):
    """Product categories"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    """Product model for artisan items"""
    name = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    image_url = models.URLField()
    additional_images = models.JSONField(default=list, blank=True)
    stock_quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    artisan_name = models.CharField(max_length=100, blank=True, null=True)
    materials = models.CharField(max_length=255, blank=True, null=True)
    dimensions = models.CharField(max_length=100, blank=True, null=True)
    weight = models.CharField(max_length=50, blank=True, null=True)
    colors = models.JSONField(default=list, blank=True)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def is_in_stock(self):
        """Check if product is in stock"""
        return self.stock_quantity > 0


class CartItem(models.Model):
    """Shopping cart items"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['user', 'product']
        verbose_name = 'Item del Carrito'
        verbose_name_plural = 'Items del Carrito'

    def __str__(self):
        return f'{self.user.username} - {self.product.name} ({self.quantity})'

    def get_total_price(self):
        """Calcula el precio total del item (precio * cantidad)"""
        return self.product.price * self.quantity


class Order(models.Model):
    """Customer orders"""
    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('confirmed', 'Confirmado'),
        ('processing', 'Procesando'),
        ('shipped', 'Enviado'),
        ('delivered', 'Entregado'),
        ('cancelled', 'Cancelado'),
    ]

    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('paid', 'Pagado'),
        ('failed', 'Fallido'),
        ('refunded', 'Reembolsado'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    order_number = models.CharField(max_length=20, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    # Billing information
    billing_first_name = models.CharField(max_length=50)
    billing_last_name = models.CharField(max_length=50)
    billing_email = models.EmailField()
    billing_phone = models.CharField(max_length=20)
    billing_address = models.TextField()
    billing_city = models.CharField(max_length=50)
    billing_country = models.CharField(max_length=50)
    billing_postal_code = models.CharField(max_length=20, blank=True, null=True)

    # Shipping information
    shipping_first_name = models.CharField(max_length=50, blank=True, null=True)
    shipping_last_name = models.CharField(max_length=50, blank=True, null=True)
    shipping_address = models.TextField(blank=True, null=True)
    shipping_city = models.CharField(max_length=50, blank=True, null=True)
    shipping_country = models.CharField(max_length=50, blank=True, null=True)
    shipping_postal_code = models.CharField(max_length=20, blank=True, null=True)

    # Payment information
    payment_method = models.CharField(max_length=50, blank=True, null=True)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Order {self.order_number} - {self.user.username}"

    def get_total_items(self):
        """Get total number of items in this order"""
        return sum(item.quantity for item in self.order_items.all())


class OrderItem(models.Model):
    """Items within an order"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price at time of order
    selected_color = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.order.order_number} - {self.product.name} ({self.quantity})"

    def get_total_price(self):
        """Calculate total price for this order item"""
        return self.price * self.quantity


class BlogPost(models.Model):
    """Blog posts about artisan culture and products"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True, null=True)
    featured_image = models.URLField(blank=True, null=True)
    author = models.CharField(max_length=100)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Contact(models.Model):
    """Contact form submissions"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Contact from {self.name} - {self.subject}"