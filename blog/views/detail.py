from django.shortcuts import render,get_object_or_404
from blog.models import ArticleModel
from blog.forms import CommentForm

def article_detail(request,articleSlug):
    article=get_object_or_404(ArticleModel,slug=articleSlug)
    comments=article.yorumlar.all()
    if request.method=='POST':
        add_comment=CommentForm(data=request.POST)
        c=add_comment.save(commit=False)
        c.author=request.user
        c.article=article
        c.save()
    add_comment=CommentForm()
    return render(request,'pages/detail.html',context={
        'article':article,
        'comments':comments,
        'form':add_comment
        })
    