from django.contrib import admin
from .models import *

# Register your models here.
class PopulationsAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Populations._meta.fields]
admin.site.register(Populations, PopulationsAdmin)

# Register your models here.
class MenuesAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Menues._meta.fields]
admin.site.register(Menues, MenuesAdmin)

class StoreAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Store._meta.fields]
admin.site.register(Store, StoreAdmin)

class StoreByUserAdmin(admin.ModelAdmin):
	list_display=[f.name for f in StoreByUser._meta.fields]
admin.site.register(StoreByUser, StoreByUserAdmin)

class InformationsAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Informations._meta.fields]
admin.site.register(Informations, InformationsAdmin)
