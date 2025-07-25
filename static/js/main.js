/* ==============================================
   RAICES VIVAS - MAIN JAVASCRIPT
   Interactive functionality for Wayuu e-commerce
   ============================================== */

document.addEventListener('DOMContentLoaded', function() {
    
    // Initialize all functions
    initStickyNavigation();
    initFloatingNavigation();
    initScrollAnimations();
    initCarousel();
    initFlashMessages();
    initFormValidation();
    initImageZoom();
    initQuantityControls();
    initSearchFunctionality();
    initLoadingStates();
    
    console.log('Raíces Vivas - JavaScript loaded successfully! 🎨');
    console.log('Raíces Vivas - Sistema iniciado correctamente');
});

/* ==============================================
   STICKY NAVIGATION
   ============================================== */
function initStickyNavigation() {
    const navbar = document.getElementById('mainNav');
    if (!navbar) return;
    
    let lastScrollTop = 0;
    const scrollThreshold = 100;
    
    window.addEventListener('scroll', function() {
        const currentScroll = window.pageYOffset || document.documentElement.scrollTop;
        
        // Add scrolled class for styling
        if (currentScroll > scrollThreshold) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
        
        // Hide/show navbar on scroll (optional)
        if (currentScroll > lastScrollTop && currentScroll > scrollThreshold) {
            // Scrolling down
            navbar.style.transform = 'translateY(-100%)';
        } else {
            // Scrolling up
            navbar.style.transform = 'translateY(0)';
        }
        
        lastScrollTop = currentScroll <= 0 ? 0 : currentScroll;
    });
}

/* ==============================================
   FLOATING NAVIGATION (Homepage)
   ============================================== */
function initFloatingNavigation() {
    const floatingNav = document.getElementById('homeNavCapsule');
    if (!floatingNav) return;
    
    let lastScrollTop = 0;
    const showThreshold = 100;
    
    // Show navigation after initial delay
    setTimeout(() => {
        floatingNav.classList.add('visible');
    }, 1000);
    
    window.addEventListener('scroll', function() {
        const currentScroll = window.pageYOffset || document.documentElement.scrollTop;
        
        // Always keep the floating nav visible on homepage
        if (currentScroll > showThreshold) {
            floatingNav.classList.add('visible');
        }
        
        lastScrollTop = currentScroll <= 0 ? 0 : currentScroll;
    });
    
    // Add smooth hover effects to nav icons
    const navIcons = document.querySelectorAll('.nav-icon');
    navIcons.forEach(icon => {
        icon.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px) scale(1.05)';
        });
        
        icon.addEventListener('mouseleave', function() {
            if (!this.classList.contains('active')) {
                this.style.transform = '';
            }
        });
    });
    
    // Enhanced search functionality
    const searchInput = document.querySelector('.search-input');
    const searchContainer = document.querySelector('.search-container');
    
    if (searchInput && searchContainer) {
        searchInput.addEventListener('focus', function() {
            searchContainer.style.transform = 'scale(1.02)';
        });
        
        searchInput.addEventListener('blur', function() {
            searchContainer.style.transform = '';
        });
    }
}

/* ==============================================
   SCROLL ANIMATIONS
   ============================================== */
function initScrollAnimations() {
    const animatedElements = document.querySelectorAll('.animate-on-scroll');
    
    if (animatedElements.length === 0) return;
    
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                // Add staggered animation delay for multiple elements
                const delay = Array.from(animatedElements).indexOf(entry.target) * 100;
                entry.target.style.transitionDelay = `${delay}ms`;
            }
        });
    }, observerOptions);
    
    animatedElements.forEach(element => {
        observer.observe(element);
    });
}

/* ==============================================
   CAROUSEL FUNCTIONALITY
   ============================================== */
function initCarousel() {
    const carousels = document.querySelectorAll('.carousel');
    
    carousels.forEach(carousel => {
        // Auto-play functionality
        const autoPlayInterval = 5000; // 5 seconds
        let autoPlay;
        
        function startAutoPlay() {
            autoPlay = setInterval(() => {
                const nextButton = carousel.querySelector('.carousel-control-next');
                if (nextButton) {
                    nextButton.click();
                }
            }, autoPlayInterval);
        }
        
        function stopAutoPlay() {
            if (autoPlay) {
                clearInterval(autoPlay);
            }
        }
        
        // Start auto-play
        startAutoPlay();
        
        // Pause on hover
        carousel.addEventListener('mouseenter', stopAutoPlay);
        carousel.addEventListener('mouseleave', startAutoPlay);
        
        // Touch/swipe support for mobile
        let startX = null;
        let currentX = null;
        let isDragging = false;
        
        carousel.addEventListener('touchstart', function(e) {
            startX = e.touches[0].clientX;
            isDragging = true;
            stopAutoPlay();
        });
        
        carousel.addEventListener('touchmove', function(e) {
            if (!isDragging) return;
            currentX = e.touches[0].clientX;
        });
        
        carousel.addEventListener('touchend', function(e) {
            if (!isDragging || !startX || !currentX) return;
            
            const diffX = startX - currentX;
            const threshold = 50;
            
            if (Math.abs(diffX) > threshold) {
                if (diffX > 0) {
                    // Swipe left - next slide
                    const nextButton = carousel.querySelector('.carousel-control-next');
                    if (nextButton) nextButton.click();
                } else {
                    // Swipe right - previous slide
                    const prevButton = carousel.querySelector('.carousel-control-prev');
                    if (prevButton) prevButton.click();
                }
            }
            
            startX = null;
            currentX = null;
            isDragging = false;
            startAutoPlay();
        });
    });
}

/* ==============================================
   FLASH MESSAGES
   ============================================== */
function initFlashMessages() {
    const flashMessages = document.querySelectorAll('.alert');
    
    flashMessages.forEach(message => {
        // Auto-dismiss after 5 seconds
        setTimeout(() => {
            if (message && !message.classList.contains('fade')) {
                message.classList.add('fade');
                setTimeout(() => {
                    if (message.parentNode) {
                        message.parentNode.removeChild(message);
                    }
                }, 150);
            }
        }, 5000);
        
        // Add slide-in animation
        message.style.transform = 'translateX(100%)';
        message.style.opacity = '0';
        
        setTimeout(() => {
            message.style.transition = 'all 0.3s ease';
            message.style.transform = 'translateX(0)';
            message.style.opacity = '1';
        }, 100);
    });
}

/* ==============================================
   FORM VALIDATION
   ============================================== */
function initFormValidation() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        const inputs = form.querySelectorAll('input, textarea, select');
        
        inputs.forEach(input => {
            // Real-time validation
            input.addEventListener('blur', function() {
                validateField(this);
            });
            
            input.addEventListener('input', function() {
                // Clear previous error styles on input
                this.classList.remove('is-invalid');
                const errorDiv = this.parentNode.querySelector('.invalid-feedback');
                if (errorDiv) {
                    errorDiv.remove();
                }
            });
        });
        
        // Form submission validation
        form.addEventListener('submit', function(e) {
            let isValid = true;
            
            inputs.forEach(input => {
                if (!validateField(input)) {
                    isValid = false;
                }
            });
            
            if (!isValid) {
                e.preventDefault();
                // Scroll to first error
                const firstError = form.querySelector('.is-invalid');
                if (firstError) {
                    firstError.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    firstError.focus();
                }
            }
        });
    });
}

function validateField(field) {
    const value = field.value.trim();
    const type = field.type;
    const required = field.hasAttribute('required');
    let isValid = true;
    let errorMessage = '';
    
    // Clear previous errors
    field.classList.remove('is-invalid');
    const existingError = field.parentNode.querySelector('.invalid-feedback');
    if (existingError) {
        existingError.remove();
    }
    
    // Required field validation
    if (required && !value) {
        isValid = false;
        errorMessage = 'Este campo es obligatorio.';
    }
    
    // Email validation
    if (type === 'email' && value) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(value)) {
            isValid = false;
            errorMessage = 'Por favor, introduce un email válido.';
        }
    }
    
    // Password validation
    if (type === 'password' && value && value.length < 6) {
        isValid = false;
        errorMessage = 'La contraseña debe tener al menos 6 caracteres.';
    }
    
    // Phone validation
    if (field.name === 'phone' || field.name === 'billing_phone') {
        const phoneRegex = /^[\+]?[0-9\s\-\(\)]{10,}$/;
        if (value && !phoneRegex.test(value)) {
            isValid = false;
            errorMessage = 'Por favor, introduce un número de teléfono válido.';
        }
    }
    
    if (!isValid) {
        field.classList.add('is-invalid');
        const errorDiv = document.createElement('div');
        errorDiv.className = 'invalid-feedback';
        errorDiv.textContent = errorMessage;
        field.parentNode.appendChild(errorDiv);
    }
    
    return isValid;
}

/* ==============================================
   IMAGE ZOOM FUNCTIONALITY
   ============================================== */
function initImageZoom() {
    const productImages = document.querySelectorAll('.product-image img, .main-image img');
    
    productImages.forEach(img => {
        img.addEventListener('click', function() {
            createImageModal(this.src, this.alt);
        });
        
        // Add cursor pointer to indicate clickable
        img.style.cursor = 'pointer';
    });
}

function createImageModal(src, alt) {
    const modal = document.createElement('div');
    modal.className = 'image-modal';
    modal.innerHTML = `
        <div class="image-modal-backdrop">
            <div class="image-modal-content">
                <button class="image-modal-close">&times;</button>
                <img src="${src}" alt="${alt}" class="img-fluid">
            </div>
        </div>
    `;
    
    // Add styles
    modal.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 9999;
        display: flex;
        align-items: center;
        justify-content: center;
    `;
    
    const backdrop = modal.querySelector('.image-modal-backdrop');
    backdrop.style.cssText = `
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.9);
        display: flex;
        align-items: center;
        justify-content: center;
    `;
    
    const content = modal.querySelector('.image-modal-content');
    content.style.cssText = `
        position: relative;
        max-width: 90%;
        max-height: 90%;
    `;
    
    const closeBtn = modal.querySelector('.image-modal-close');
    closeBtn.style.cssText = `
        position: absolute;
        top: -40px;
        right: 0;
        background: none;
        border: none;
        color: white;
        font-size: 2rem;
        cursor: pointer;
        z-index: 1000;
    `;
    
    document.body.appendChild(modal);
    
    // Close functionality
    closeBtn.addEventListener('click', () => modal.remove());
    backdrop.addEventListener('click', (e) => {
        if (e.target === backdrop) modal.remove();
    });
    
    // ESC key to close
    document.addEventListener('keydown', function escHandler(e) {
        if (e.key === 'Escape') {
            modal.remove();
            document.removeEventListener('keydown', escHandler);
        }
    });
}

/* ==============================================
   QUANTITY CONTROLS
   ============================================== */
function initQuantityControls() {
    const quantityInputs = document.querySelectorAll('input[name="quantity"]');
    
    quantityInputs.forEach(input => {
        const minusBtn = input.parentNode.querySelector('button[onclick*="-1"]');
        const plusBtn = input.parentNode.querySelector('button[onclick*="1"]');
        
        if (minusBtn) {
            minusBtn.addEventListener('click', function(e) {
                e.preventDefault();
                const currentValue = parseInt(input.value) || 1;
                const newValue = Math.max(1, currentValue - 1);
                input.value = newValue;
                updateQuantityInCart(input);
            });
        }
        
        if (plusBtn) {
            plusBtn.addEventListener('click', function(e) {
                e.preventDefault();
                const currentValue = parseInt(input.value) || 1;
                const maxValue = parseInt(input.getAttribute('max')) || 99;
                const newValue = Math.min(maxValue, currentValue + 1);
                input.value = newValue;
                updateQuantityInCart(input);
            });
        }
        
        input.addEventListener('change', function() {
            const min = parseInt(this.getAttribute('min')) || 1;
            const max = parseInt(this.getAttribute('max')) || 99;
            let value = parseInt(this.value) || min;
            
            value = Math.max(min, Math.min(max, value));
            this.value = value;
            updateQuantityInCart(this);
        });
    });
}

function updateQuantityInCart(input) {
    // This would typically send an AJAX request to update cart quantity
    // For now, we'll just update the total if it exists
    const cartTable = input.closest('table');
    if (cartTable) {
        updateCartTotals(cartTable);
    }
}

function updateCartTotals(table) {
    let total = 0;
    const rows = table.querySelectorAll('tbody tr');
    
    rows.forEach(row => {
        const priceText = row.querySelector('td:nth-child(2)').textContent;
        const quantityInput = row.querySelector('input[name="quantity"]');
        const subtotalCell = row.querySelector('td:nth-child(4)');
        
        if (priceText && quantityInput && subtotalCell) {
            const price = parseFloat(priceText.replace(/[^\d.]/g, ''));
            const quantity = parseInt(quantityInput.value) || 0;
            const subtotal = price * quantity;
            
            subtotalCell.textContent = `Rs. ${subtotal.toLocaleString()}.00`;
            total += subtotal;
        }
    });
    
    // Update total display
    const totalDisplay = document.querySelector('.cart-summary .h5');
    if (totalDisplay) {
        totalDisplay.textContent = `Rs. ${total.toLocaleString()}.00`;
    }
}

/* ==============================================
   SEARCH FUNCTIONALITY
   ============================================== */
function initSearchFunctionality() {
    const searchForm = document.querySelector('form[action*="shop"]');
    const searchInput = searchForm?.querySelector('input[name="search"]');
    
    if (!searchInput) return;
    
    let searchTimeout;
    
    searchInput.addEventListener('input', function() {
        clearTimeout(searchTimeout);
        
        // Debounce search to avoid too many requests
        searchTimeout = setTimeout(() => {
            if (this.value.length >= 2) {
                performLiveSearch(this.value);
            } else {
                hideLiveSearchResults();
            }
        }, 300);
    });
    
    // Hide results when clicking outside
    document.addEventListener('click', function(e) {
        if (!searchForm.contains(e.target)) {
            hideLiveSearchResults();
        }
    });
}

function performLiveSearch(query) {
    // This would typically make an AJAX request to get search results
    // For now, we'll show a simple dropdown with suggestions
    const searchContainer = document.querySelector('.d-flex.me-3');
    if (!searchContainer) return;
    
    let resultsDiv = searchContainer.querySelector('.search-results');
    if (!resultsDiv) {
        resultsDiv = document.createElement('div');
        resultsDiv.className = 'search-results';
        resultsDiv.style.cssText = `
            position: absolute;
            top: 100%;
            left: 0;
            right: 0;
            background: white;
            border: 1px solid #ddd;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            z-index: 1000;
            max-height: 300px;
            overflow-y: auto;
        `;
        searchContainer.style.position = 'relative';
        searchContainer.appendChild(resultsDiv);
    }
    
    // Mock search results
    const mockResults = [
        { name: 'Mochila Wayuu Tradicional', price: '250,000', url: '/shop' },
        { name: 'Bolso Wayuu Pequeño', price: '180,000', url: '/shop' },
        { name: 'Hamaca Wayuu Doble', price: '450,000', url: '/shop' }
    ].filter(item => 
        item.name.toLowerCase().includes(query.toLowerCase())
    );
    
    if (mockResults.length > 0) {
        resultsDiv.innerHTML = mockResults.map(item => `
            <div class="search-result-item p-2 border-bottom" style="cursor: pointer;">
                <div class="fw-bold">${item.name}</div>
                <div class="text-muted small">Rs. ${item.price}.00</div>
            </div>
        `).join('');
        
        resultsDiv.style.display = 'block';
        
        // Add click handlers
        resultsDiv.querySelectorAll('.search-result-item').forEach(item => {
            item.addEventListener('click', function() {
                window.location.href = '/shop';
            });
            
            item.addEventListener('mouseenter', function() {
                this.style.backgroundColor = '#f8f9fa';
            });
            
            item.addEventListener('mouseleave', function() {
                this.style.backgroundColor = 'white';
            });
        });
    } else {
        resultsDiv.innerHTML = '<div class="p-3 text-muted text-center">No se encontraron productos</div>';
        resultsDiv.style.display = 'block';
    }
}

function hideLiveSearchResults() {
    const resultsDiv = document.querySelector('.search-results');
    if (resultsDiv) {
        resultsDiv.style.display = 'none';
    }
}

/* ==============================================
   LOADING STATES
   ============================================== */
function initLoadingStates() {
    // Add loading states to forms
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function() {
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn && !submitBtn.disabled) {
                const originalText = submitBtn.innerHTML;
                submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Procesando...';
                submitBtn.disabled = true;
                
                // Re-enable after 5 seconds as fallback
                setTimeout(() => {
                    submitBtn.innerHTML = originalText;
                    submitBtn.disabled = false;
                }, 5000);
            }
        });
    });
    
    // Add loading states to AJAX links
    const ajaxLinks = document.querySelectorAll('[data-ajax="true"]');
    
    ajaxLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const originalText = this.innerHTML;
            this.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Cargando...';
            this.style.pointerEvents = 'none';
            
            // Simulate loading
            setTimeout(() => {
                this.innerHTML = originalText;
                this.style.pointerEvents = 'auto';
            }, 2000);
        });
    });
}

/* ==============================================
   UTILITY FUNCTIONS
   ============================================== */

// Smooth scroll to element
function smoothScrollTo(element) {
    if (typeof element === 'string') {
        element = document.querySelector(element);
    }
    
    if (element) {
        element.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
}

// Format currency
function formatCurrency(amount) {
    return `Rs. ${parseFloat(amount).toLocaleString()}.00`;
}

// Show toast notification
function showToast(message, type = 'info') {
    const toast = document.createElement('div');
    toast.className = `alert alert-${type} toast-notification`;
    toast.innerHTML = `
        ${message}
        <button type="button" class="btn-close" onclick="this.parentElement.remove()"></button>
    `;
    
    toast.style.cssText = `
        position: fixed;
        top: 100px;
        right: 20px;
        z-index: 9999;
        min-width: 300px;
        animation: slideInRight 0.3s ease;
    `;
    
    document.body.appendChild(toast);
    
    // Auto-remove after 4 seconds
    setTimeout(() => {
        if (toast.parentNode) {
            toast.style.animation = 'slideOutRight 0.3s ease';
            setTimeout(() => toast.remove(), 300);
        }
    }, 4000);
}

// Add CSS animations for toasts
const style = document.createElement('style');
style.textContent = `
    @keyframes slideInRight {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes slideOutRight {
        from { transform: translateX(0); opacity: 1; }
        to { transform: translateX(100%); opacity: 0; }
    }
`;
document.head.appendChild(style);

// Global error handler
window.addEventListener('error', function(e) {
    console.error('JavaScript Error:', e.error);
    // You could send this to a logging service in production
});

// Global promise rejection handler
window.addEventListener('unhandledrejection', function(e) {
    console.error('Unhandled Promise Rejection:', e.reason);
    // You could send this to a logging service in production
});

console.log('Raíces Vivas - JavaScript loaded successfully! 🎨');
