from django.db import models

# Create your models here.


class Users(models.Model):
    username = models.CharField(max_length=155, unique=True)
    password = models.CharField(max_length=155)

    def __str__(self):
        return self.username

class Tasks(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
