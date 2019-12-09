from django.contrib import admin
from .models import Management, Mentee, Mentor, Subject, LiveCode, Challenge

# Register your models here.

admin.site.register(Management)
admin.site.register(Mentee)
admin.site.register(Mentor)
admin.site.register(Subject)
admin.site.register(LiveCode)
admin.site.register(Challenge)