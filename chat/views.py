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
		return render(request, 'chat.html', {'me': request.user.username, 'pair': request.GET['pair']})

@login_required
def getMessages(request):
	# messages = Message.objects.filter(time__lte=)
	pass

@login_required
def sendMessage(request):
	print(request.POST['me'])
	sender = User.objects.get(id=request.user.id)
	reciever = User.objects.get(username=request.POST['pair'])
	obj = Message.objects.create(text=request.POST['text'], sender=sender, reciever=reciever)
	pass	