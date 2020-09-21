# Generated by Django 3.1.1 on 2020-09-19 08:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type_name', models.CharField(max_length=100)),
                ('event_type_uuid', models.CharField(max_length=400)),
                ('event_start_time', models.DateTimeField(max_length=10)),
                ('event_end_time', models.DateTimeField(max_length=10)),
                ('invitee_uuid', models.CharField(max_length=400)),
                ('invitee_email', models.EmailField(max_length=254)),
                ('invitee_first_name', models.CharField(default=None, max_length=100, null=True)),
                ('invitee_last_name', models.CharField(default=None, max_length=100, null=True)),
                ('invitee_full_name', models.CharField(default=None, max_length=100, null=True)),
                ('invitee_payment_amount', models.CharField(default=None, max_length=100, null=True)),
                ('invitee_payment_currency', models.CharField(default=None, max_length=100, null=True)),
                ('guests', models.CharField(default=None, max_length=500, null=True)),
                ('utm_source', models.CharField(default=None, max_length=100, null=True)),
                ('utm_medium', models.CharField(default=None, max_length=100, null=True)),
                ('utm_campaign', models.CharField(default=None, max_length=100, null=True)),
                ('utm_content', models.CharField(default=None, max_length=100, null=True)),
                ('utm_term', models.CharField(default=None, max_length=100, null=True)),
                ('assigned_to', models.CharField(default=None, max_length=100, null=True)),
                ('text_reminder_number', models.CharField(default=None, max_length=100, null=True)),
                ('answer_1', models.CharField(default=None, max_length=100, null=True)),
                ('answer_2', models.CharField(default=None, max_length=100, null=True)),
                ('answer_3', models.CharField(default=None, max_length=100, null=True)),
                ('answer_4', models.CharField(default=None, max_length=100, null=True)),
                ('answer_5', models.CharField(default=None, max_length=100, null=True)),
                ('answer_6', models.CharField(default=None, max_length=100, null=True)),
                ('answer_7', models.CharField(default=None, max_length=100, null=True)),
                ('answer_8', models.CharField(default=None, max_length=100, null=True)),
                ('answer_9', models.CharField(default=None, max_length=100, null=True)),
                ('answer_10', models.CharField(default=None, max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 19, 14, 22, 22, 705703)),
        ),
    ]