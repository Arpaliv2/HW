from django import template
from data_base.models import Category
from django.contrib.auth.models import User

register = template.Library()

@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
   d = context['request'].GET.copy()
   for k, v in kwargs.items():
       d[k] = v
   return d.urlencode()

@register.simple_tag
def subscribe(category, user):
    cat = Category.objects.get(name=category)
    new_subscribe=cat.subscribers.add(user)