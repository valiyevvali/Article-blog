from django.shortcuts import render,redirect
from blog.models import ArticleModel
from blog.forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='/')
def add_article(request):
    form=ArticleForm(request.POST or None,files=request.FILES or None)
    if form.is_valid():
        article=form.save(commit=False)
        article.author=request.user
        article.save()
        form.save_m2m()
        messages.info(request, 'Your message has been sent successfully...')
        return redirect('article_detail',articleSlug=article.slug)
    context={
        'form':form
    }
    return render(request,'pages/add_article.html',context)
   
    