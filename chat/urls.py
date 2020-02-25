from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chat/', views.chat, name='chat'),
    path('sendMessage/', views.sendMessage, name='sendMessage'),
    path('getMessages/', views.getMessages, name='getMessages'),
    path('getNewMessages/', views.getNewMessages, name='getNewMessages'),
]

# urlpatterns += staticfiles_urlpatterns()
