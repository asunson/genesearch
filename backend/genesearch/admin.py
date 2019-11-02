from django.contrib import admin
from .models import Sample
from .models import Gene

class SampleAdmin(admin.ModelAdmin): 
    list_display = ('name',) 

class GeneAdmin(admin.ModelAdmin): 
    list_display = ('sample', 'symbol', 'fpkm') 

    # def get_samples(self, obj):
    #     return "\n".join([s.name for s in obj.sample.all()])

admin.site.register(Sample, SampleAdmin)
admin.site.register(Gene, GeneAdmin)