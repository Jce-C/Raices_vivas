
"""
Django admin configuration for Wayuu Artesania
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Category, Product, CartItem, Order, OrderItem, BlogPost, Contact


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'created_at')
    list_filter = ('is_staff', 'is_active', 'created_at')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Información Adicional', {
            'fields': ('phone', 'address', 'city', 'country')
        }),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'description')
    prepopulated_fields = {}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock_quantity', 'artisan_name', 'is_featured', 'is_active')
    list_filter = ('category', 'is_featured', 'is_active', 'created_at')
    search_fields = ('name', 'description', 'artisan_name', 'materials')
    list_editable = ('is_featured', 'is_active')
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('name', 'description', 'category', 'price')
        }),
        ('Imágenes', {
            'fields': ('image_url', 'additional_images')
        }),
        ('Inventario', {
            'fields': ('stock_quantity',)
        }),
        ('Detalles del Artesano', {
            'fields': ('artisan_name', 'materials', 'dimensions', 'weight', 'colors')
        }),
        ('Estado', {
            'fields': ('is_featured', 'is_active')
        }),
    )


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'product__name')


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product', 'quantity', 'price', 'selected_color')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'user', 'status', 'total_amount', 'payment_status', 'created_at')
    list_filter = ('status', 'payment_status', 'created_at')
    search_fields = ('order_number', 'user__username', 'billing_email')
    readonly_fields = ('order_number', 'created_at', 'updated_at')
    inlines = [OrderItemInline]
    
    fieldsets = (
        ('Información de la Orden', {
            'fields': ('order_number', 'user', 'status', 'total_amount', 'payment_method', 'payment_status')
        }),
        ('Información de Facturación', {
            'fields': ('billing_first_name', 'billing_last_name', 'billing_email', 'billing_phone',
                      'billing_address', 'billing_city', 'billing_country', 'billing_postal_code')
        }),
        ('Información de Envío', {
            'fields': ('shipping_first_name', 'shipping_last_name', 'shipping_address',
                      'shipping_city', 'shipping_country', 'shipping_postal_code')
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at')
        }),
    )


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_published', 'created_at')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'content', 'author')
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ('is_published',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)
    list_editable = ('is_read',)
