from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Events
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.'



class HomePageView(LoginRequiredMixin,ListView):
    template_name = 'index.html'
    model = Events
    context_object_name = 'students'

    def get_queryset(self):
        events = super().get_queryset()
        if not self.request.user.is_authenticated:
            return None
        #return students.filter(manager=self.request.user)
        if self.request.GET:
            return events.filter(id=self.request.GET['search_term'])


class spage1View(LoginRequiredMixin, DetailView):
    template_name = 'spage1.html'
    model = Events
    context_object_name = 'student'


@login_required
def search(request):
    print(request.GET)

    if request.GET:
        search_term = request.GET['search_term']
        # search_result = Student.objects.filter(firstname__icontains = search_term)
        # for complex query
        search_result = Student.objects.filter(
            Q(manager=request.user) &
            Q(firstname__icontains=search_term) |
            Q(lastname__icontains=search_term)
        )

        context = {'search_term': search_term,
                   'students': search_result}
        return render(request, 'search.html', context)
    else:
        return redirect('home')

def CreateStudent(request):
    model = Events
    template_name = 'create.html'
    """
    fields = [
        'event_type_name',

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
        'answer_10',

    ]"""
    success_url = '/create/success'

    #def get_queryset(self):
    if request.method == 'GET':
        e = Events.objects.create(
            event_type_name=request.GET.get('event_type_name',None), #,None),
            event_type_uuid=request.GET.get('event_type_uuid',None),
            event_start_time=request.GET.get('event_start_time', None),
            event_end_time=request.GET.get('event_end_time', None),
            invitee_uuid=request.GET.get('invitee_uuid', None),
            invitee_email=request.GET.get('invitee_email', None),
            invitee_first_name=request.GET.get('invitee_first_name', None),
            invitee_last_name=request.GET.get('invitee_last_name', None),
            invitee_full_name=request.GET.get('invitee_full_name', None),
            invitee_payment_amount=request.GET.get('invitee_payment_amount', None),
            invitee_payment_currency=request.GET.get('invitee_payment_currency', None),
            guests=request.GET.get('guests', None),
            utm_source=request.GET.get('utm_source', None),
            utm_medium=request.GET.get('utm_medium', None),
            utm_campaign=request.GET.get('utm_campaign', None),
            utm_content=request.GET.get('utm_content', None),
            utm_term=request.GET.get('utm_term', None),
            assigned_to=request.GET.get('assigned_to', None),
            text_reminder_number=request.GET.get('text_reminder_number', None),
            answer_1=request.GET.get('answer_1', None),
            answer_2=request.GET.get('answer_2', None),
            answer_3=request.GET.get('answer_3', None),
            answer_4=request.GET.get('answer_4', None),
            answer_5=request.GET.get('answer_5', None),
            answer_6=request.GET.get('answer_6', None),
            answer_7=request.GET.get('answer_7', None),
            answer_8=request.GET.get('answer_8', None),
            answer_9=request.GET.get('answer_9', None),
            answer_10=request.GET.get('answer_10', None),
        )#.save()

        return redirect('success', e.id)



    """
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.event_type_name = self.request.GET.get('event_type_name')
        instance.event_type_uuid = self.request.GET.get('event_type_uuid')
        #instance.manager = self.request.user
        instance.save()
        return redirect('success', instance.pk)
    """


"""
def success(request):
    model = Events
    template_name = 'success.html'
    context = {}
    return render(request, 'success.html', context)
"""
class success(DetailView):
    template_name = 'spage1.html'
    model = Events
    context_object_name = 'student'


class UpdateStudent(LoginRequiredMixin, UpdateView):
    model = Events
    template_name = 'update.html'
    #slug_field = 'search_term'
    fields = [
        'event_type_name',

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
        'answer_10',

    ]
    success_url = '/'

    def form_valid(self, form):
        instance = form.save()
        return redirect('/?search_term=+'+ str(instance.pk))

    """def get_queryset(self):
        events = super().get_queryset()
        if not self.request.user.is_authenticated:
            return None
        #return students.filter(manager=self.request.user)
        if self.request.GET:
            return events.filter(id=self.request.GET['search_term'])
    """

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "registration/signup.html"
    success_url = "/"


class DeleteStudent(DeleteView):
    model = Events
    template_name = "delete.html"
    success_url = '/'



