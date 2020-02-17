from django.contrib import admin
from .models import WeighIn
from .models import Shed
from .models import Feed
from .models import Measurement
from .models import DailyCheck

class WeighInAdmin(admin.ModelAdmin):
    list_display = ('animal', 'weight', 'date')

class ShedAdmin(admin.ModelAdmin):
    list_display = ('animal', 'date', 'success')

class FeedAdmin(admin.ModelAdmin):
    list_display = ('animal', 'date', 'feed', 'feed_weight', 'success')

class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('animal', 'date', 'measurement')

class DailyCheckAdmin(admin.ModelAdmin):
    list_display = ('animal', 'date', 'water_changed', 'animal_seen', 'temperature_measured')        
  
admin.site.register(WeighIn, WeighInAdmin)
admin.site.register(Shed, ShedAdmin)
admin.site.register(Feed, FeedAdmin)
admin.site.register(Measurement, MeasurementAdmin)
admin.site.register(DailyCheck, DailyCheckAdmin)