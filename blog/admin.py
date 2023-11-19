from gettext import ngettext

from django.contrib import admin
from django.core.checks import messages

from .models import Article, Category


# Register your models here.

# write actions for admin panel
def make_published(modeladmin, request, queryset):
    row_updated = queryset.update(status='p')
    if row_updated == 1:
        message_bit = "منتشر شد"
    else:
        message_bit = "منتشر شد"
    modeladmin.message_user(request, '{} مقاله {}'.format(row_updated, message_bit))


make_published.short_description = "انتشار مقالات انتخاب شده"


# write actions for admin panel
def make_draft(modeladmin, request, queryset):
    row_updated = queryset.update(status='d')
    if row_updated == 1:
        message_bit = "پیش نویس شد"
    else:
        message_bit = "پیش نویس شد"
    modeladmin.message_user(request, '{} مقاله {}'.format(row_updated, message_bit))


make_draft.short_description = "پیش نویس شدن مقالات انتخاب شده"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'parent', 'slug', 'status')
    list_filter = (['status'])
    search_fields = ('title', 'title')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)


class AricleAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail_tag', 'slug', 'jpublished', 'status', 'category_to_str')
    list_filter = ('published', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['-status', '-published']
    actions = [make_published, make_draft]

    def category_to_str(self, obj):
        return "، ".join([category.title for category in obj.category_published()])

    category_to_str.short_description = "دسته بندی"


admin.site.register(Article, AricleAdmin)
