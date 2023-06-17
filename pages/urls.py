from django.urls import path
from .views import HomePageView, PostCreateView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path('create_post/', PostCreateView.as_view(), name="create_post")
   
]
