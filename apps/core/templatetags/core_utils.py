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
