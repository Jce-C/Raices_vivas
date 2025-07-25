from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Product, Category, CartItem, Order, OrderItem, BlogPost, Contact
from .serializers import ContactSerializer
import json


def home(request):
    """Vista principal usando el template index.html existente"""
    # Obtener productos destacados para mostrar en el home
    featured_products = Product.objects.filter(is_featured=True, is_active=True)[:6]
    categories = Category.objects.filter(is_active=True)

    # Si no hay productos, crear algunos de muestra para la demo
    if not featured_products.exists():
        # Crear datos de muestra para la demo
        sample_products = []
        for i in range(1, 5):
            sample_products.append({
                'id': i,
                'name': f'Artesanía Wayuu {i}',
                'price': 150000 + (i * 50000),
                'artisan_name': f'Artesana María {i}',
                'image_url': f'https://picsum.photos/400/300?random={i}'
            })
        featured_products = sample_products

    # Imágenes de muestra para el carrusel
    artisan_images = [
        'https://picsum.photos/400/300?random=10',
        'https://picsum.photos/400/300?random=11', 
        'https://picsum.photos/400/300?random=12',
        'https://picsum.photos/400/300?random=13',
        'https://picsum.photos/400/300?random=14',
        'https://picsum.photos/400/300?random=15'
    ]

    # Posts del blog de muestra
    blog_posts = [
        {
            'title': 'La Tradición Wayuu',
            'excerpt': 'Conoce la rica historia detrás de las artesanías Wayuu...',
            'featured_image': 'https://picsum.photos/400/300?random=20',
            'author': 'Admin',
            'slug': 'tradicion-wayuu'
        },
        {
            'title': 'Técnicas Ancestrales', 
            'excerpt': 'Las técnicas de tejido se han transmitido por generaciones...',
            'featured_image': 'https://picsum.photos/400/300?random=21',
            'author': 'Admin',
            'slug': 'tecnicas-ancestrales'
        }
    ]

    context = {
        'featured_products': featured_products,
        'categories': categories,
        'artisan_images': artisan_images,
        'blog_posts': blog_posts,
    }
    return render(request, 'index.html', context)


def shop(request):
    """Vista de la tienda usando el template shop.html existente"""
    from django.core.paginator import Paginator

    products = Product.objects.filter(is_active=True)
    categories = Category.objects.filter(is_active=True)

    # Filtro por categoría
    category_id = request.GET.get('category')
    current_category = None
    if category_id:
        try:
            current_category = int(category_id)
            products = products.filter(category_id=current_category)
        except (ValueError, TypeError):
            current_category = None

    # Búsqueda
    search = request.GET.get('search', '')
    if search:
        products = products.filter(name__icontains=search)

    # Ordenamiento
    sort = request.GET.get('sort', '')
    if sort == 'price_asc':
        products = products.order_by('price')
    elif sort == 'price_desc':
        products = products.order_by('-price')

    # Si no hay productos en la base de datos, crear algunos de muestra
    if not products.exists() and not search and not current_category:
        sample_products = []
        for i in range(1, 13):
            sample_products.append({
                'id': i,
                'name': f'Artesanía Wayuu {i}',
                'description': f'Hermosa artesanía tradicional Wayuu hecha a mano por artesanas expertas. Cada pieza es única y representa la rica cultura de la comunidad Wayuu.',
                'price': 150000 + (i * 25000),
                'artisan_name': f'Artesana María {i}',
                'image_url': f'https://picsum.photos/400/300?random={i + 100}',
                'colors': ['Rojo', 'Azul', 'Verde', 'Amarillo'][:(i % 4) + 1],
                'is_featured': i <= 3,
                'stock_quantity': 10
            })

        # Crear un objeto similar a la paginación para los datos de muestra
        paginator = Paginator(sample_products, 12)
        page_number = request.GET.get('page', 1)
        products_page = paginator.get_page(page_number)

        # Convertir a objetos que el template pueda usar
        class MockProduct:
            def __init__(self, data):
                for key, value in data.items():
                    setattr(self, key, value)

        products_page.object_list = [MockProduct(product) for product in products_page.object_list]

        context = {
            'products': products_page,
            'categories': categories,
            'current_category': current_category,
            'search': search,
            'sort': sort,
        }
    else:
        # Paginación para productos reales
        paginator = Paginator(products, 12)
        page_number = request.GET.get('page', 1)
        products_page = paginator.get_page(page_number)

        context = {
            'products': products_page,
            'categories': categories,
            'current_category': current_category,
            'search': search,
            'sort': sort,
        }

    return render(request, 'shop.html', context)


def product_detail(request, product_id):
    """Vista de detalle del producto usando el template product.html existente"""
    product = get_object_or_404(Product, id=product_id, is_active=True)
    related_products = Product.objects.filter(
        category=product.category, 
        is_active=True
    ).exclude(id=product.id)[:4]

    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'product.html', context)


@login_required
def cart(request):
    """Vista del carrito usando el template cart.html existente"""
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.get_total_price() for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total': total,
    }
    return render(request, 'cart.html', context)


@login_required
def checkout(request):
    """Vista de checkout usando el template checkout.html existente"""
    cart_items = CartItem.objects.filter(user=request.user)

    if not cart_items.exists():
        messages.warning(request, 'Tu carrito está vacío.')
        return redirect('cart')

    total = sum(item.get_total_price() for item in cart_items)

    if request.method == 'POST':
        # Procesar la orden
        order = Order.objects.create(
            user=request.user,
            total_amount=total,
            status='pending'
        )

        # Crear los items de la orden
        for cart_item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=cart_item.product,
                quantity=cart_item.quantity,
                price=cart_item.product.price
            )

            # Actualizar stock
            cart_item.product.stock_quantity -= cart_item.quantity
            cart_item.product.save()

        # Limpiar carrito
        cart_items.delete()

        messages.success(request, 'Orden creada exitosamente!')
        return redirect('order_confirmation', order_id=order.id)

    context = {
        'cart_items': cart_items,
        'total': total,
    }
    return render(request, 'checkout.html', context)


@login_required
def order_confirmation(request, order_id):
    """Vista de confirmación de orden"""
    order = get_object_or_404(Order, id=order_id, user=request.user)

    context = {
        'order': order,
    }
    return render(request, 'order_confirmation.html', context)


def blog(request):
    """Vista del blog usando el template blog.html existente"""
    from django.core.paginator import Paginator
    
    posts = BlogPost.objects.filter(is_published=True).order_by('-created_at')
    
    # Si no hay posts reales, crear algunos de muestra
    if not posts.exists():
        sample_posts = []
        for i in range(1, 11):
            from datetime import datetime, timedelta
            sample_posts.append({
                'id': i,
                'title': f'La Historia del Arte Wayuu - Parte {i}',
                'content': f'Este es el contenido del post número {i}. Aquí hablamos sobre la rica tradición de las artesanías Wayuu, sus técnicas ancestrales y la importancia cultural de cada pieza creada por nuestras expertas artesanas.',
                'excerpt': f'Una introducción fascinante a las técnicas tradicionales Wayuu que han sido transmitidas por generaciones...',
                'featured_image': f'https://picsum.photos/400/300?random={i + 200}',
                'author': 'Equipo Raíces Vivas',
                'slug': f'historia-arte-wayuu-{i}',
                'is_published': True,
                'created_at': datetime.now() - timedelta(days=i)
            })
        
        # Crear objetos similares a los del modelo
        class MockPost:
            def __init__(self, data):
                for key, value in data.items():
                    setattr(self, key, value)
        
        posts_list = [MockPost(post) for post in sample_posts]
        
        # Paginación
        paginator = Paginator(posts_list, 6)
        page_number = request.GET.get('page', 1)
        posts = paginator.get_page(page_number)
    else:
        # Paginación para posts reales
        paginator = Paginator(posts, 6)
        page_number = request.GET.get('page', 1)
        posts = paginator.get_page(page_number)

    context = {
        'posts': posts,
    }
    return render(request, 'blog.html', context)


def contact(request):
    """Vista de contacto usando el template contact.html existente"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Crear contacto
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        messages.success(request, 'Mensaje enviado exitosamente. Te contactaremos pronto.')
        return redirect('contact')

    return render(request, 'contact.html')


def login_view(request):
    """Vista de login usando el template login.html existente"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Sesión iniciada exitosamente!')
            return redirect('home')
        else:
            messages.error(request, 'Credenciales inválidas.')

    return render(request, 'login.html')


def register_view(request):
    """Vista de registro usando el template register.html existente"""
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        if password1 != password2:
            messages.error(request, 'Las contraseñas no coinciden.')
            return render(request, 'register.html')

        # Crear usuario
        from .models import User
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1,
                first_name=first_name,
                last_name=last_name
            )
            messages.success(request, 'Usuario creado exitosamente!')
            return redirect('login')
        except Exception as e:
            messages.error(request, 'Error al crear usuario.')

    return render(request, 'register.html')


@login_required
def profile(request):
    """Vista del perfil usando el template profile.html existente"""
    orders = Order.objects.filter(user=request.user).order_by('-created_at')

    context = {
        'orders': orders,
    }
    return render(request, 'profile.html', context)


def logout_view(request):
    """Vista para cerrar sesión"""
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente!')
    return redirect('home')


# AJAX Views para funcionalidad del carrito
@login_required
@csrf_exempt
@require_http_methods(["POST"])
def add_to_cart(request):
    """Agregar producto al carrito via AJAX"""
    data = json.loads(request.body)
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)

    try:
        product = Product.objects.get(id=product_id, is_active=True)
        cart_item, created = CartItem.objects.get_or_create(
            user=request.user,
            product=product,
            defaults={'quantity': quantity}
        )

        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        return JsonResponse({
            'success': True,
            'message': 'Producto agregado al carrito!'
        })
    except Product.DoesNotExist:
        return JsonResponse({
            'success': False,
            'message': 'Producto no encontrado.'
        })


@login_required
@csrf_exempt
@require_http_methods(["POST"])
def update_cart(request):
    """Actualizar cantidad en el carrito via AJAX"""
    data = json.loads(request.body)
    cart_item_id = data.get('cart_item_id')
    quantity = data.get('quantity')

    try:
        cart_item = CartItem.objects.get(id=cart_item_id, user=request.user)
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()

        return JsonResponse({
            'success': True,
            'message': 'Carrito actualizado!'
        })
    except CartItem.DoesNotExist:
        return JsonResponse({
            'success': False,
            'message': 'Item no encontrado.'
        })


@login_required
@csrf_exempt
@require_http_methods(["POST"])
def remove_from_cart(request):
    """Remover producto del carrito via AJAX"""
    data = json.loads(request.body)
    cart_item_id = data.get('cart_item_id')

    try:
        cart_item = CartItem.objects.get(id=cart_item_id, user=request.user)
        cart_item.delete()

        return JsonResponse({
            'success': True,
            'message': 'Producto removido del carrito!'
        })
    except CartItem.DoesNotExist:
        return JsonResponse({
            'success': False,
            'message': 'Item no encontrado.'
        })