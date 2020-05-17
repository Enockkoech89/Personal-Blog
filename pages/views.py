from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .forms import SubsForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.
# def home(request):
# 	context = {
# 		'posts':Post.objects.all()
# 	}
# 	return render(request, 'home.html', context)
class PostListView(ListView):
	model = Post
	template_name = 'home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 9


class PostDetailView(DetailView):
	model = Post

	template_name = 'post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'category', 'photo', 'intro', 'content', 'video' ]
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'category', 'photo', 'intro', 'content', 'video' ]
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False



# view based on category 

# def motivational(request):
# 	context = {
# 		'posts':Post.objects.all()
# 	}
# 	return render( request, 'motivational.html', context)

def technology(request):
	context = {
		'posts':Post.objects.all()
	}
	return render( request, 'technology.html', context)


# def health(request):
# 	context = {
# 		'posts':Post.objects.all()
# 	}
# 	return render( request, 'health.html', context)

# def sermons(request):
# 	context = {
# 		'posts':Post.objects.all()
# 	}
# 	return render( request, 'sermons.html', context)

def economics(request):
	context = {
		'posts':Post.objects.all()
	}
	return render( request, 'economics.html', context)



def subsciption(request):

	if request.method == 'POST':
		r_form = SubsForm(request.POST)
		if r_form.is_valid():
			r_form.save()
			messages.success(request, f'Thank you! Your subscription request has been received')
			return redirect('home')
	else: 
		r_form = SubsForm()
	return render( request,'subs.html', {'r_form':r_form})


def about(request):
	return render(request, 'about.html')
	



	

