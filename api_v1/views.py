from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status

from mail_subscribe import views as mailing


@csrf_exempt
def subscribe(request):
    return mailing.subscribe(request)


@csrf_exempt
def unsubscribe(request):
    return mailing.unsubscribe(request)


@csrf_exempt
def send_email(request):
    return mailing.send_email(request)
