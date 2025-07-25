"""
Django REST Framework views for Wayuu Artesania API
"""
from rest_framework import generics, status, permissions, filters
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import login, logout
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from .models import User, Category, Product, CartItem, Order, OrderItem, BlogPost, Contact
from .serializers import (
    UserSerializer, LoginSerializer, CategorySerializer, ProductSerializer,
    CartItemSerializer, OrderSerializer, BlogPostSerializer, ContactSerializer
)
from .utils import generate_order_number
import logging

logger = logging.getLogger(__name__)


# Authentication Views
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register_view(request):
    """User registration endpoint"""
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'user': UserSerializer(user).data,
            'token': token.key,
            'message': 'Usuario registrado exitosamente'
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login_view(request):
    """User login endpoint"""
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        login(request, user)
        return Response({
            'user': UserSerializer(user).data,
            'token': token.key,
            'message': 'Inicio de sesión exitoso'
        }, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def logout_view(request):
    """User logout endpoint"""
    try:
        request.user.auth_token.delete()
    except:
        pass
    logout(request)
    return Response({'message': 'Sesión cerrada exitosamente'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def profile_view(request):
    """Get user profile"""
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


# Category Views
class CategoryListView(generics.ListCreateAPIView):
    """List all categories or create a new category"""
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'created_at']
    ordering = ['name']


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a category"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Product Views
class ProductListView(generics.ListCreateAPIView):
    """List all products or create a new product"""
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'is_featured', 'artisan_name']
    search_fields = ['name', 'description', 'artisan_name', 'materials']
    ordering_fields = ['name', 'price', 'created_at']
    ordering = ['-created_at']


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a product"""
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def featured_products_view(request):
    """Get featured products"""
    products = Product.objects.filter(is_featured=True, is_active=True)[:8]
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


# Cart Views
class CartItemListView(generics.ListCreateAPIView):
    """List user's cart items or add item to cart"""
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        # Check if item already exists in cart
        product = serializer.validated_data['product']
        selected_color = serializer.validated_data.get('selected_color')
        quantity = serializer.validated_data['quantity']
        
        existing_item = CartItem.objects.filter(
            user=self.request.user,
            product=product,
            selected_color=selected_color
        ).first()
        
        if existing_item:
            existing_item.quantity += quantity
            existing_item.save()
            return existing_item
        else:
            serializer.save(user=self.request.user)


class CartItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a cart item"""
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)


@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def clear_cart_view(request):
    """Clear all items from user's cart"""
    CartItem.objects.filter(user=request.user).delete()
    return Response({'message': 'Carrito vaciado exitosamente'}, status=status.HTTP_200_OK)


# Order Views
class OrderListView(generics.ListCreateAPIView):
    """List user's orders or create a new order"""
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        # Generate order number and process cart items
        order = serializer.save(
            user=self.request.user,
            order_number=generate_order_number()
        )
        
        # Move cart items to order items
        cart_items = CartItem.objects.filter(user=self.request.user)
        total_amount = 0
        
        for cart_item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                quantity=cart_item.quantity,
                price=cart_item.product.price,
                selected_color=cart_item.selected_color
            )
            total_amount += cart_item.product.price * cart_item.quantity
        
        # Update order total and clear cart
        order.total_amount = total_amount
        order.save()
        cart_items.delete()


class OrderDetailView(generics.RetrieveAPIView):
    """Retrieve order details"""
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


# Blog Views
class BlogPostListView(generics.ListAPIView):
    """List published blog posts"""
    queryset = BlogPost.objects.filter(is_published=True)
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content', 'author']
    ordering_fields = ['created_at', 'title']
    ordering = ['-created_at']


class BlogPostDetailView(generics.RetrieveAPIView):
    """Retrieve blog post by slug"""
    queryset = BlogPost.objects.filter(is_published=True)
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'slug'


# Contact Views
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def contact_view(request):
    """Submit contact form"""
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message': 'Mensaje enviado exitosamente. Te contactaremos pronto.'
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Admin Views (for managing contacts)
class ContactListView(generics.ListAPIView):
    """List all contact submissions (admin only)"""
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAdminUser]
    filter_backends = [filters.OrderingFilter]
    ordering = ['-created_at']
