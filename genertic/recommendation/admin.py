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

class User_sessionAdmin(admin.ModelAdmin):
	list_display=[f.name for f in User_session._meta.fields]
admin.site.register(User_session, User_sessionAdmin)

class InformationsAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Informations._meta.fields]
admin.site.register(Informations, InformationsAdmin)

class NPArrayAdmin(admin.ModelAdmin):
	list_display=[f.name for f in NPArray._meta.fields]
admin.site.register(NPArray, NPArrayAdmin)
class OrderAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Order._meta.fields]
admin.site.register(Order, OrderAdmin)

class BoardAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Board._meta.fields]
admin.site.register(Board, BoardAdmin)
