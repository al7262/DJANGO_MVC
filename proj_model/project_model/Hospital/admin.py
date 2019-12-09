from django.contrib import admin

from .models import Doctor, Patient, Medicines, Prescription

# Register your models here.

admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Medicines)
admin.site.register(Prescription)