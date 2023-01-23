from django.urls import path

from . import views

urlpatterns = [
    path('likepost/', views.likePost, name='likepost'),
    path('dislikepost/', views.dislikePost, name='dislikepost'),
    path('content/', views.index, name='index'),
    path('', views.index, name='index'),

    #path('', views.likePost, name='likepost'),
    
]