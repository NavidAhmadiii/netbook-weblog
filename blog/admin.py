from django.contrib import admin
from .models import Article, Category


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'parent','slug', 'status')
    list_filter = (['status'])
    search_fields = ('title', 'title')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)


class AricleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'jpublished', 'status', 'category_to_str')
    list_filter = ('published', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-status', '-published']

    def category_to_str(self, obj):
        return "، ".join([category.title for category in obj.category_published()])
    category_to_str.short_description = "دسته بندی"


admin.site.register(Article, AricleAdmin)