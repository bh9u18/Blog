from django.contrib import admin
from .models import Blog,Category

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
	list_display=('blog_name','blog_text','author','date','category')
	list_filter=(['date','category'])
	search_fields=['blog_name','blog_text','author','category']

admin.site.register(Blog,BlogAdmin)
admin.site.register(Category)