from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Question._meta.get_fields()]

    class Meta:
    	model = Question
    
admin.site.register(Question, QuestionAdmin)