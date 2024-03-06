from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('newschedule', views.newschedule, name='newschedule'),
    path('submitnews', views.submitnews, name='submitnews'),
]