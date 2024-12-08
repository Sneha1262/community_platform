# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup'),
     path('login/', views.login_view, name='login'),
     path('login/addevents/', views.addevents, name='addevents'),
     path('listevents/', views.list_events, name='listevents'), 
     path('editevents/', views.edit_events, name='editevents'), 
     path('deleteevents/', views.delete_events, name='deleteevents'), 
]
