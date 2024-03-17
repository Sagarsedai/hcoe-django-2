from django.db import models
from tinymce import models as tmcemodel


class Author(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()

    # this method is called when somebody
    # tries to print this model object
    def __str__(self) -> str:
        return self.name


class BlogCategory(models.Model):
    name = models.CharField(max_length=100)

    # this method is called when somebody
    # tries to print this model object
    def __str__(self) -> str:
        return self.name


class BlogTags(models.Model):
    name = models.CharField(max_length=100)

    # this method is called when somebody
    # tries to print this model object
    def __str__(self) -> str:
        return self.name


class Blog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    #
    image = models.ImageField()
    title = models.CharField(max_length=255)
    # relation with author
    # Many Blogs written by one author
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    # relation with category
    # Many Blogs inside one category
    category = models.ForeignKey(BlogCategory, on_delete=models.PROTECT)
    # Many Blogs linked in many tags
    tags = models.ManyToManyField(BlogTags, blank=True)

    short_description = models.TextField(default="")

    description = tmcemodel.HTMLField()

    class Meta:
        ordering = ("-created_at",)

    # this method is called when somebody
    # tries to print this model object
    def __str__(self) -> str:
        return self.title


class BlogComment(models.Model):
    comment = models.TextField()
    full_name = models.CharField(max_length=100)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    # Many Comment in one blog
    blog = models.ForeignKey(
        Blog,
        on_delete=models.CASCADE,
        related_name="comments",
    )

    class Meta:
        ordering = ("-created_at",)
