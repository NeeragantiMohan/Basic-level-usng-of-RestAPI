from django.contrib import admin
from restapp.models import Employee


# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','name','no','role','location','salary']
admin.site.register(Employee,EmployeeAdmin)