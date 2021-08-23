from django.shortcuts import redirect, render,get_object_or_404
from blog.models import ArticleModel
from blog.forms import CommentForm
from django.views import View
import logging

logger=logging.getLogger('article_reader')
class detail_article(View):
    http_method_names=['get','post']
    add_comment=CommentForm

    def get(self,request,articleSlug):
        article=get_object_or_404(ArticleModel,slug=articleSlug)
        if request.user.is_authenticated:
            logger.info('article readed by: '+request.user.username)
        comments=article.yorumlar.all()
        return render(request,'pages/detail.html',context={
        'article':article,
        'comments':comments,
        'form':self.add_comment()
        })
    
    def post(self,request,articleSlug):
        article=get_object_or_404(ArticleModel,slug=articleSlug)
        add_comment=self.add_comment(data=request.POST)
        c=add_comment.save(commit=False)
        c.author=request.user
        c.article=article
        c.save()
        return redirect('article_detail',articleSlug=articleSlug)




# def article_detail(request,articleSlug):
#     article=get_object_or_404(ArticleModel,slug=articleSlug)
#     comments=article.yorumlar.all()
#     if request.method=='POST':
#         add_comment=CommentForm(data=request.POST)
#         c=add_comment.save(commit=False)
#         c.author=request.user
#         c.article=article
#         c.save()
#     add_comment=CommentForm()
#     return render(request,'pages/detail.html',context={
#         'article':article,
#         'comments':comments,
#         'form':add_comment
#         })
    