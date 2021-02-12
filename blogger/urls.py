from django.urls import path
from . import views

app_name='blogger'
urlpatterns=[
	path('',views.IndexView.as_view(),name='index'),
	path('registeration/',views.registeration,name='registeration'),
	path('<int:pk>/',views.DetailView.as_view(),name='details'),
	path('login/',views.login,name='login'),
	path('logout/',views.logout,name='logout'),
	path('myblogs/',views.myblogs,name='myblogs'),
	path('addblog/',views.AddblogView.as_view(),name='addblog'),
	path('<int:pk>/edit/',views.UpdateBlogView.as_view(),name='editblog'),
	path('<int:pk>/delete/',views.DeleteBlogView.as_view(),name='deleteblog'),
	path('addcategory/',views.AddcategoryView.as_view(),name='addcategory'),
	path('category/<str:cats>/',views.CategoryView,name='category'),
	#path('search/<slug:query>/',views.search,name='search')
	]