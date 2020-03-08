from django.contrib import admin
from .models import Regulation


class RegulationAdmin(admin.ModelAdmin):
    list_display = ['Title', 'Preview', 'Text', 'Pub_date', 'File']   
    extra = 0

    class Meta:
    	model = Regulation

admin.site.register(Regulation, RegulationAdmin)