from django.db import models

# Create your models here.

class Animal(models.Model):
    name = models.CharField(max_length=200)
    species = models.CharField(max_length=200)
    weight = models.IntegerField(default=0)
    age = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.species})"

class Cage(models.Model):
    name = models.CharField(max_length=200)
    area = models.IntegerField(default=0)
    animals = models.ManyToManyField(Animal)

    def __str__(self):
        return f"{self.name} ({self.area}m)"

class Guard(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=13)
    schedule = models.TimeField('Shift Time')

    def __str__(self):
        return self.name

class Visitor(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=13)
    visitDay = models.DateField('Visit Day')

    def __str__(self):
        return self.name

