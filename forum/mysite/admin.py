from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Category)
admin.site.register(Types)
#admin.site.register(Role)
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'number', 'user')
@admin.register(Request)
class Request(admin.ModelAdmin):
    list_display = ('person', 'type', 'datetime', 'text')
@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'type', 'datetime', 'text')




