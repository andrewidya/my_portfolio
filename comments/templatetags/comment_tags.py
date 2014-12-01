from django import template

register = template.Library()

@register.inclusion_tag('comments/comment_list')