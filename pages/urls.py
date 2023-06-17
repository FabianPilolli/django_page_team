from django.urls import path
from .views import HomePageView, PostCreateView, PostListView, BlogDeleteView

urlpatterns = [
    
    path('create_post/', PostCreateView.as_view(), name="create_post"),
    path('', PostListView.as_view(), name="post_list"),
    path('', BlogDeleteView.as_view(), name="blog_delete"),
]
