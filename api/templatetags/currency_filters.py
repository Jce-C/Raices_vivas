"""
Template filters for currency formatting
"""
from django import template
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()


@register.filter
def currency_symbol(value):
    """
    Format a price with Colombian peso symbol and thousand separators
    """
    try:
        # Convert to float and format with thousand separators
        formatted_price = intcomma(int(float(value)))
        return f"${formatted_price} COP"
    except (ValueError, TypeError):
        return value

@register.filter
def currency(value):
    """Format a number as Colombian Peso currency"""
    if value is None:
        return "$0"

    try:
        # Convert to float if it's a Decimal
        value = float(value)
        # Format with thousands separator and add peso sign
        return f"${intcomma(int(value))}"
    except (ValueError, TypeError):
        return "$0"


@register.filter
def multiply(value, arg):
    """Multiply two values"""
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0