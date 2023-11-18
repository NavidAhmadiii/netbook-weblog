from django import template
from ..models import Category

register = template.Library()


@register.simple_tag
def title():
    return "به وبلاگ نت بوک خوش امدید"


@register.inclusion_tag("partials/category_navbar.html")
def category_navbar():
    return {
        "category": Category.objects.filter(status=True)

    }
