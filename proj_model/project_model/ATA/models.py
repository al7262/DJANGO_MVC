from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Management(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=13)
    position = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.position})"

class Mentee(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=13)
    absentNum = models.CharField(max_length=100)
    averageScore = models.DecimalField(decimal_places=2, max_digits=5, validators=[MaxValueValidator(100), MinValueValidator(1)])

    def __str__(self):
        return f"{self.name} ({self.absentNum})"


class Subject(models.Model):
    name =  models.CharField(max_length=200)
    startTime = models.DateTimeField('Started at')
    endTime = models.DateTimeField('Ended at')

    def __str__(self):
        return self.name

class Mentor(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=13)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Challenge(models.Model):
    name =  models.CharField(max_length=200)
    questionNum = models.IntegerField(default=0)
    scoreWeight = models.DecimalField(decimal_places=0, max_digits=3, validators=[MaxValueValidator(100), MinValueValidator(1)])
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class LiveCode(models.Model):
    name =  models.CharField(max_length=200)
    questionNum = models.IntegerField(default=0)
    scoreWeight = models.DecimalField(decimal_places=0, max_digits=3, validators=[MaxValueValidator(100), MinValueValidator(1)])
    date = models.DateTimeField('Scheduled at')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name