from django import forms
from . import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EmailForm(forms.Form):
    to_recipients = fields.EmailListField(label='To', help_text='Required. Comma separated list of emails')
    cc_list = fields.EmailListField(required=False, label='Cc', help_text='Comma separated list of emails')
    bcc_list = fields.EmailListField(required=False, label='Bcc', help_text='Comma separated list of emails')
    subject = forms.CharField(required=False, max_length=100)
    body = forms.CharField(widget=forms.Textarea, required=False)

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. This email id will be used to send emails.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')