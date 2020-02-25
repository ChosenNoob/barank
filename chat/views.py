from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.utils import timezone
import datetime
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
		pair = User.objects.get(username=request.GET['pair'])
		return render(request, 'chat.html', {'me': request.user.id, 'pair': pair.id})

@login_required
def getMessages(request):
	# print(timezone.now())
	messages = Message.objects
	messages = messages.filter(Q(sender=request.user, reciever=request.POST['pair']) | Q(reciever=request.user, sender=request.POST['pair'])).order_by('order')
	# print(messages)
	# print('---------')
	# messages = messages.filter(time__lte=timezone.now()).order_by('time')
	# print(messages)

	data = serializers.serialize('json', messages)
	print(data)
	return HttpResponse(data, content_type="application/json")

@login_required
def getNewMessages(request):
	
	# print(timezone.now())
	messages = Message.objects
	messages = messages.filter(Q(sender=request.user, reciever=request.POST['pair']) | Q(reciever=request.user, sender=request.POST['pair'])).order_by('time')
	# print(messages)
	# print('---------')
	# messages = messages.exclude(time__lte=request.POST['timestamp']).order_by('time')
	messages = messages.exclude(order__gt=request.POST['timestamp']).order_by('order')
	print(messages)
	data = serializers.serialize('json', messages)
	return HttpResponse(data, content_type="application/json")
# 2020-02-25T21:29:22.557Z

@login_required
def sendMessage(request):
	sender = User.objects.get(id=request.POST['me'])
	reciever = User.objects.get(id=request.POST['pair'])
	obj = Message.objects.create(text=request.POST['text'], sender=sender, reciever=reciever)
	return HttpResponse('success', status=200)
