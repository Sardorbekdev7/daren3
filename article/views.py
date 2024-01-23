from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from .models import Article, Comment, Tags, Category
from .forms import CommentForm
# Create your views here.


def article_list(request):
    articles = Article.objects.order_by('-id')
    categories = Category.objects.all()
    print(categories.values())
    for i in articles.values():
        print(i['category_id'])
    ctx = {
        'articles': articles
    }

    return render(request, 'article/index.html', ctx)


def article_archive(request):
    articles = Article.objects.order_by('-id')
    popular_articles = Article.objects.order_by('-id')
    categories = Category.objects.all()
    tags = Tags.objects.all()
    q = request.GET.get('q')
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    if q:
        articles = articles.filter(title__contains=q)
    if cat:
        articles = articles.filter(category__name=cat)
    if tag:
        articles = articles.filter(tags__name=tag)
    ctx = {
        'articles': articles,
        'popular_articles': popular_articles,
        'categories': categories,
        'tags': tags
    }
    return render(request, 'article/archive.html', ctx)


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    form = CommentForm()
    q = request.GET.get('q')
    if q:
        article = Article.objects.filter(title__contains=q)
        resolve = resolve_url('article:list')
        return redirect(resolve)
    if request.method == 'POST':
        print(request.POST)
        form = CommentForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            print(comment)
            return redirect('article:detail', slug=article.slug)
    ctx = {
        'article': article,
        'form': form
    }

    return render(request, 'article/single-blog.html', ctx)






