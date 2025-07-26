"""URL configuration for Wayuu Artesania API"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# API URL patterns
urlpatterns = [
    # Authentication endpoints
    path('auth/register/', views.register_view, name='register'),
    path('auth/login/', views.login_view, name='login'),
    path('auth/logout/', views.logout_view, name='logout'),
    path('auth/profile/', views.profile_view, name='profile'),

    # Category endpoints
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),

    # Product endpoints
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('products/featured/', views.featured_products_view, name='featured-products'),

    # Cart endpoints
    path('cart/', views.CartItemListView.as_view(), name='cart-list'),
    path('cart/<int:pk>/', views.CartItemDetailView.as_view(), name='cart-detail'),
    path('cart/clear/', views.clear_cart_view, name='cart-clear'),

    # Order endpoints
    path('orders/', views.OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),

    # Blog endpoints
    path('blog/', views.BlogPostListView.as_view(), name='blog-list'),
    path('blog/<slug:slug>/', views.BlogPostDetailView.as_view(), name='blog-detail'),

    # Contact endpoint
    path('contact/', views.contact_view, name='contact'),
    path('admin/contacts/', views.ContactListView.as_view(), name='contact-list'),

    # Legacy endpoints for compatibility
    path('', views.ProductListView.as_view(), name='index'),  # Home page shows products
    path('shop/', views.ProductListView.as_view(), name='shop'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail-legacy'),
]