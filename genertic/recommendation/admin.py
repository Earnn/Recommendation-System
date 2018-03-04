from django.contrib import admin
from .models import *

# Register your models here.
class PopulationsAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Populations._meta.fields]
admin.site.register(Populations, PopulationsAdmin)