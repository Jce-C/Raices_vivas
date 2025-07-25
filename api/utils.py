"""
Utility functions for the Wayuu Artesania API
"""
import random
import string
from datetime import datetime


def generate_order_number():
    """Generate a unique order number"""
    timestamp = datetime.now().strftime('%Y%m%d')
    random_part = ''.join(random.choices(string.digits, k=4))
    return f"WA{timestamp}{random_part}"