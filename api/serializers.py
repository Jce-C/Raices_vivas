"""
Django REST Framework serializers for Wayuu Artesania API
"""
from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User, Category, Product, CartItem, Order, OrderItem, BlogPost, Contact


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""
    password = serializers.CharField(write_only=True)
    cart_total = serializers.SerializerMethodField()
    cart_count = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 
                 'phone', 'address', 'city', 'country', 'is_admin', 
                 'created_at', 'password', 'cart_total', 'cart_count']
        extra_kwargs = {'password': {'write_only': True}}
    
    def get_cart_total(self, obj):
        return float(obj.get_cart_total())
    
    def get_cart_count(self, obj):
        return obj.get_cart_count()
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    """Serializer for user login"""
    username = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data['user'] = user
                else:
                    raise serializers.ValidationError('User account is disabled.')
            else:
                raise serializers.ValidationError('Unable to log in with provided credentials.')
        else:
            raise serializers.ValidationError('Must include username and password.')
        
        return data


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category model"""
    products_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'image_url', 'is_active', 
                 'created_at', 'products_count']
    
    def get_products_count(self, obj):
        return obj.products.filter(is_active=True).count()


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for Product model"""
    category_name = serializers.CharField(source='category.name', read_only=True)
    in_stock = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image_url', 
                 'additional_images', 'stock_quantity', 'category', 'category_name',
                 'artisan_name', 'materials', 'dimensions', 'weight', 'colors',
                 'is_featured', 'is_active', 'created_at', 'updated_at', 'in_stock']
    
    def get_in_stock(self, obj):
        return obj.is_in_stock()


class CartItemSerializer(serializers.ModelSerializer):
    """Serializer for CartItem model"""
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_price = serializers.DecimalField(source='product.price', max_digits=10, decimal_places=2, read_only=True)
    product_image = serializers.URLField(source='product.image_url', read_only=True)
    total_price = serializers.SerializerMethodField()
    
    class Meta:
        model = CartItem
        fields = ['id', 'user', 'product', 'product_name', 'product_price', 
                 'product_image', 'quantity', 'selected_color', 'added_at', 'total_price']
        read_only_fields = ['user', 'added_at']
    
    def get_total_price(self, obj):
        return float(obj.get_total_price())


class OrderItemSerializer(serializers.ModelSerializer):
    """Serializer for OrderItem model"""
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_image = serializers.URLField(source='product.image_url', read_only=True)
    total_price = serializers.SerializerMethodField()
    
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'product_image', 
                 'quantity', 'price', 'selected_color', 'total_price']
    
    def get_total_price(self, obj):
        return float(obj.get_total_price())


class OrderSerializer(serializers.ModelSerializer):
    """Serializer for Order model"""
    order_items = OrderItemSerializer(many=True, read_only=True)
    user_name = serializers.CharField(source='user.get_full_name', read_only=True)
    total_items = serializers.SerializerMethodField()
    
    class Meta:
        model = Order
        fields = ['id', 'user', 'user_name', 'order_number', 'status', 'total_amount',
                 'billing_first_name', 'billing_last_name', 'billing_email', 'billing_phone',
                 'billing_address', 'billing_city', 'billing_country', 'billing_postal_code',
                 'shipping_first_name', 'shipping_last_name', 'shipping_address',
                 'shipping_city', 'shipping_country', 'shipping_postal_code',
                 'payment_method', 'payment_status', 'created_at', 'updated_at',
                 'order_items', 'total_items']
        read_only_fields = ['user', 'order_number', 'created_at', 'updated_at']
    
    def get_total_items(self, obj):
        return obj.get_total_items()


class BlogPostSerializer(serializers.ModelSerializer):
    """Serializer for BlogPost model"""
    
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'slug', 'content', 'excerpt', 'featured_image',
                 'author', 'is_published', 'created_at', 'updated_at']


class ContactSerializer(serializers.ModelSerializer):
    """Serializer for Contact model"""
    
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', 'subject', 'message', 'is_read', 'created_at']
        read_only_fields = ['created_at']
