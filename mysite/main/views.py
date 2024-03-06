from datetime import date, datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils.safestring import mark_safe
from calendar import HTMLCalendar

from .models import *
from .utils import Calendar

def home(request):
    return render(request, 'main/home.html')

class CalendarView(generic.ListView):
    model = Events
    template_name = 'main/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def newschedule(request):
    return render(request, 'main/newschedule.html')

def submitnews(request):
    e = Events()
    e.title = request.POST['title']
    e.content = request.POST['contents']
    e.date = request.POST['date']
    e.save()
    return HttpResponseRedirect(reverse('main:calendar'))