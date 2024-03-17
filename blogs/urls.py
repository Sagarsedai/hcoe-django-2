from django.urls import path

from .views import (
    HomePage,
    BlogPage,
    BlogDetailPage,
)

urlpatterns = [
    path("", HomePage.as_view(), name="index"),
    path("blogs/", BlogPage.as_view(), name="blogs"),
    path("blogs/<int:pk>/", BlogDetailPage.as_view(), name="blog_detail"),
]
