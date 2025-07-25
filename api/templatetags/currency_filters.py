
from django import template
from decimal import Decimal

register = template.Library()

@register.filter
def format_currency(value):
    """Format currency in Colombian Pesos"""
    try:
        amount = Decimal(str(value))
        return f"${amount:,.0f} COP"
    except (ValueError, TypeError):
        return f"${value}"

@register.filter
def currency_symbol(value):
    """Simple currency formatting with just dollar sign"""
    try:
        amount = Decimal(str(value))
        return f"${amount:,.0f}"
    except (ValueError, TypeError):
        return f"${value}"
