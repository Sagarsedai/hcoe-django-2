from django.contrib import admin

# Register your models here.


from .models import Author, Blog, BlogCategory, BlogComment, BlogTags


admin.site.register(
    [
        Author,
        Blog,
        BlogTags,
        BlogCategory,
        BlogComment,
    ]
)
