from django.contrib import admin
from .models import Headphone, Listened, Equipment

# Register your models here.

admin.site.register(Headphone)
admin.site.register(Listened)
admin.site.register(Equipment)
