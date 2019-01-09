from django.db import models

# Create your models here.
class UserDetails(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    Gender = models.TextField()
    berth_perference = models.TextField()
    status = models.TextField(null=True)
    coach = models.TextField()

