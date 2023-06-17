from django.views.generic import TemplateView, CreateView, ListView
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

