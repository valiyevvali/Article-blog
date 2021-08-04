from django.shortcuts import render,redirect,get_object_or_404
from blog.models import ArticleModel
from blog.forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='/')
def edit_article(request,articleSlug):
    article=get_object_or_404(ArticleModel,slug=articleSlug,author=request.user)
    form=ArticleForm(request.POST or None,files=request.FILES or None,instance=article)

    if form.is_valid():
        form.save()
        return redirect('article_detail',articleSlug=article.slug)
    context={
        'form':form
    }
    return render(request,'pages/edit_article.html',context)
   
    