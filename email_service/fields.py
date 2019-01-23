from django import forms
from django.core.validators import validate_email
from django.db import models


class EmailListField(forms.Field):
    def to_python(self, value):
        """ Normalize data to a list of strings """
        if not value:
            return []

        email_list_old = value.split(',')
        email_list_new = []

        for email in email_list_old:
            email_list_new.append(email.strip())

        return email_list_new

    def validate(self, value):
        """ Check if value consists only of valid emails """

        super().validate(value)
        for email in value:
            validate_email(email.strip())


class EmailStringField(models.Field):

    def get_db_prep_value(self, value, connection, prepared=False):
        value = super().get_db_prep_value(value, connection, prepared)

        str = ''

        if value is not None:
            str = ','.join(email.strip() for email in value)

        return str

    def db_type(self, connection):
        return 'text'
