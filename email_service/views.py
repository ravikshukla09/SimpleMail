from django.shortcuts import render, redirect, reverse
from .forms import EmailForm, SignUpForm
from .models import Email
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
import socket
import traceback
import logging

logger = logging.getLogger(__name__)

# Create your views here.

@login_required()
def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            from_sender = request.user
            to_recipients = form.cleaned_data.get('to_recipients')
            cc_list = form.cleaned_data.get('cc_list')
            bcc_list = form.cleaned_data.get('bcc_list')
            subject = form.cleaned_data.get('subject')
            body = form.cleaned_data.get('body')

            # sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
            # from_email = Email(from_sender.email)
            # Mail()


            try:
                EmailMessage(subject, body, from_sender.email, to_recipients, bcc_list, cc=cc_list).send()

            except Exception:
                # print(traceback.format_exc())
                logger.error(traceback.format_exc())
                return render(request, 'email_service/new_email.html', {'form': form, 'error': 'socket.gaierror'})

            email = Email.objects.create(from_sender=from_sender, to_recipients=to_recipients,
                                         cc_list=cc_list, bcc_list=bcc_list, subject=subject, body=body)

            # return redirect('index', kwargs={'message': 'Your email has been sent'}, permanent=True)

            logger.info('Email sent for user: ' + str(request.user))
            messages.add_message(request, messages.INFO, 'Your email has been sent.')
            return redirect(reverse('email_service:index'))
    else:
        form = EmailForm()

    return render(request, 'email_service/new_email.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            logger.info('New user signed up: ' + str(username))
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'email_service/signup.html', {'form': form})


@login_required()
def index(request):
    return render(request, 'email_service/index.html')


@login_required()
def sent_emails(request):
    emails = Email.objects.filter(from_sender = request.user).order_by('-sent_on')
    return render(request, 'email_service/sent_emails.html', {'emails': emails})
