from django.core import paginator
from django.shortcuts import render
from blog.models import ArticleModel
from django.core.paginator import Paginator
from django.db.models import Q
def home(request):
    search=request.GET.get('search')
    articles=ArticleModel.objects.order_by('-created_date')
    if search:
        articles=articles.filter(Q(header__icontains=search) | Q(content__icontains=search))
    page=request.GET.get('page')
    paginator=Paginator(articles,2)
    return render(request,'pages/home.html',context={'articles':paginator.get_page(page)})
    