from django.db import models
from django.urls import reverse
import django
from django.contrib.auth.models import User
from django.http import HttpResponse 

# Create your models here.
class Category(models.Model):
	name=models.CharField(max_length=250)
	
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('blogger:index')
 

class Blog(models.Model):
	
	blog_name=models.CharField(max_length=100)
	author=models.ForeignKey(User,on_delete=models.CASCADE,null="true")
	date=models.DateTimeField(default=django.utils.timezone.now())
	blog_text=models.TextField()
	category=models.CharField(max_length=250,default='uncategorized')

	def __str__(self):
		return self.blog_name

	def publish_date(self):
		return date
	def get_absolute_url(self):
		return reverse('blogger:index')
