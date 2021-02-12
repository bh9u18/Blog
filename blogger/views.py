from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.forms import inlineformset_factory
from django.urls import reverse,reverse_lazy
from django.views import generic
from .models import Blog, Category
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, BlogForm,UpdateBlogForm
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .filters import BlogFilter
# Create your views here.
	
"""def search(request):
    query = request.GET['query']
    if len(query)>78:
        allBlogs = Blogs.object.none()
    else:
        allBlogTitle = Blog.objects.filter(title__icontains=query)
        allBolgsContent = Blog.objects.filter(content__icontains=query)
        allBlogs = allBlogsTitle.union(allBlogsContent)
    if allBlogs.count == 0:
            messages.warning(request, "No search result found. please rechcek your input")
    params = {'allBlogs': allBlogs, 'query':query}
    return render(request, 'blogger/search.html',params)
"""
class IndexView(generic.ListView):
	template_name='blogger/index.html'
	model=Blog
	ordering=['-date']
	paginate_by=5

	def get_context_data(self,**kwargs):
		context=super().get_context_data(**kwargs)
		context['filter']=BlogFilter(self.request.GET,queryset=self.get_queryset())
		return context

	
class DetailView(generic.DetailView):
	model=Blog
	template_name='blogger/details.html'

def registeration(request):
	form=CreateUserForm()

	if request.method == 'POST':
		form=CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user=form.cleaned_data.get('username')
			messages.success(request,'Congratulations! Account is created for ' + user)
			return redirect('/blogger/login')

	context={'form':form}
	return render(request,'blogger/registeration.html',context)
	
def login(request):

	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')

		user=authenticate(request,username=username, password=password)

		if user is not None:
			auth_login(request,user)
			return redirect('/blogger')
		else:
			messages.info(request,"Username or password is incorrect")

	context={}
	return render(request,'blogger/login.html',context)

def CategoryView(request,cats):

	category_blogs=Blog.objects.filter(category=cats)
	return render(request,'blogger/categories.html',{'cats':cats,'category_posts':category_blogs})

@login_required(login_url='/blogger/login')
def logout(request):
	auth_logout(request)
	return redirect('/blogger/login')

@login_required(login_url='/blogger/login')
def myblogs(request):
	blogs=Blog.objects.filter(author=request.user).order_by('-date')
	context={'blogs':blogs}
	return render(request,'blogger/myblogs.html',context)
	
@method_decorator(login_required, name='dispatch')
class AddblogView(generic.CreateView):
	model = Blog
	form_class=BlogForm
	
	template_name = 'blogger/addblog.html'
	
	def get(self,request,*args,**kwargs):
		form=self.form_class(initial={'author':request.user})
		return render(request,self.template_name,{'form':form})

	def post(self,request,*args,**kwargs):
		form=self.form_class(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/blogger')
		return render(request,self.template_name,{'form':form})

@method_decorator(login_required, name='dispatch')
class AddcategoryView(generic.CreateView):
	model = Category
	fields='__all__'
	template_name = 'blogger/addcategory.html'

@method_decorator(login_required, name='dispatch')
class UpdateBlogView(generic.UpdateView):
	model=Blog
	form_class=UpdateBlogForm
	template_name='blogger/editblog.html'
	

@method_decorator(login_required, name='dispatch')
class DeleteBlogView(generic.DeleteView):
	model=Blog
	template_name='blogger/deleteblog.html'
	success_url=reverse_lazy('blogger:index')


"""
@method_decorator(login_required, name='dispatch')
class myblogsIndexView(generic.ListView):
	template_name='blogger/myblogs.html'
	context_object_name='users_latest_blog_list'
	paginate_by=5
	
	def get_username(request):
		username = Anonymous
		if request.user.is_authenticated():
			username= self.request.user
		return username
	
	def get_queryset(self):
		uname=get_username(request)
		return Blog.objects.filter(username=uname).order_by('-date')
"""

#registeration
"""if request.method == 'POST': 
		
		first_name = request.POST.get('firstName')
		last_name = request.POST.get('lastName')
		username = request.POST.get('userName')
		email = request.POST.get('inputEmail3')
		password=request.POST.get('inputPassword3')
		password1=request.POST.get('inputPassword4')
		if password1==password:
			if User.objects.filter(email = email).exists():
				messages.info(request,'Email Taken')
				return redirect('registeration')
			elif User.objects.filter(username=username).exists():
				messages.info(request,'Username Taken')
				return redirect('registeration')
			else:
				user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
				user.save()
				print("user")
				return redirect('login')
		else:
			messages.info(request,"Password don't match!")
			return rediect('registeration')
	else:
		return render(request,'blogger/registeration.html')
"""