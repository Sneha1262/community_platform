# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import UserCreationForm
from myapp.forms import loginform, signupform ,eventform_1,edit_event_form,delete_event_form # Assume these are your custom forms
import pymysql
import sys

global_username="default"

conn = pymysql.connect(
host= "database-1.cq3zzo5swvvt.us-east-1.rds.amazonaws.com", #endpoint link
        port = 3306, # 3306
        user = 'admin', # admin
        password = 'adminireland', #adminadmin
        db = 'communitydb', #test
        )

def verify_and_delete(id, username):
    global global_username
    
    
    try:
        cursor = conn.cursor()

        
        if global_username.upper() == username.upper():
            
            query = f"DELETE FROM myapp_events_1 WHERE id = {id}"
            
            cursor.execute(query)
            
            conn.commit()
            
            cursor.close()
            
            return True 
        else:
            return False  
    except Exception as e:
        
        print(f"Error during deletion: {e}")
        return False  

    
        
        
    
    


def verify_and_update(id,username,eventname,eventdate,eventtime):
    global global_username
    
    cursor = conn.cursor()
    print(global_username)
    print(username)
    if global_username.upper() == username.upper():
        query="""
        update myapp_events_1 set username = %s , eventname = %s , eventdate = %s , eventtime= %s where id = %s
        """
         
        values=(username,eventname,eventdate,eventtime,id)   

        cursor.execute(query,values)
        conn.commit()
        cursor.close()
        return True
    else:
        return False
    
     
    

    

def save_events(username,eventname,eventdate,eventtime):
    
    cursor = conn.cursor()
    query = """
    INSERT INTO myapp_events_1 (username,eventname,eventdate,eventtime)
    VALUES (%s, %s,%s, %s)
    """
    
    values=(username,eventname,eventdate,eventtime)
    
    print("event added succesfully")
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    return True

    

def get_eventlist():
    global global_username
    cursor = conn.cursor()
    
    print(global_username)
    
    
    cursor.execute(f"SELECT * FROM myapp_events_1 ")  # Replace 'yourapp_events' with your actual table name
    rows = cursor.fetchall()  # Fetch all rows from the query result

    # Create a list of dictionaries representing the rows
    event_list = []
    for row in rows:
        event = {
            'eventid': row[0],
            'eventname': row[1],  # Assuming the first column is eventname
            'eventdate': row[2],  # Assuming the second column is eventdate
            'eventtime': row[3],  # Assuming the third column is eventtime
        }
        event_list.append(event)
        
    return event_list    

def edit_events(request):
    
    if request.method == 'POST':
        form = edit_event_form(request.POST)  
        if form.is_valid():
            id        =form.cleaned_data['id']
            username  =form.cleaned_data['username']
            eventname =form.cleaned_data['eventname']
            eventdate =form.cleaned_data['eventdate']
            eventtime =form.cleaned_data['eventtime']
           
            if(verify_and_update(id,username,eventname,eventdate,eventtime)):
                 return render(request, 'success.html')
            else:
                return render(request,'failure.html') 



    else:        
        form=edit_event_form()
        return render(request, 'editevents.html', {'form': form})


def delete_events(request):
    if request.method == 'POST':
        
     print("entered for deletion")   
     form = delete_event_form(request.POST)  
     if form.is_valid():
         id        =form.cleaned_data['id']
         username  =form.cleaned_data['username']
        
         if(verify_and_delete(id,username)):
              return render(request, 'success.html')
         else:
             return render(request,'failure.html') 
    
    form=delete_event_form()
    return render(request, 'deleteevents.html', {'form': form})

    

   
    
    
    

def authenticate_user(username,password,action):
    global global_username
    
    global_username=username
    
    cursor = conn.cursor()
    
    if 'signup' == action:
        
        check_user_exist_query=f"Select password from myapp_login where username ='{password}'"
        
        print(check_user_exist_query)

        pass_result=cursor.execute(check_user_exist_query)
        print("res")
        print(pass_result)
        if pass_result == 0:
            query = """
            INSERT INTO myapp_login (Username,password)
            VALUES (%s, %s)
            """
            
            values=(username,password)
            cursor.execute(query, values)
            conn.commit()
            cursor.close()
            
            print("user added")
            
            return True
        
        else:
            print("user already exist")
            
            return False
    else:
        check_user_exist_query=f"Select password from myapp_login where username ='{username}'"

        pass_result=cursor.execute(check_user_exist_query)

        if str(pass_result).upper() == password.upper():
            print("already exist change your user name ")
            return False
        else:
            print("user created !!!")
            return True
            
       
            
                     
    
    
    

# Signup view
def signup(request):
    print("Rendering signup view...")
    if request.method == 'POST':
        form = signupform(request.POST)  # Assuming SignupForm is your custom form
        if form.is_valid():
            username = form.cleaned_data['Username']
            password = form.cleaned_data['password']
            
            print(username)
            print(password)
            
            if(authenticate_user(username,password,'signup')):
                return render(request, 'success.html') 
            
            else:
                return render(request, 'alreadythere.html')
            #user = form.save()  # Save the user to the database
            #auth_login(request, user)  # Log the user in immediately after sign-up
            #return redirect('home')  # Redirect to a 'home' page or another page after successful signup
    else:
        form = signupform()

    return render(request, 'signup.html', {'form': form})

# Login view
def login_view(request):
    print("Rendering login view...")
    if request.method == 'POST':
        form = loginform(request.POST)  # Assuming LoginForm is your custom login form
        if form.is_valid():
            username = form.cleaned_data['Username']
            password = form.cleaned_data['password']
            
            print(username)
            print(password)
            
            if(authenticate_user(username,password,'login')):
                return render(request, 'community.html')   
                
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = loginform()

    return render(request, 'login.html', {'form': form})  # Render login page with form

def addevents(request):
    if request.method == 'POST':
        print("post trigered")
        form = eventform_1(request.POST)  # Assuming LoginForm is your custom login form
        if form.is_valid():
            username  =form.cleaned_data['username']
            eventname =form.cleaned_data['eventname']
            eventdate =form.cleaned_data['eventdate']
            eventtime =form.cleaned_data['eventtime']
            
            
            added=save_events(username,eventname,eventdate,eventtime)
            print("event added successfully")
            if (added):
                return render(request, 'eventadded.html')
            else:
                print("failed to add events")
         
            
            
            
    else:
        form = eventform_1()
    return render(request, 'addevents.html', {'form': form})


def list_events(request):
    
    
    event_list=get_eventlist()
    print(event_list)
    
    print("hi from list events")
    
    return render(request, 'listevents.html', {'events': event_list})
    
    