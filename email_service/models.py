from django.db import models
from . import fields


# Create your models here.
class Email(models.Model):
    from_sender = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, related_name='user')
    to_recipients = fields.EmailStringField(default='')
    cc_list = fields.EmailStringField(null=True)
    bcc_list = fields.EmailStringField(null=True)
    subject = models.CharField(max_length=100, null=True)
    body = models.TextField(null=True)
    sent_on = models.DateTimeField(auto_now_add=True)
