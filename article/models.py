from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from ckeditor.fields import RichTextField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='author/')
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True, related_name='articles')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='articles')
    tags = models.ManyToManyField(Tags, related_name='tags')
    title = models.CharField(max_length=250)
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='article/')
    slug = models.SlugField()
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


def pre_save_article(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)


pre_save.connect(pre_save_article, sender=Article)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True, blank=True, related_name='comments')
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='comments/')
    email = models.EmailField(null=True, blank=True, max_length=50)
    website = models.CharField(null=True, blank=True, max_length=50)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name