from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.
from .models import Events
from import_export.admin import ImportExportModelAdmin

admin.site.unregister(Group)


class EventAdmin(ImportExportModelAdmin):
    list_display_links = ('event_type_name',)
    list_display = (   'event_type_name',

        'event_type_uuid',

        'event_start_time',
        'event_end_time',
    'invitee_uuid',
    'invitee_email',
    'invitee_first_name',
    'invitee_last_name',
    'invitee_full_name',
    'invitee_payment_amount',
    'invitee_payment_currency',
    'guests',
    'utm_source',
    'utm_medium',
    'utm_campaign',
    'utm_content',
    'utm_term',
    'assigned_to',
    'text_reminder_number',
    'answer_1',
        'answer_2',
        'answer_3',
        'answer_4',
        'answer_5',
        'answer_6',
        'answer_7',
        'answer_8',
        'answer_9',
        'answer_10',)
    #list_editable = ('email',)
    #list_filter = ('gender', 'date_added',)
    #search_fields = ('firstname', 'lastname', 'email', 'gender')


admin.site.register(Events, EventAdmin)

