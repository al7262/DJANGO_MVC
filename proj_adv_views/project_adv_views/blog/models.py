from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField('Publication Date', auto_now_add=True)
    photo = models.CharField('url for photo', max_length=1000, default=None)
    totComment = models.IntegerField(default=0)
    content = models.TextField()

    def __str__(self):
        return f"{self.title} ({self.date})"

class Mentor(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    year = models.IntegerField(default=0)
    quote = models.TextField()
    photo = models.CharField('url for photo', max_length=1000)

    def __str__(self):
        return f"{self.name} ({self.title})"

class Mentee(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    quote = models.TextField()
    photo = models.CharField('url for photo', max_length=1000)

    def __str__(self):
        return f"{self.name} ({self.age})"