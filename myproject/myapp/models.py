# myapp/models.py
from django.db import models

class UserInput(models.Model):
    text = models.TextField()
    sentiment = models.CharField(max_length=255, blank=True, null=True)
