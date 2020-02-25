from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from chat.models import *
# Create your views here.

@login_required
def index(request):
	if request.method == 'GET':
		user = User.objects.get(id=request.user.id)
		chats = Chat.objects.filter( Q(starter=request.user) | Q(joiner=request.user))

		return render(request, 'index.html', {'chats': chats, 'user': user})

@login_required
def chat(request):
	if request.method == 'GET':
		user = User.objects.get(id=request.user.id)
		return render(request, 'chat.html', {'pair': request.GET['pair']})		