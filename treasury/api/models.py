from django.db import models


# Create your models here.

class Token(models.Model):
    token_file = models.FileField(upload_to='token')
