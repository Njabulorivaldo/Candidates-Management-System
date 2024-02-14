from django.db import models
from django.contrib.auth.models import User

class Candidate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    contact = models.CharField(max_length=150)
    email_add = models.EmailField(unique=True)
    notes = models.TextField(max_length=1500)
    date_added = models.DateTimeField(auto_now_add=True)
    resume = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.name
