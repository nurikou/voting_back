from django.contrib import admin
from .models import Survey, Option, Vote

# Register your models here.

admin.site.register(Survey)
admin.site.register(Option)
admin.site.register(Vote)
