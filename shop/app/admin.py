from django.contrib import admin
from .models import Fruits,Contact

# Register your models here.
@admin.register(Fruits)
class amdmin(admin.ModelAdmin):
    list_display=['id','name','about',]
@admin.register(Contact)
class admincotact(admin.ModelAdmin):
    list_display=['id','name','number','email','message']
