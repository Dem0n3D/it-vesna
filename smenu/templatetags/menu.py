from django import template

from operator import attrgetter

from ..models import Menu, Node

register = template.Library()

@register.inclusion_tag("menu.html")
def menu(name):
    return {
        "childrens": sorted(Menu.objects.filter(name=name)[0].node.childrens.all(), key=attrgetter("order"))
    }

@register.inclusion_tag("node.html")
def node(node):
    return {
        "has_childrens": len(node.childrens.all()) > 0,
        "childrens": sorted(node.childrens.all(), key=attrgetter("order")),
        "title": node.title,
        "url": node.url
    }
