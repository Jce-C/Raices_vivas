from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.utils.text import slugify
from django.db.models import Q
from .models import User, Product, Category, BlogPost, CartItem, Order
from django.core.paginator import Paginator


def home(request):
    """Home page view"""
    featured_products = Product.objects.filter(is_featured=True, is_active=True)[:6]
    recent_posts = BlogPost.objects.filter(is_published=True, is_recent_post=True)[:3]

    context = {
        'featured_products': featured_products,
        'blog_posts': recent_posts,
    }
    return render(request, 'index.html', context)


def shop(request):
    """Shop page with products listing"""
    products = Product.objects.filter(is_active=True)
    categories = Category.objects.filter(is_active=True)

    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) | 
            Q(description__icontains=search_query)
        )

    # Category filter
    category_id = request.GET.get('category')
    if category_id:
        products = products.filter(category_id=category_id)

    # Sorting
    sort_by = request.GET.get('sort', '')
    if sort_by == 'price_asc':
        products = products.order_by('price')
    elif sort_by == 'price_desc':
        products = products.order_by('-price')
    elif sort_by == 'name_asc':
        products = products.order_by('name')
    elif sort_by == 'name_desc':
        products = products.order_by('-name')
    else:
        products = products.order_by('-created_at')

    # Pagination
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,
        'page_obj': page_obj,
        'categories': categories,
        'search_query': search_query,
        'current_category': int(category_id) if category_id else None,
        'search': search_query,
        'sort_by': sort_by,
    }
    return render(request, 'shop.html', context)


def product_detail(request, product_id):
    """Individual product page"""
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


def blog(request):
    """Blog page"""
    posts = BlogPost.objects.filter(is_published=True).order_by('-created_at')
    recent_posts = BlogPost.objects.filter(is_published=True, is_recent_post=True)[:5]
    featured_products = Product.objects.filter(is_featured=True, is_active=True)[:3]

    # Pagination
    paginator = Paginator(posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'recent_posts': recent_posts,
        'featured_products': featured_products,
    }
    return render(request, 'blog.html', context)


def contact(request):
    """Contact page"""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Here you would typically save to database or send email
        messages.success(request, 'Gracias por tu mensaje. Te contactaremos pronto.')
        return redirect('contact')

    return render(request, 'contact.html')


def login_view(request):
    """User login view"""
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'home')
            messages.success(request, f'¡Bienvenido de vuelta, {user.first_name}!')
            return redirect(next_url)
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, 'login.html')


def register_view(request):
    """User registration view"""
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Basic validation
        if password1 != password2:
            messages.error(request, 'Las contraseñas no coinciden.')
            return render(request, 'register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya existe.')
            return render(request, 'register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'El email ya está registrado.')
            return render(request, 'register.html')

        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password1
        )

        messages.success(request, '¡Cuenta creada exitosamente! Ya puedes iniciar sesión.')
        return redirect('login')

    return render(request, 'register.html')


def logout_view(request):
    """User logout view"""
    logout(request)
    messages.success(request, 'Has cerrado sesión exitosamente.')
    return redirect('home')


@login_required
def profile(request):
    """User profile page"""
    orders = Order.objects.filter(user=request.user).order_by('-created_at')[:5]

    context = {
        'orders': orders,
    }
    return render(request, 'profile.html', context)


@login_required
def cart(request):
    """Shopping cart page"""
    cart_items = CartItem.objects.filter(user=request.user)

    context = {
        'cart_items': cart_items,
    }
    return render(request, 'cart.html', context)


@login_required
def checkout(request):
    """Checkout page"""
    cart_items = CartItem.objects.filter(user=request.user)

    if not cart_items.exists():
        messages.warning(request, 'Tu carrito está vacío.')
        return redirect('cart')

    if request.method == 'POST':
        # Process checkout logic here
        messages.success(request, 'Pedido realizado exitosamente.')
        return redirect('profile')

    context = {
        'cart_items': cart_items,
    }
    return render(request, 'checkout.html', context)


def is_staff_user(user):
    """Check if user is staff"""
    return user.is_authenticated and user.is_staff


@user_passes_test(is_staff_user)
def admin_add_product(request):
    """Admin view to add products"""
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image_url = request.POST.get('image_url')
        category_id = request.POST.get('category')
        stock_quantity = request.POST.get('stock_quantity', 0)
        artisan_name = request.POST.get('artisan_name', '')
        materials = request.POST.get('materials', '')
        dimensions = request.POST.get('dimensions', '')
        weight = request.POST.get('weight', '')
        is_featured = request.POST.get('is_featured') == 'on'

        try:
            category = Category.objects.get(id=category_id)
            product = Product.objects.create(
                name=name,
                description=description,
                price=price,
                image_url=image_url,
                category=category,
                stock_quantity=int(stock_quantity),
                artisan_name=artisan_name,
                materials=materials,
                dimensions=dimensions,
                weight=weight,
                is_featured=is_featured
            )
            messages.success(request, f'Producto "{product.name}" agregado exitosamente.')
            return redirect('admin_add_product')
        except Exception as e:
            messages.error(request, f'Error al agregar producto: {str(e)}')

    categories = Category.objects.filter(is_active=True)
    context = {
        'categories': categories,
    }
    return render(request, 'admin_add_product.html', context)


@user_passes_test(is_staff_user)
def admin_add_blog_post(request):
    """Admin view to add blog posts"""
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        excerpt = request.POST.get('excerpt', '')
        featured_image = request.POST.get('featured_image', '')
        author = request.POST.get('author')
        is_published = request.POST.get('is_published') == 'on'
        is_recent_post = request.POST.get('is_recent_post') == 'on'

        try:
            # Generate slug from title
            slug = slugify(title)

            # Ensure unique slug
            original_slug = slug
            counter = 1
            while BlogPost.objects.filter(slug=slug).exists():
                slug = f"{original_slug}-{counter}"
                counter += 1

            blog_post = BlogPost.objects.create(
                title=title,
                slug=slug,
                content=content,
                excerpt=excerpt,
                featured_image=featured_image,
                author=author,
                is_published=is_published,
                is_recent_post=is_recent_post
            )
            messages.success(request, f'Post "{blog_post.title}" agregado exitosamente.')
            return redirect('admin_add_blog_post')
        except Exception as e:
            messages.error(request, f'Error al agregar post: {str(e)}')

    return render(request, 'admin_add_blog_post.html')