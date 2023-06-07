from django.db import models

class FormData(models.Model):
    text_input = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/')