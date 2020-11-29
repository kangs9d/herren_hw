from django.urls import path
from . import views

urlpatterns = [
    path('subscribe', views.subscribe, name='subscribe'),
    path('unsubscribe', views.unsubscribe, name='unsubscribe'),
    path('sendEmail', views.send_email, name='send_email'),
]
