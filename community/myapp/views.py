# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import UserCreationForm
from myapp.forms import loginform, signupform, eventform_1, edit_event_form, delete_event_form
from myapp.models import Login, signup, events_1, edit_events, delete_your_events

# Global variable for the username
global_username = "default"

# Function to authenticate and handle signup and login
def authenticate_user(username, password, action):
    global global_username
    global_username = username
    
    if action == 'signup':
        # Check if user exists
        if not signup.objects.filter(Username=username).exists():
            # Create new user
            signup.objects.create(Username=username, password=password)
            return True
        else:
            return False
    else:  # login
        user = signup.objects.filter(Username=username, password=password).first()
        if user:
            return True
        else:
            return False

# Function to list all events
def get_eventlist():
    return events_1.objects.all()

# View to add new events
def addevents(request):
    if request.method == 'POST':
        form = eventform_1(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            eventname = form.cleaned_data['eventname']
            eventdate = form.cleaned_data['eventdate']
            eventtime = form.cleaned_data['eventtime']
            
            # Save event to the database using the ORM
            events_1.objects.create(username=username, eventname=eventname, eventdate=eventdate, eventtime=eventtime)
            
            return render(request, 'eventadded.html')
    else:
        form = eventform_1()
    return render(request, 'addevents.html', {'form': form})

# View to edit events
def edit_events(request):
    if request.method == 'POST':
        form = edit_event_form(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            username = form.cleaned_data['username']
            eventname = form.cleaned_data['eventname']
            eventdate = form.cleaned_data['eventdate']
            eventtime = form.cleaned_data['eventtime']
            
            # Try to find the event and update it
            event = events_1.objects.filter(id=id, username=username).first()
            if event:
                event.eventname = eventname
                event.eventdate = eventdate
                event.eventtime = eventtime
                event.save()  # Save the updated event
                
                return render(request, 'success.html')
            else:
                return render(request, 'failure.html')
    else:
        form = edit_event_form()
    return render(request, 'editevents.html', {'form': form})

# View to delete events
def delete_events(request):
    if request.method == 'POST':
        form = delete_event_form(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            username = form.cleaned_data['username']
            
            # Find the event and delete it
            event = events_1.objects.filter(id=id, username=username).first()
            if event:
                event.delete()  # Delete the event
                return render(request, 'success.html')
            else:
                return render(request, 'failure.html')
    else:
        form = delete_event_form()
    return render(request, 'deleteevents.html', {'form': form})

# Signup view
def signup_view(request):
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['Username']
            password = form.cleaned_data['password']
            
            if authenticate_user(username, password, 'signup'):
                return render(request, 'success.html')
            else:
                return render(request, 'alreadythere.html')
    else:
        form = signupform()
    return render(request, 'signup.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = loginform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['Username']
            password = form.cleaned_data['password']
            
            if authenticate_user(username, password, 'login'):
                return render(request, 'community.html')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = loginform()
    return render(request, 'login.html', {'form': form})

# View to list all events
def list_events(request):
    event_list = get_eventlist()
    return render(request, 'listevents.html', {'events': event_list})
