from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


    
from .models import Post


def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'contents/index.html', context)


def likePost(request ):
    if request.method == 'POST':
           #post_id = request.POST['post_id']
           #print( post_id)
           likedpost = Post.objects.get(pk=1) 
           likedpost.like_votes = int(request.POST['votes'])
           likedpost.save()
           return HttpResponse("Success!") 
    else:
           return HttpResponse("Request method is not a POST")


def dislikePost(request ):
    if request.method == 'POST':
           #post_id = request.POST['post_id']
           #print( post_id)
           dislikedpost = Post.objects.get(pk=1) 
           dislikedpost.dislike_votes = int(request.POST['votes'])
           dislikedpost.save()
           return HttpResponse("Success!") 
    else:
           return HttpResponse("Request method is not a POST")
