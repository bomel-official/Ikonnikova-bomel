from django.contrib import admin
from .models import Development, DevelopmentCategory, File

class FileInline(admin.TabularInline):
	model = File

class DevelopmentAdmin(admin.ModelAdmin):
    list_display = ['Title', 'Category', 'Preview', 'Text', 'Pub_date']   
    inlines = [FileInline]
    extra = 0

    class Meta:
    	model = Development


admin.site.register(Development, DevelopmentAdmin)
admin.site.register(DevelopmentCategory)