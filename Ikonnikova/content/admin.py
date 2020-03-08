from django.contrib import admin
from .models import Contact, ContactCategory, Text, Image

class ContactAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Contact._meta.get_fields()]

    class Meta:
    	model = Contact

class TextAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Text._meta.get_fields()]

    class Meta:
    	model = Text

class ImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Image._meta.get_fields()]

    class Meta:
    	model = Image
    
admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactCategory)
admin.site.register(Text, TextAdmin)
admin.site.register(Image, ImageAdmin)