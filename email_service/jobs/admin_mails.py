from email_service.models import Email
from django.core.mail import mail_admins
import datetime
import socket
import traceback


def mail_to_admin():
    today = datetime.datetime.now().replace(hour=0, minute=0, second=0)
    emails = Email.objects.filter(sent_on__gte = today).order_by('sent_on')
    count = len(emails)
    message = 'Total emails sent today: ' + str(count) + '\n\n'

    for email in emails:
        message += email.sent_on.strftime("%H:%M") + '\n\n'

    # print(message)

    subject = 'Email Statistics for ' + str(today.date())
    mail_sent = False

    for i in range(5):   # Try 5 times in case mail is not sent due to socket.gaierror
        try:
            mail_admins(subject=subject, message=message)
            mail_sent = True
            break
        except socket.gaierror:
            # print(type(e).__name__, '.  Retrying...')
            print(traceback.format_exc(), '\nRetrying...\n')

    if mail_sent is False:
        print('Admin mail could not be sent after 5 attempts')
    else:
        print('Mail sent.')

