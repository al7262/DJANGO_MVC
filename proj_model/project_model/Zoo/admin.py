from django.contrib import admin

from .models import Animal, Cage, Guard, Visitor

# Register your models here.

admin.site.register(Animal)
admin.site.register(Cage)
admin.site.register(Guard)
admin.site.register(Visitor)