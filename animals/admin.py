from django.contrib import admin
from .models import Animal
from .models import Species

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_acquired', 'owner', 'species')
    list_filter = ("owner",)
    search_fields = ['name']

admin.site.register(Animal, AnimalAdmin)
admin.site.register(Species)