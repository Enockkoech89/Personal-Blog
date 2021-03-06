from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
urlpatterns = [
	path('', PostListView.as_view(), name='home'),
	path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
	path('post/new/', PostCreateView.as_view(template_name='post_form.html'), name='post-create'),
	path('post/<int:pk>/update/', PostUpdateView.as_view(template_name='post_form.html'), name='post-update'),
	path('post/<int:pk>/delete/', PostDeleteView.as_view(template_name='post_confirm_delete.html'), name='post-delete'),
	path('about/', views.about, name='about'), 
	path('technology/', views.technology, name='technology'), 	
	path('economics/', views.economics, name='economics'),
	path('subsciption/', views.subsciption, name='subsciption'),
	

]

