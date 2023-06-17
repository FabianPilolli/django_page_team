from django.views.generic import TemplateView, CreateView, ListView,DetailView, UpdateView
from django.urls import reverse_lazy 
from .models import Post

# Create your views here.

class HomePageView(TemplateView):
    template_name = "home.html"

class PostCreateView(CreateView):
    model = Post
    template_name = "create_post.html"
    fields = ('title', 'description')
    success_url = reverse_lazy('home')

class PostListView(ListView):
    model = Post
    template_name = 'home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'description')
    template_name = 'update_post.html'
    success_url = reverse_lazy('post_list')


