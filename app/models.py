from django.db import models

# Create your models here.
from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User
from utils import create_new_ref_number


# Create your models here.

class Student(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField()
    gender = models.CharField(max_length=20, choices=(('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER')))
    date_added = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.firstname

class Events(models.Model):

    event_type_name = models.CharField(max_length=100)

    event_type_uuid = models.CharField(max_length=400)

    event_start_time = models.DateTimeField(max_length=10)
    #( in invitee timezone(iso8601 format))

    event_end_time =  models.DateTimeField(max_length=10)
    # ( in invitee timezone(iso8601 format))

    invitee_uuid = models.CharField(max_length=400)

    invitee_email = models.EmailField()

    invitee_first_name = models.CharField(max_length=100 , null=True, default=None)
    #(when aaplicable)

    invitee_last_name = models.CharField(max_length=100 , null=True, default=None)
    #(when    applicable)

    invitee_full_name = models.CharField(max_length=100 , null=True, default=None)
    # (when    applicable)

    invitee_payment_amount = models.CharField(max_length=100 , null=True, default=None)
    # (when    applicable)

    invitee_payment_currency = models.CharField(max_length=100 , null=True, default=None)
    # (when   applicable)

    guests = models.CharField(max_length=500 , null=True, default=None)

    utm_source = models.CharField(max_length=100 , null=True, default=None)
    # ( if available)

    utm_medium = models.CharField(max_length=100 , null=True, default=None)
    #( if available)

    utm_campaign = models.CharField(max_length=100 , null=True, default=None)
    #( if available)

    utm_content = models.CharField(max_length=100 , null=True, default=None)
    #( if available)

    utm_term = models.CharField(max_length=100 , null=True, default=None)
    #( if available)

    assigned_to = models.CharField(max_length=100 , null=True, default=None)

    text_reminder_number = models.CharField(max_length=100 , null=True, default=None)
    # ( if available)

    answer_1 = models.CharField(max_length=100 , null=True, default=None)
    #( if available)

    answer_2 = models.CharField(max_length=100 , null=True, default=None)
    #( if available)
    answer_3 = models.CharField(max_length=100 , null=True, default=None)
    #( if available)
    answer_4 = models.CharField(max_length=100 , null=True, default=None)
    #( if available)
    answer_5 = models.CharField(max_length=100 , null=True, default=None)
    #( if available)
    answer_6 = models.CharField(max_length=100 , null=True, default=None)
    #( if available)
    answer_7 = models.CharField(max_length=100 , null=True, default=None)
    #( if available)
    answer_8 = models.CharField(max_length=100 , null=True, default=None)
    #( if available)
    answer_9 = models.CharField(max_length=100 , null=True, default=None)
    #( if available)
    answer_10 = models.CharField(max_length=100 , null=True, default=None)
    #( if available)
