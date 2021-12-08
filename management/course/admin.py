from django.contrib import admin
from  course.models import Orgdetail,Empdetail

# Register your models here.

@admin.register(Orgdetail)
class OrgdetailAdmin(admin.ModelAdmin):
    list_display=['id','name','register_on','last_modified']

@admin.register(Empdetail)
class EmpdetailAdmin(admin.ModelAdmin):
    list_display=['id','name','orgdetail','register_on','last_modified']
