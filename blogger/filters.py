import django_filters
from .models import *
from django import forms

class BlogFilter(django_filters.FilterSet):
	"""category = django_filters.ModelMultipleChoiceFilter(queryset=Blog.objects.order_by().values_list('category',flat=True).distinct(),
        widget=forms.CheckboxSelectMultiple)"""
	class Meta:
		model = Blog
		fields={
				'category': ['icontains'],		
				'blog_name':['icontains'],
				'blog_text':['icontains'],
				}