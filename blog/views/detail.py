from django.core import paginator
from django.shortcuts import render,get_object_or_404
from blog.models import ArticleModel


def article_detail(request,articleSlug):
    article=get_object_or_404(ArticleModel,slug=articleSlug)
    comments=article.yorumlar.all()
    return render(request,'pages/detail.html',context={
        'article':article,
        'comments':comments
        })
    