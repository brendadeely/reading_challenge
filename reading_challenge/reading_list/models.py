from django.db import models

# Create your models here.
class Challenge(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=30)
    book = models.ManyToManyField(Book)
    completed = models

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=300)
    author = models.ManyToManyField(Author)
    num_pages = models.IntegerField()
    genre = models.CharField(max_length=20)
    published = models.DateTimeField()
    language = models.CharField(default='English')
    orig_lang = models.CharField('original language', default='English')

class Author(models.Model):
    first = models.CharField(max_length=20)
    middle = models.CharField(max_length=20)
    last = models.CharField(max_length=30)
    birth_country = models.CharField(max_length=30)
    lives_in = models.CharField(max_length=30)
