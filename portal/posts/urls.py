from django.urls import path
from .views import HomePageView, CreatePostView

from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('post/', CreatePostView.as_view(), name='add_post'),
]