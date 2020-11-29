import json
import multiprocessing

import requests
from django.http import HttpResponse
from rest_framework import status
from herren_hw import settings
import django

django.setup()

from mail_subscribe.models import MailingList


def subscribe(request):
    if request.method != 'POST':
        return HttpResponse('method not allowed', status=status.HTTP_405_METHOD_NOT_ALLOWED)
    username = request.POST.get('username')
    email = request.POST.get('email')

    new_user = MailingList.objects.get_or_create(username=username, user_email=email, deleted=False)
    if not new_user[1]:
        return HttpResponse('User Already Subscribed', status=status.HTTP_200_OK)
    else:
        return HttpResponse('Successfully Subscribed', status=status.HTTP_200_OK)


def unsubscribe(request):
    if request.method != 'POST':
        return HttpResponse('method not allowed', status=status.HTTP_405_METHOD_NOT_ALLOWED)
    email = request.POST.get('email')
    try:
        unsubscribing_users = MailingList.objects.filter(user_email=email, deleted=False)
    except MailingList.DoesNotExist:
        return HttpResponse('User Cannot Found', status=status.HTTP_404_NOT_FOUND)
    for element in unsubscribing_users:
        element.deleted = True
        element.save()
    return HttpResponse('Successfully Unsubscribed', status=status.HTTP_200_OK)


def send_email(request):
    if request.method != 'POST':
        return HttpResponse('method not allowed', status=status.HTTP_405_METHOD_NOT_ALLOWED)
    mailing_list = MailingList.objects.all()
    subject = request.POST.get('subject')
    content = request.POST.get('content')
    pool = multiprocessing.Pool(processes=2)
    i = pool.map(process_mailing, divide_queryset_with_content(mailing_list, [subject, content], 4))
    for elem in i:
        if not elem:
            return HttpResponse('Server Internal Error', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    pool.close()
    pool.join()
    return HttpResponse('Successfully sent Email', status=status.HTTP_200_OK)


def divide_queryset_with_content(seq, content, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0
    while last < len(seq):
        out.append({'queryset': seq[int(last):int(last + avg)], 'content': content})

        last += avg
    return out


def process_mailing(queryset_and_content):
    for elem in queryset_and_content.get('queryset'):
        email = elem.user_email
        external_herren_url = settings.MAILING_API_URL + 'api/v1/mail'
        subject = queryset_and_content.get('content')[0]
        content = queryset_and_content.get('content')[1]
        post_data = {'mailto': email, 'subject': subject, 'content': content}
        headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'herren-recruit-python'}
        res = requests.post(external_herren_url, headers=headers, data=post_data)
        resp = json.loads(res.text)
        if not resp.get('status') == 'success':
            return False
    return True
