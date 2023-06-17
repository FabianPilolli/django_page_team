from django.urls import path
from .views import HomePageView, PostCreateView, PostListView,PostDetailView, PostUpdateView, BlogDeleteView

urlpatterns = [
    
    path('create_post/', PostCreateView.as_view(), name="create_post"),
    path('', PostListView.as_view(), name="post_list"),
    path('post/<int:pk>', PostDetailView.as_view(), name="post_detail"),
    path('post/<int:pk>/update', PostUpdateView.as_view(),name='post_update'),
    path('', BlogDeleteView.as_view(), name="blog_delete"),
]
