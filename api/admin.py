from django.contrib import admin
from django.utils.html import format_html
from django.utils.text import slugify
from .models import (User, Category, Product, CartItem, Order, OrderItem, 
                     BlogPost, Contact)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'created_at')
    list_filter = ('created_at', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    readonly_fields = ('created_at',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'products_count', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at',)

    def products_count(self, obj):
        return obj.products.count()
    products_count.short_description = 'Productos'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock_quantity', 'is_featured', 'is_active', 'image_preview')
    list_filter = ('category', 'is_featured', 'is_active', 'created_at')
    search_fields = ('name', 'description', 'artisan_name')
    readonly_fields = ('created_at', 'image_preview')
    list_editable = ('is_featured', 'is_active', 'stock_quantity')
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('name', 'category', 'description', 'price', 'stock_quantity')
        }),
        ('Imágenes', {
            'fields': ('image_url', 'image_preview', 'additional_images'),
            'classes': ('wide',)
        }),
        ('Detalles del Artesano', {
            'fields': ('artisan_name', 'materials', 'dimensions', 'weight', 'colors'),
            'classes': ('collapse',)
        }),
        ('Configuración', {
            'fields': ('is_featured', 'is_active', 'created_at'),
            'classes': ('collapse',)
        }),
    )

    def image_preview(self, obj):
        if obj.image_url:
            return format_html(
                '<img src="{}" width="100" height="100" style="object-fit: cover; border-radius: 8px;" />',
                obj.image_url
            )
        return "Sin imagen"
    image_preview.short_description = 'Vista Previa'
    
    class Media:
        css = {
            'all': ('admin/css/custom_admin.css',)
        }

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'user', 'status', 'total_amount', 'created_at')
    list_filter = ('status', 'payment_status', 'created_at')
    search_fields = ('order_number', 'user__username', 'billing_email')
    readonly_fields = ('order_number', 'created_at', 'updated_at')

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_published', 'is_recent_post', 'is_featured', 'created_at', 'post_preview')
    list_filter = ('is_published', 'is_recent_post', 'is_featured', 'created_at', 'author')
    search_fields = ('title', 'content', 'author')
    readonly_fields = ('slug', 'created_at', 'updated_at')
    list_editable = ('is_published', 'is_recent_post', 'is_featured')

    fieldsets = (
        ('Información Básica', {
            'fields': ('title', 'slug', 'author', 'is_published', 'is_recent_post', 'is_featured')
        }),
        ('Contenido', {
            'fields': ('excerpt', 'content', 'featured_image'),
            'classes': ('wide',)
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(obj.title)
        super().save_model(request, obj, form, change)

    def post_preview(self, obj):
        if obj.featured_image:
            return format_html('<img src="{}" width="50" height="50" />', obj.featured_image)
        return "Sin imagen"
    post_preview.short_description = 'Preview'

    class Media:
        css = {
            'all': ('admin/css/blog_admin.css', 'admin/css/custom_admin.css')
        }
        js = ('admin/js/blog_admin.js',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at',)
    list_editable = ('is_read',)