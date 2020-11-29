from django.urls import path
from . import views

urlpatterns = [
    path('subscribe', views.subscribe, name='subscribe'),
    path('unsubscribe', views.unsubscribe, name='unsubscribe'),
    path('mail', views.send_email, name='send_email'),
    path('inbox', views.check_inbox, name='check_inbox')
]
