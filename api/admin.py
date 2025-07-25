"""
Django admin configuration for Wayuu Artesania API
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Category, Product, CartItem, Order, OrderItem, BlogPost, Contact


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Admin configuration for User model"""
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_admin', 'created_at']
    list_filter = ['is_admin', 'is_staff', 'is_active', 'created_at']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    ordering = ['-created_at']
    
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('phone', 'address', 'city', 'country', 'is_admin')
        }),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin configuration for Category model"""
    list_display = ['name', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {}
    ordering = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Admin configuration for Product model"""
    list_display = ['name', 'category', 'price', 'stock_quantity', 'is_featured', 'is_active', 'created_at']
    list_filter = ['category', 'is_featured', 'is_active', 'created_at']
    search_fields = ['name', 'description', 'artisan_name']
    list_editable = ['price', 'stock_quantity', 'is_featured', 'is_active']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'category', 'price', 'stock_quantity')
        }),
        ('Images', {
            'fields': ('image_url', 'additional_images')
        }),
        ('Product Details', {
            'fields': ('artisan_name', 'materials', 'dimensions', 'weight', 'colors')
        }),
        ('Status', {
            'fields': ('is_featured', 'is_active')
        }),
    )


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    """Admin configuration for CartItem model"""
    list_display = ['user', 'product', 'quantity', 'selected_color', 'added_at']
    list_filter = ['added_at', 'selected_color']
    search_fields = ['user__username', 'product__name']
    ordering = ['-added_at']


class OrderItemInline(admin.TabularInline):
    """Inline admin for OrderItem"""
    model = OrderItem
    extra = 0
    readonly_fields = ['product', 'quantity', 'price', 'selected_color']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Admin configuration for Order model"""
    list_display = ['order_number', 'user', 'status', 'total_amount', 'payment_status', 'created_at']
    list_filter = ['status', 'payment_status', 'created_at']
    search_fields = ['order_number', 'user__username', 'billing_email']
    list_editable = ['status', 'payment_status']
    ordering = ['-created_at']
    inlines = [OrderItemInline]
    
    fieldsets = (
        ('Order Information', {
            'fields': ('user', 'order_number', 'status', 'total_amount', 'payment_status')
        }),
        ('Billing Information', {
            'fields': ('billing_first_name', 'billing_last_name', 'billing_email', 
                      'billing_phone', 'billing_address', 'billing_city', 
                      'billing_country', 'billing_postal_code')
        }),
        ('Shipping Information', {
            'fields': ('shipping_first_name', 'shipping_last_name', 'shipping_address',
                      'shipping_city', 'shipping_country', 'shipping_postal_code')
        }),
        ('Payment', {
            'fields': ('payment_method',)
        }),
    )
    
    readonly_fields = ['order_number', 'created_at', 'updated_at']


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    """Admin configuration for BlogPost model"""
    list_display = ['title', 'author', 'is_published', 'created_at']
    list_filter = ['is_published', 'created_at', 'author']
    search_fields = ['title', 'content', 'author']
    list_editable = ['is_published']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-created_at']
    
    fieldsets = (
        ('Content', {
            'fields': ('title', 'slug', 'content', 'excerpt')
        }),
        ('Media', {
            'fields': ('featured_image',)
        }),
        ('Publishing', {
            'fields': ('author', 'is_published')
        }),
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Admin configuration for Contact model"""
    list_display = ['name', 'email', 'subject', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    list_editable = ['is_read']
    ordering = ['-created_at']
    readonly_fields = ['created_at']
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'subject')
        }),
        ('Message', {
            'fields': ('message',)
        }),
        ('Status', {
            'fields': ('is_read',)
        }),
    )
