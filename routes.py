from flask import render_template, request, redirect, url_for, flash, jsonify, session
from flask_login import login_user, logout_user, login_required, current_user
from urllib.parse import urlparse
from app import app, db, login_manager
from models import User, Product, Category, CartItem, Order, OrderItem, BlogPost, Contact
from forms import LoginForm, RegisterForm, ContactForm, CheckoutForm, AddToCartForm
from utils import generate_order_number, format_currency, get_sample_products, get_sample_blog_posts
import logging

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Initialize sample data
# Función para crear datos de ejemplo (para estudiantes)
# Aquí puedes modificar los productos, categorías, etc.
def create_sample_data():
    """Create sample data if database is empty"""
    if Category.query.count() == 0:
        # Create categories
        categories_data = [
            {'name': 'Mochilas', 'description': 'Mochilas tradicionales Wayuu'},
            {'name': 'Bolsos', 'description': 'Bolsos artesanales'},
            {'name': 'Hamacas', 'description': 'Hamacas tejidas a mano'},
            {'name': 'Accesorios', 'description': 'Accesorios únicos'}
        ]
        
        for cat_data in categories_data:
            category = Category()
            category.name = cat_data['name']
            category.description = cat_data['description']
            db.session.add(category)
        
        db.session.commit()
        
        # Create sample products
        sample_products = get_sample_products()
        for product_data in sample_products:
            category = Category.query.filter_by(name=product_data['category']).first()
            if category:
                product = Product()
                product.name = product_data['name']
                product.description = product_data['description']
                product.price = product_data['price']
                product.image_url = product_data['image_url']
                product.category_id = category.id
                product.artisan_name = product_data['artisan_name']
                product.materials = product_data['materials']
                product.colors = product_data['colors']
                product.stock_quantity = 10
                product.is_featured = True
                product.is_active = True
                db.session.add(product)
        
        # Create sample blog posts
        sample_posts = get_sample_blog_posts()
        for post_data in sample_posts:
            post = BlogPost()
            post.title = post_data['title']
            post.slug = post_data['slug']
            post.content = post_data['content']
            post.excerpt = post_data['excerpt']
            post.featured_image = post_data['featured_image']
            post.author = post_data['author']
            post.is_published = True
            db.session.add(post)
        
        db.session.commit()
        logging.info("Sample data created successfully")

@app.route('/')
def index():
    featured_products = Product.query.filter_by(is_featured=True, is_active=True).limit(8).all()
    blog_posts = BlogPost.query.filter_by(is_published=True).limit(3).all()
    
    # Artisan images for carousel
    artisan_images = [
        'https://pixabay.com/get/g4cb61acb2ecb4d9b926cbd249dfc1cd5df755e543ccf124bdf13f138de12c6f6b2ae4a84352b329aa134ec01344cbed0891ba00c065f5fe20faea775e124af09_1280.jpg',
        'https://pixabay.com/get/g6f503c030ef0f1e0b832d891c8dc45caa152bfcfbbca31e85be426a0b51d5795ca9ed21cac265b24d3ecdf4dd2bb7d428bb408f167a6158be69b8963eb97e94c_1280.jpg',
        'https://pixabay.com/get/gd71f9f98ba52cbb79522c47f662a4142cd96cc81246d330f754084d4a08f61208fef9df246cc18af27810cf573047dbce3dee81a092bc6f23e5ab31617c4f6f9_1280.jpg',
        'https://pixabay.com/get/gb24af68db22816c386a486edddf43830063d0fb8cf5695d73d1776f925ccec78d5cde72f8b5f3b67c47fa2ba0d9ccd09a5ac7339c6fcff49b5b1ee962e45fc51_1280.jpg',
        'https://pixabay.com/get/g482d3eee08091e5767da7c26d5a6c7508e3b880d9524356be8735302b665b3ccee568fd0294560f1e18f547c0b9cf5ec395249bc0b7c0910a1dd779cfa45cdda_1280.jpg',
        'https://pixabay.com/get/g8a6a3ba4705484f233cf940e0e2af563e31276cc20f6a43ac625e0386ba52b2998b5b7a8242328a1396b60e856fcae63e52cd086ccbbb604b6815029cc512dcf_1280.jpg'
    ]
    
    return render_template('index.html', 
                         featured_products=featured_products,
                         blog_posts=blog_posts,
                         artisan_images=artisan_images)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or urlparse(next_page).netloc != '':
                next_page = url_for('index')
            flash('¡Bienvenido de nuevo!', 'success')
            return redirect(next_page)
        flash('Correo electrónico o contraseña incorrectos', 'error')
    
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = RegisterForm()
    if form.validate_on_submit():
        user = User()
        user.username = form.username.data
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data
        user.email = form.email.data
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('¡Registro exitoso! Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión exitosamente.', 'info')
    return redirect(url_for('index'))

@app.route('/shop')
def shop():
    page = request.args.get('page', 1, type=int)
    category_id = request.args.get('category', type=int)
    search = request.args.get('search', '')
    
    query = Product.query.filter_by(is_active=True)
    
    if category_id:
        query = query.filter_by(category_id=category_id)
    
    if search:
        query = query.filter(Product.name.contains(search))
    
    products = query.paginate(
        page=page, per_page=12, error_out=False
    )
    
    categories = Category.query.all()
    
    return render_template('shop.html', 
                         products=products, 
                         categories=categories,
                         current_category=category_id,
                         search=search)

@app.route('/product/<int:id>')
def product_detail(id):
    product = Product.query.get_or_404(id)
    related_products = Product.query.filter(
        Product.category_id == product.category_id,
        Product.id != product.id,
        Product.is_active == True
    ).limit(4).all()
    
    form = AddToCartForm()
    if product.colors:
        form.selected_color.choices = [(color, color) for color in product.colors]
    
    return render_template('product.html', 
                         product=product, 
                         related_products=related_products,
                         form=form)

@app.route('/add_to_cart', methods=['POST'])
@login_required
def add_to_cart():
    form = AddToCartForm()
    if form.validate_on_submit():
        product_id = form.product_id.data
        quantity = form.quantity.data
        selected_color = form.selected_color.data if form.selected_color.data else None
        
        # Check if item already exists in cart
        existing_item = CartItem.query.filter_by(
            user_id=current_user.id,
            product_id=product_id,
            selected_color=selected_color
        ).first()
        
        if existing_item:
            existing_item.quantity += quantity
        else:
            cart_item = CartItem()
            cart_item.user_id = current_user.id
            cart_item.product_id = product_id
            cart_item.quantity = quantity
            cart_item.selected_color = selected_color
            db.session.add(cart_item)
        
        db.session.commit()
        flash('Producto agregado al carrito', 'success')
    
    return redirect(request.referrer or url_for('shop'))

@app.route('/cart')
@login_required
def cart():
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    total = current_user.get_cart_total()
    return render_template('cart.html', cart_items=cart_items, total=total)

@app.route('/update_cart', methods=['POST'])
@login_required
def update_cart():
    item_id = request.form.get('item_id', type=int)
    quantity = request.form.get('quantity', type=int)
    
    if quantity <= 0:
        return remove_from_cart()
    
    cart_item = CartItem.query.filter_by(id=item_id, user_id=current_user.id).first()
    if cart_item:
        cart_item.quantity = quantity
        db.session.commit()
        flash('Carrito actualizado', 'success')
    
    return redirect(url_for('cart'))

@app.route('/remove_from_cart', methods=['POST'])
@login_required
def remove_from_cart():
    item_id = request.form.get('item_id', type=int)
    cart_item = CartItem.query.filter_by(id=item_id, user_id=current_user.id).first()
    
    if cart_item:
        db.session.delete(cart_item)
        db.session.commit()
        flash('Producto eliminado del carrito', 'success')
    
    return redirect(url_for('cart'))

@app.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    if not cart_items:
        flash('Tu carrito está vacío', 'warning')
        return redirect(url_for('cart'))
    
    form = CheckoutForm()
    total = current_user.get_cart_total()
    
    # Pre-populate form with user data
    if request.method == 'GET':
        form.billing_first_name.data = current_user.first_name
        form.billing_last_name.data = current_user.last_name
        form.billing_email.data = current_user.email
        if current_user.phone:
            form.billing_phone.data = current_user.phone
        if current_user.address:
            form.billing_address.data = current_user.address
        if current_user.city:
            form.billing_city.data = current_user.city
        if current_user.country:
            form.billing_country.data = current_user.country
    
    if form.validate_on_submit():
        # Create order
        order = Order()
        order.user_id = current_user.id
        order.order_number = generate_order_number()
        order.total_amount = total
        order.billing_first_name = form.billing_first_name.data
        order.billing_last_name = form.billing_last_name.data
        order.billing_email = form.billing_email.data
        order.billing_phone = form.billing_phone.data
        order.billing_address = form.billing_address.data
        order.billing_city = form.billing_city.data
        order.billing_country = form.billing_country.data
        order.billing_postal_code = form.billing_postal_code.data
        order.payment_method = form.payment_method.data
        
        db.session.add(order)
        db.session.flush()  # Get the order ID
        
        # Create order items
        for cart_item in cart_items:
            order_item = OrderItem()
            order_item.order_id = order.id
            order_item.product_id = cart_item.product_id
            order_item.quantity = cart_item.quantity
            order_item.price = cart_item.product.price
            order_item.selected_color = cart_item.selected_color
            db.session.add(order_item)
        
        # Clear cart
        for cart_item in cart_items:
            db.session.delete(cart_item)
        
        db.session.commit()
        
        flash(f'¡Pedido realizado exitosamente! Número de orden: {order.order_number}', 'success')
        return redirect(url_for('order_confirmation', order_number=order.order_number))
    
    return render_template('checkout.html', form=form, cart_items=cart_items, total=total)

@app.route('/order/<order_number>')
@login_required
def order_confirmation(order_number):
    order = Order.query.filter_by(order_number=order_number, user_id=current_user.id).first_or_404()
    return render_template('order_confirmation.html', order=order)

@app.route('/nosotros')
@app.route('/blog')
def blog():
    page = request.args.get('page', 1, type=int)
    posts = BlogPost.query.filter_by(is_published=True).paginate(
        page=page, per_page=6, error_out=False
    )
    return render_template('blog.html', posts=posts)

@app.route('/blog/<slug>')
def blog_post(slug):
    post = BlogPost.query.filter_by(slug=slug, is_published=True).first_or_404()
    return render_template('blog_post.html', post=post)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        contact = Contact()
        contact.name = form.name.data
        contact.email = form.email.data
        contact.subject = form.subject.data
        contact.message = form.message.data
        db.session.add(contact)
        db.session.commit()
        flash('¡Gracias por tu mensaje! Te responderemos pronto.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html', form=form)

@app.route('/profile')
@login_required
def profile():
    orders = Order.query.filter_by(user_id=current_user.id).order_by(Order.created_at.desc()).all()
    return render_template('profile.html', orders=orders)

# Template context processors
@app.context_processor
def inject_cart_count():
    if current_user.is_authenticated:
        return dict(cart_count=current_user.get_cart_count())
    return dict(cart_count=0)

@app.context_processor
def utility_processor():
    return dict(format_currency=format_currency)

# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
