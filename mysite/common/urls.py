from django.urls import path
from . import views

app_name = 'common'

urlpatterns=[
    path('', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
]