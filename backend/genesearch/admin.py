from django.contrib import admin
from .models import Sample
from .models import Gene

class SampleAdmin(admin.ModelAdmin): 
    list_display = ('name', 'description') 

class GeneAdmin(admin.ModelAdmin): 
    list_display = ('get_samples', 'symbol', 'fpkm') 

    def get_samples(self, obj):
        return "\n".join([s.name for s in obj.sample.all()])

admin.site.register(Sample, SampleAdmin)
admin.site.register(Gene, GeneAdmin)