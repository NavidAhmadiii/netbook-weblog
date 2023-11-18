from django.urls import path
from .views import ArticleListView, ArticleDetailView, CategoryListView

app_name = "blog"
urlpatterns = [
    path('', ArticleListView.as_view(), name="home"),
    path('page/<int:page>', ArticleListView.as_view(), name="home"),
    path('article/<slug:slug>', ArticleDetailView.as_view(), name="detail"),
    path('category/<slug:slug>', CategoryListView.as_view(), name="category"),
    path('category/<slug:slug>/page/<int:page>', CategoryListView.as_view(), name="category"),

]
