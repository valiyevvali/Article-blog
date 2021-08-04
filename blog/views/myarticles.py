from django.core import paginator
from django.shortcuts import render
from blog.models import ArticleModel
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def myarticles(request):
    
    articles=request.user.texts.order_by('-created_date')
    page=request.GET.get('page')
    paginator=Paginator(articles,2)
    return render(request,'pages/myarticle.html',context={'articles':paginator.get_page(page)})
    