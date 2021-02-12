from django.forms import ModelForm
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Blog,Category

choices=Category.objects.all().values_list('name','name')
cats=[]
for i in choices:
	cats.append(i)

class CreateUserForm(UserCreationForm):
	"""docstring for CreateUserForm"""
	class Meta:
		model = User
		fields=['username','email','password1','password2']

class BlogForm(forms.ModelForm):
	class Meta:
		model=Blog
		fields=('blog_name','date','author','category','blog_text')
		
		widgets={
			'blog_name':forms.TextInput(attrs={'class':'form-control'}),
			'date':forms.DateTimeInput(attrs={'class':'form-control'}),
			'author':forms.Select(attrs={'class':'form-control'}),
			'category':forms.Select(choices=cats,attrs={'class':'form-control'}),
			'blog_text':forms.Textarea(attrs={'class':'form-control'})
		}

class UpdateBlogForm(forms.ModelForm):
	class Meta:
		model=Blog
		fields=('blog_name','date','category','blog_text')

		widgets={
			'blog_name':forms.TextInput(attrs={'class':'form-control'}),
			'date':forms.DateTimeInput(attrs={'class':'form-control'}),
			'category':forms.Select(choices=cats,attrs={'class':'form-control'}),
			'blog_text':forms.Textarea(attrs={'class':'form-control'})
		}