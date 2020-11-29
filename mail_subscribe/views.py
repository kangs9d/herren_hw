import json

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from rest_framework import status

from mail_subscribe.models import MailingList


def subscribe(request):
    if request.method != 'POST':
        return HttpResponse('method not allowed', status=status.HTTP_405_METHOD_NOT_ALLOWED)
    username = request.POST.get('username')
    email = request.POST.get('email')

    new_user = MailingList.objects.get_or_create(username=username, user_email=email)
    if not new_user[1]:
        return HttpResponse('User Already Subscribed', status=status.HTTP_200_OK)
    else:
        return HttpResponse('Successfully Subscribed', status=status.HTTP_200_OK)


def unsubscribe(request):
    if request.method != 'POST':
        return HttpResponse('method not allowed', status=status.HTTP_405_METHOD_NOT_ALLOWED)
    email = request.POST.get('email')
    try:
        unsubscribing_user = MailingList.objects.filter(user_email=email)
    except MailingList.DoesNotExist:
        return HttpResponse('User Cannot Found', status=status.HTTP_404_NOT_FOUND)
    
    return 0


def send_email(request):
    return 0
