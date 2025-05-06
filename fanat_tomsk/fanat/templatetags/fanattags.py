from django import template
import fanat.views as views


register = template.Library()


@register.simple_tag()
def get_coach():
	return views.db_coach