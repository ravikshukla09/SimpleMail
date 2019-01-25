from django.urls import path
from . import views

app_name = 'email_service'
urlpatterns = [
    path('', views.index, name='index'),
    path('new_email/$', views.send_email, name='new_email'),
    path('sent_emails/$', views.sent_emails, name='sent_emails'),
    path('signup/$', views.signup, name='signup'),
]