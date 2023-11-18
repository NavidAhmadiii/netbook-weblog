from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Article, Category


# Create your views here.
def home(request, page=1):
    articles_list = Article.objects.published()
    paginator = Paginator(articles_list, 4)
    page = request.GET.get('page')
    articles = paginator.get_page(page)
    context = {
        "articles": articles,
    }
    return render(request, "home.html", context)


def detail(request, slug):
    context = {
        "article": get_object_or_404(Article.objects.published(), slug=slug)
    }
    return render(request, "detail.html", context)


def category(request, slug):
    context = {
        "category": get_object_or_404(Category, slug=slug, status=True)
    }
    return render(request, "category.html", context)
