from django import template

register = template.Library()


@register.filter('server_items')
def server_items(mod, server):
    return mod.items.filter(server=server)
