from django.contrib import admin
from .models import CategoryModel,ArticleModel,CommentModel,ContactModel
from blog import models
# Register your models here.
admin.site.register(CategoryModel)

@admin.register(ArticleModel)
class ArticleAdmin(admin.ModelAdmin):
    search_fields=('header',)
    list_display=(
        'slug','created_date','author'
    )


@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    search_fields=('author','comment')
    list_display=(
        'author','created_date','updated_date'
    )


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    search_fields=('email','name_surname')
    list_display=(
        'email','created_date'
    )

