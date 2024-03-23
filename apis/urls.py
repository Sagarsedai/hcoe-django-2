from django.urls import path
from .viewsets import BlogCreateListView

urlpatterns = [
    path("blogs/", BlogCreateListView.as_view()),
]
