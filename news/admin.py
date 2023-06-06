from django.contrib import admin
from .models import Post, Category


def nullfy_quantity(modeladmin, request, queryset):
    queryset.update(content_rating=0)


nullfy_quantity.short_description = 'Обнулить рейтинг'


class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'content_type', 'data', 'content_header', 'content_text', 'content_rating')
    list_filter = ('author', 'content_type', 'data', 'content_rating')
    search_fields = ('content_type',)
    actions = [nullfy_quantity]


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
