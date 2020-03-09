from django.contrib import admin
from .models import Article, ArticleCategory, File, Award, AwardCategory

class FileInline(admin.TabularInline):
	model = File

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['Title', 'Category', 'Preview', 'Text', 'Pub_date']
    inlines = [FileInline]
    extra = 0

    class Meta:
    	model = Article

class AwardAdmin(admin.ModelAdmin):
    list_display = ['Year', 'Image', 'Category']

    class Meta:
    	model = Article
   

admin.site.register(Award, AwardAdmin)
admin.site.register(AwardCategory)
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory)