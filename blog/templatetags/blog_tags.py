from django import template
from blog.models import Category

register = template.Library()

@register.simple_tag
def hello():
    return "hello mehdi nova"
