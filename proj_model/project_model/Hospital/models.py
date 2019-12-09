from django.db import models

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=13)
    specialization = models.CharField(max_length=100)
    schedule = models.DateTimeField('Practice Schedule')

    def __str__(self):
        return f"{self.name} ({self.specialization})"

class Patient(models.Model):
    doctors = models.ManyToManyField(Doctor)
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=13)
    address = models.CharField(max_length=500)
    complain = models.TextField()

    def __str__(self):
        return self.name

class Medicines(models.Model):
    name = models.CharField(max_length=200)
    ingredient = models.TextField()
    effect = models.TextField()

    def __str__(self):
        return self.name

class Prescription(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    totalPrice = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    medicines = models.ManyToManyField(Medicines)

    def __str__(self):
        return f"Perscription for {self.patient}"