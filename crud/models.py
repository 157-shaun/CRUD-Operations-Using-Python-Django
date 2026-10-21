from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=50)
    course=models.CharField(max_length=40)
    price=models.IntegerField()
    
    def __str__(self):
        return self.name