from typing import Any
from django.shortcuts import render

# Create your views here.
from django.views import generic

from .models import Blog, BlogComment


class HomePage(generic.TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class BlogPage(generic.ListView):
    template_name = "blog.html"
    model = Blog
    context_object_name = "ol"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class BlogDetailPage(generic.DetailView):
    template_name = "single.html"
    model = Blog
    context_object_name = "detail"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        data = request.POST
        files = request.FILES

        instance = self.get_object()

        BlogComment.objects.create(
            full_name=data.get("full_name"),
            comment=data.get("comment"),
            image=files.get("image"),
            blog=instance,
        )

        return super().get(request, *args, **kwargs)
