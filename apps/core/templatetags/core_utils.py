from django.utils import timezone
from django import template

register = template.Library()


@register.filter
def make_list(value):
    """
    A filter that converts a number into a list of numbers.
    Usage:
        {% for i in 5|make_list %}
        <li>Item {{ i }}</li>
        {% endfor %}
    """
    return list(range(value))


@register.filter
def received_time(value):
    """
    A filter to return time if data was created today or date if otherwise
    Usage:
        {{ message.received_time|received_time }}
    """
    now = timezone.now()
    if value.date() == now.date():
        return value.strftime("%I:%M %p")
    else:
        return value.strftime("%b %d")


@register.filter
def shorten_text(value, length=200, ellipsis='...'):
    """Shorten a long text to a specified number of characters."""
    if len(value) > length:
        return value[:length-len(ellipsis)] + ellipsis
    return value
