from django.contrib import admin
from .models import (
    Category,
    Comment,
    Tags,
    Article,
    Author
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', )
    list_display_links = ('id', 'name')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'comment', 'website')
    search_fields = ('name', )
    list_display_links = ('id', 'name')


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', )


@admin.register(Author)
class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'content')
    search_fields = ('name', )





@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'category', 'slug')
    search_fields = ('title', )
    list_display_links = ('id', 'title')
    readonly_fields = ('created_at', 'slug')
    autocomplete_fields = ('author', 'category')
    filter_horizontal = ('tags', )








