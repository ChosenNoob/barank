from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Message(models.Model):
	text = models.TextField()
	time = models.DateField(auto_now=True)
	sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
	reciever = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recieved_messages')

class Chat(models.Model):
	starter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='started_chats')		
	joiner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='joined_chats')		
	messages = models.ManyToManyField(Message, related_name='chat')