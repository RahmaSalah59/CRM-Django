from django.db import models

class record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.IntegerField()
    city = models.CharField(max_length=50)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    

   
