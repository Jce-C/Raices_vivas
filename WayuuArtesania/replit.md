# Raíces Vivas - Wayuu E-commerce Platform

## Overview

Raíces Vivas is a Flask-based e-commerce platform showcasing authentic Wayuu artisan crafts from La Guajira, Colombia. The application promotes cultural heritage while providing a modern shopping experience for traditional handicrafts including bags, hammocks, and accessories.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Backend Architecture
- **Framework**: Flask (Python web framework)
- **Database ORM**: SQLAlchemy with Flask-SQLAlchemy extension
- **Authentication**: Flask-Login for user session management
- **Forms**: WTForms with Flask-WTF for form handling and validation
- **Security**: Werkzeug for password hashing and security utilities

### Frontend Architecture
- **Templates**: Jinja2 templating engine with Flask
- **CSS Framework**: Bootstrap 5.3.0 for responsive design
- **Icons**: Font Awesome 6.4.0 for iconography
- **Fonts**: Google Fonts (Playfair Display + Poppins)
- **JavaScript**: Vanilla JavaScript for interactive functionality

### Database Design
- **Base Class**: SQLAlchemy DeclarativeBase for model definitions
- **User Management**: User model with authentication and profile data
- **Product Catalog**: Product, Category models for inventory
- **Shopping System**: Cart, Order, OrderItem models for e-commerce
- **Content Management**: BlogPost, Contact models for content

## Key Components

### User Authentication System
- Registration and login functionality with email validation
- Password hashing using Werkzeug security
- Session management with Flask-Login
- User profile management with order history

### E-commerce Core
- Product catalog with categories and detailed descriptions
- Shopping cart functionality with quantity management
- Checkout process with billing information collection
- Order management and confirmation system
- Inventory tracking with stock quantities

### Content Management
- Blog system for cultural stories and artisan features
- Contact form for customer inquiries
- Static page management for about/info content
- Image management for product galleries

### Cultural Integration
- Wayuu-inspired color palette and design elements
- Spanish language interface reflecting target market
- Artisan attribution for each product
- Cultural storytelling through product descriptions

## Data Flow

### User Journey
1. **Browse** → Category/product listing with filtering
2. **View** → Detailed product pages with artisan information
3. **Cart** → Add items with quantity selection
4. **Checkout** → Billing information and payment processing
5. **Confirmation** → Order summary and tracking information

### Admin Operations
1. **Inventory** → Product and category management
2. **Orders** → Order processing and fulfillment
3. **Content** → Blog posts and cultural content updates
4. **Users** → Customer account management

### Data Models Relationships
- Users → Orders (one-to-many)
- Users → CartItems (one-to-many)
- Categories → Products (one-to-many)
- Orders → OrderItems (one-to-many)
- Products → CartItems (one-to-many)

## External Dependencies

### Frontend Libraries
- **Bootstrap 5.3.0**: Responsive UI components and grid system
- **Font Awesome 6.4.0**: Icon library for visual elements
- **Google Fonts**: Typography (Playfair Display, Poppins)

### Backend Packages
- **Flask**: Core web framework
- **Flask-SQLAlchemy**: Database ORM integration
- **Flask-Login**: User session management
- **Flask-WTF**: Form handling and CSRF protection
- **WTForms**: Form validation and rendering
- **Werkzeug**: WSGI utilities and security functions

### Database
- **PostgreSQL**: Primary database (configurable via DATABASE_URL)
- **SQLAlchemy**: ORM with connection pooling and optimization

## Deployment Strategy

### Environment Configuration
- **Development**: Local SQLite fallback with debug mode
- **Production**: PostgreSQL with environment-based configuration
- **Session Management**: Configurable secret key via SESSION_SECRET
- **Database URL**: Flexible connection via DATABASE_URL environment variable

### Application Structure
- **Entry Point**: main.py for development server
- **Application Factory**: create_app() pattern for configuration
- **Proxy Support**: ProxyFix middleware for deployment behind reverse proxy
- **Database Initialization**: Automatic table creation with sample data

### Static Assets
- **CSS**: Custom Wayuu-themed styling in static/css/
- **JavaScript**: Interactive functionality in static/js/
- **Images**: Product and cultural imagery via external URLs
- **Templates**: Organized Jinja2 templates with inheritance

### Error Handling
- Custom 404 and 500 error pages with brand consistency
- Flash message system for user feedback
- Form validation with localized Spanish messages
- Logging configuration for debugging and monitoring

The application follows Flask best practices with modular organization, making it easy to extend with additional features like payment processing, inventory management, or multi-language support.