from django.db import models
import pymysql

conn = pymysql.connect(
host= "database-1.cq3zzo5swvvt.us-east-1.rds.amazonaws.com", #endpoint link
        port = 3306, # 3306
        user = 'admin', # admin
        password = 'adminireland', #adminadmin
        db = 'communitydb', #test
        )




# Create your models here.
class Login(models.Model):
    Username = models.CharField(max_length=100)  # Name of the person placing the order
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return self.Username 
    
class signup(models.Model):
    Username = models.CharField(max_length=100)  # Name of the person placing the order
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return self.Username     
    
class events_1(models.Model):
    username  =models.CharField(max_length=100)
    eventname = models.CharField(max_length=100)  # Name of the person placing the order
    eventdate = models.CharField(max_length=9)
    
    
    eventtime=models.CharField(max_length=100)  
    
    def __str__(self):
        return self.Username     
    
class edit_events(models.Model):
    
    id=models.IntegerField(primary_key=True)
    username  =models.CharField(max_length=100)
    eventname = models.CharField(max_length=100)  
    eventdate = models.CharField(max_length=9)
    eventtime=models.CharField(max_length=100)  
         
class delete_your_events(models.Model):   
    id=models.IntegerField(primary_key=True)
    username = models.CharField(max_length=100)
           
           
def verify_and_delete(id, username,global_username):
  #  global global_username
    print("entered here/....")
    
    print(username)
    
    print(global_username)
    
    try:
        cursor = conn.cursor()

        
        if global_username.upper() == username.upper():
            
            query = f"DELETE FROM myapp_events_1 WHERE id = {id}"
            
            
            print(query)
            
            cursor.execute(query)
            
            print(query)
            
            conn.commit()
            
            cursor.close()
            
            
            
            return True 
        else:
            return False  
    except Exception as e:
        
        print(f"Error during deletion: {e}")
        return False  
           

def verify_and_update(id,username,eventname,eventdate,eventtime,global_username):
    
    
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
    

def get_eventlist():
    print("called every time")
    
    cursor = conn.cursor()
    
    
    
    
    cursor.execute(f"SELECT * FROM myapp_events_1 ")  # Replace 'yourapp_events' with your actual table name
    rows = cursor.fetchall()  # Fetch all rows from the query result

    # Create a list of dictionaries representing the rows
    event_list = []
    for row in rows:
        event = {
            'eventid': row[0],
            'eventname': row[1],  
            'eventdate': row[2],  
            'eventtime': row[3],  
        }
        event_list.append(event)
        
    return event_list        
    
           