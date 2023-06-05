from django.db import models


class Profile(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username
