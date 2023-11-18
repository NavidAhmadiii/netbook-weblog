from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Article, Category
from django.views.generic import ListView, DetailView


class ArticleListView(ListView):
    context_object_name = "articles"
    queryset = Article.objects.published()
    paginate_by = 4


class ArticleDetailView(DetailView):
    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article.objects.published(), slug=slug)


class CategoryListView(ListView):
    paginate_by = 4
    template_name = 'blog/category_list.html'

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Article.objects.published(), slug=slug)
        return category.articles.published()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryListView, self).get_context_data()
        context['category'] = category
        return context
