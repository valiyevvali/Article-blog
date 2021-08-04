from django.shortcuts import render,redirect,get_object_or_404
from blog.models import ArticleModel
from blog.forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='/')
def delete_article(request,articleSlug):
    get_object_or_404(ArticleModel,slug=articleSlug,author=request.user).delete()
    messages.info(request, 'Article is deleted succesfully...')
    return redirect(request.META.get('HTTP_REFERER'))
   
    