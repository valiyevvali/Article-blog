from django.shortcuts import render,redirect,get_object_or_404
from blog.models import CommentModel
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def delete_comment(request,comment_id):
    comment=get_object_or_404(CommentModel,id=comment_id)
    if comment.author==request.user or comment.article.author==request.user:
        comment.delete()
        return redirect('article_detail',articleSlug=comment.article.slug)
    return redirect('home')
   
    