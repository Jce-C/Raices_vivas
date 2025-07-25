
import React, { createContext, useContext, useState, useEffect } from 'react';
import api from '../services/api';
import { useAuth } from './AuthContext';

const CartContext = createContext();

export const useCart = () => {
  const context = useContext(CartContext);
  if (!context) {
    throw new Error('useCart debe usarse dentro de CartProvider');
  }
  return context;
};

export const CartProvider = ({ children }) => {
  const [cartItems, setCartItems] = useState([]);
  const [loading, setLoading] = useState(false);
  const { isAuthenticated } = useAuth();

  useEffect(() => {
    if (isAuthenticated) {
      loadCart();
    } else {
      setCartItems([]);
    }
  }, [isAuthenticated]);

  const loadCart = async () => {
    if (!isAuthenticated) return;
    
    setLoading(true);
    try {
      const response = await api.get('/cart/');
      setCartItems(response.data.results || response.data);
    } catch (error) {
      console.error('Error cargando carrito:', error);
    } finally {
      setLoading(false);
    }
  };

  const addToCart = async (productId, quantity = 1, selectedColor = null) => {
    if (!isAuthenticated) {
      alert('Debes iniciar sesión para agregar productos al carrito');
      return { success: false };
    }

    try {
      await api.post('/cart/', {
        product: productId,
        quantity,
        selected_color: selectedColor
      });
      
      await loadCart();
      return { success: true };
    } catch (error) {
      console.error('Error agregando al carrito:', error);
      return {
        success: false,
        error: error.response?.data?.detail || 'Error agregando al carrito'
      };
    }
  };

  const updateCartItem = async (itemId, quantity) => {
    try {
      await api.patch(`/cart/${itemId}/`, { quantity });
      await loadCart();
      return { success: true };
    } catch (error) {
      console.error('Error actualizando carrito:', error);
      return { success: false };
    }
  };

  const removeFromCart = async (itemId) => {
    try {
      await api.delete(`/cart/${itemId}/`);
      await loadCart();
      return { success: true };
    } catch (error) {
      console.error('Error eliminando del carrito:', error);
      return { success: false };
    }
  };

  const clearCart = async () => {
    try {
      await api.delete('/cart/clear/');
      setCartItems([]);
      return { success: true };
    } catch (error) {
      console.error('Error vaciando carrito:', error);
      return { success: false };
    }
  };

  const getCartTotal = () => {
    return cartItems.reduce((total, item) => total + item.total_price, 0);
  };

  const getCartCount = () => {
    return cartItems.reduce((total, item) => total + item.quantity, 0);
  };

  const value = {
    cartItems,
    loading,
    addToCart,
    updateCartItem,
    removeFromCart,
    clearCart,
    loadCart,
    getCartTotal,
    getCartCount
  };

  return (
    <CartContext.Provider value={value}>
      {children}
    </CartContext.Provider>
  );
};
