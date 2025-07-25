
import axios from 'axios';

// Configuración base de la API
const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:3000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Interceptor para agregar el token automáticamente
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Token ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Interceptor para manejar errores de respuesta
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Token expirado o inválido
      localStorage.removeItem('token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

// Servicios específicos
export const authService = {
  login: (credentials) => api.post('/auth/login/', credentials),
  register: (userData) => api.post('/auth/register/', userData),
  logout: () => api.post('/auth/logout/'),
  getProfile: () => api.get('/auth/profile/'),
};

export const productService = {
  getProducts: (params) => api.get('/products/', { params }),
  getProduct: (id) => api.get(`/products/${id}/`),
  getFeaturedProducts: () => api.get('/products/featured/'),
};

export const categoryService = {
  getCategories: () => api.get('/categories/'),
  getCategory: (id) => api.get(`/categories/${id}/`),
};

export const cartService = {
  getCart: () => api.get('/cart/'),
  addToCart: (data) => api.post('/cart/', data),
  updateCartItem: (id, data) => api.patch(`/cart/${id}/`, data),
  removeFromCart: (id) => api.delete(`/cart/${id}/`),
  clearCart: () => api.delete('/cart/clear/'),
};

export const orderService = {
  getOrders: () => api.get('/orders/'),
  createOrder: (data) => api.post('/orders/', data),
  getOrder: (id) => api.get(`/orders/${id}/`),
};

export const blogService = {
  getPosts: (params) => api.get('/blog/', { params }),
  getPost: (slug) => api.get(`/blog/${slug}/`),
};

export const contactService = {
  sendMessage: (data) => api.post('/contact/', data),
};

export default api;
