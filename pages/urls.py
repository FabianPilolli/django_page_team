from django.urls import path
from .views import HomePageView, PostCreateView, PostListView

urlpatterns = [
    
    path('create_post/', PostCreateView.as_view(), name="create_post"),
    path('', PostListView.as_view(), name="post_list"),
   
]
