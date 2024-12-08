from django.db import models
import pymysql






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
           