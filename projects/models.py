from django.db import models


class Project(models.Model):
    title= models.CharField(max_length=200)
    description= models.TextField()
    tecnologia= models.CharField(max_length=60)
    created_at =models.DateTimeField(auto_now_add=True) 
