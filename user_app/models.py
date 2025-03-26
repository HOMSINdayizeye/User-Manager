# Create your models here.
from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.fname} {self.lname}"
