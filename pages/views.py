from django.views.generic import TemplateView, CreateView, ListView
from django.urls import reverse_lazy 
from .models import Post
from django.views.generic.edit import DeleteView

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

class BlogDeleteView(DeleteView):
        model = Post
        template_name = "delete.html"
        success_url = reverse_lazy("home")