from django.core import paginator
from django.shortcuts import render,get_object_or_404
from blog.models import ArticleModel,CategoryModel
from django.core.paginator import Paginator

def category(request,categorySlug):
    category_name=get_object_or_404(CategoryModel,slug=categorySlug)
    articles=category_name.text.all()
    page=request.GET.get('page')
    paginator=Paginator(articles,1)
    return render(request,'pages/category.html',context={
        'articles':paginator.get_page(page),
        'category_name':categorySlug
        })
    