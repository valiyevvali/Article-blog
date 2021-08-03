from django.contrib import admin
from .models import CategoryModel,ArticleModel,CommentModel
from blog import models
# Register your models here.
admin.site.register(CategoryModel)

class ArticleAdmin(admin.ModelAdmin):
    search_fields=('header',)
    list_display=(
        'slug','created_date','author'
    )

admin.site.register(ArticleModel,ArticleAdmin)


class CommentAdmin(admin.ModelAdmin):
    search_fields=('author','comment')
    list_display=(
        'author','created_date','updated_date'
    )

admin.site.register(CommentModel,CommentAdmin)