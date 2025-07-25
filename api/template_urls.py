"""
URL configuration for template views (HTML pages)
"""
from django.urls import path
from . import template_views

urlpatterns = [
    # Main pages
    path('', template_views.home, name='home'),
    path('shop/', template_views.shop, name='shop'),
    path('product/<int:product_id>/', template_views.product_detail, name='product_detail'),
    path('blog/', template_views.blog, name='blog'),
    path('contact/', template_views.contact, name='contact'),

    # User authentication
    path('login/', template_views.login_view, name='login_view'),
    path('register/', template_views.register_view, name='register_view'),
    path('logout/', template_views.logout_view, name='logout_view'),
    path('profile/', template_views.profile, name='profile_view'),

    # Shopping cart and orders
    path('cart/', template_views.cart, name='cart'),
    path('checkout/', template_views.checkout, name='checkout'),
    path('order-confirmation/<int:order_id>/', template_views.order_confirmation, name='order_confirmation'),

    # AJAX endpoints for cart functionality
    path('ajax/add-to-cart/', template_views.add_to_cart, name='add_to_cart'),
    path('ajax/update-cart/', template_views.update_cart, name='update_cart'),
    path('ajax/remove-from-cart/', template_views.remove_from_cart, name='remove_from_cart'),
]