from django.db import models

# Create your models here.
class Challenge(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=30)
    book = models.CharField(max_length=100)

    def __str__(self):
        return self.title
