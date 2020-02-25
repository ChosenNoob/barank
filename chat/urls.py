from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chat/', views.chat, name='chat'),
    path('sendMessage/', views.sendMessage, name='sendMessage'),
]

# urlpatterns += staticfiles_urlpatterns()
