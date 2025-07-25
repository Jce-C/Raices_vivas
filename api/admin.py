from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Category, Product, CartItem, Order, OrderItem, BlogPost, Contact


class CustomUserAdmin(UserAdmin):
    """Custom admin for User model"""
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_admin', 'created_at']
    list_filter = ['is_admin', 'is_staff', 'is_active', 'created_at']
    fieldsets = UserAdmin.fieldsets + (
        ('Información adicional', {
            'fields': ('phone', 'address', 'city', 'country', 'is_admin')
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Información adicional', {
            'fields': ('phone', 'address', 'city', 'country', 'is_admin')
        }),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'name': ()}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock_quantity', 'is_featured', 'is_active', 'created_at']
    list_filter = ['category', 'is_featured', 'is_active', 'created_at']
    search_fields = ['name', 'description', 'artisan_name']
    list_editable = ['price', 'stock_quantity', 'is_featured', 'is_active']


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__username', 'product__name']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'total_amount', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['user__username', 'user__email']


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price']
    list_filter = ['order__created_at']
    search_fields = ['order__order_number', 'product__name']


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'is_published', 'created_at']
    list_filter = ['is_published', 'created_at']
    search_fields = ['title', 'content', 'author']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['is_published']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject']
    list_editable = ['is_read']
    readonly_fields = ['created_at']


# Register the custom user admin
admin.site.register(User, CustomUserAdmin)