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
    path('blog/<slug:slug>/', template_views.blog_detail, name='blog_detail'),
    path('contact/', template_views.contact, name='contact'),
    path('login/', template_views.login_view, name='login'),
    path('register/', template_views.register_view, name='register'),
    path('logout/', template_views.logout_view, name='logout_view'),
    path('profile/', template_views.profile, name='profile'),
    path('cart/', template_views.cart, name='cart'),
    path('cart/add/', template_views.add_to_cart, name='add_to_cart'),
    path('checkout/', template_views.checkout, name='checkout'),
    path('admin/add-product/', template_views.admin_add_product, name='admin_add_product'),
    path('admin/add-blog-post/', template_views.admin_add_blog_post, name='admin_add_blog_post'),
]