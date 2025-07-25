# MODELOS DE LA BASE DE DATOS - RAÍCES VIVAS
# Aquí definimos las "tablas" de nuestra base de datos
# Para estudiantes: Estos son como plantillas para guardar información

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

# MODELO DE USUARIO
# Esta "clase" define cómo guardamos la información de los usuarios
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20))
    address = db.Column(db.Text)
    city = db.Column(db.String(50))
    country = db.Column(db.String(50))
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    orders = db.relationship('Order', backref='user', lazy=True)
    cart_items = db.relationship('CartItem', backref='user', lazy=True)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_cart_total(self):
        total = 0
        for item in self.cart_items:
            total += item.product.price * item.quantity
        return total
    
    def get_cart_count(self):
        return sum(item.quantity for item in self.cart_items)

class Category(db.Model):
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    products = db.relationship('Product', backref='category', lazy=True)

class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    additional_images = db.Column(db.JSON)  # Store array of image URLs
    stock_quantity = db.Column(db.Integer, default=0)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    artisan_name = db.Column(db.String(100))
    materials = db.Column(db.String(255))
    dimensions = db.Column(db.String(100))
    weight = db.Column(db.String(50))
    colors = db.Column(db.JSON)  # Store array of available colors
    is_featured = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    cart_items = db.relationship('CartItem', backref='product', lazy=True)
    order_items = db.relationship('OrderItem', backref='product', lazy=True)

class CartItem(db.Model):
    __tablename__ = 'cart_items'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    selected_color = db.Column(db.String(50))
    added_at = db.Column(db.DateTime, default=datetime.utcnow)

class Order(db.Model):
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    order_number = db.Column(db.String(20), unique=True, nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, confirmed, shipped, delivered, cancelled
    total_amount = db.Column(db.Numeric(10, 2), nullable=False)
    
    # Billing details
    billing_first_name = db.Column(db.String(50), nullable=False)
    billing_last_name = db.Column(db.String(50), nullable=False)
    billing_email = db.Column(db.String(120), nullable=False)
    billing_phone = db.Column(db.String(20), nullable=False)
    billing_address = db.Column(db.Text, nullable=False)
    billing_city = db.Column(db.String(50), nullable=False)
    billing_country = db.Column(db.String(50), nullable=False)
    billing_postal_code = db.Column(db.String(20))
    
    # Shipping details (if different from billing)
    shipping_first_name = db.Column(db.String(50))
    shipping_last_name = db.Column(db.String(50))
    shipping_address = db.Column(db.Text)
    shipping_city = db.Column(db.String(50))
    shipping_country = db.Column(db.String(50))
    shipping_postal_code = db.Column(db.String(20))
    
    payment_method = db.Column(db.String(50))
    payment_status = db.Column(db.String(20), default='pending')
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    order_items = db.relationship('OrderItem', backref='order', lazy=True)

class OrderItem(db.Model):
    __tablename__ = 'order_items'
    
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)  # Price at time of order
    selected_color = db.Column(db.String(50))

class BlogPost(db.Model):
    __tablename__ = 'blog_posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    excerpt = db.Column(db.Text)
    featured_image = db.Column(db.String(255))
    author = db.Column(db.String(100), nullable=False)
    is_published = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Contact(db.Model):
    __tablename__ = 'contacts'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200))
    message = db.Column(db.Text, nullable=False)
    is_read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
