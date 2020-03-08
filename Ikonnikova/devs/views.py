from django.shortcuts import render
from .models import Development, DevelopmentCategory, File
from questions.forms import QuestionForm

def myDevelopments(request):
	devs = Development.objects.order_by('-Pub_date')
	categories = DevelopmentCategory.objects.all()

	return render(request, 'my-developments.html', locals())

def development(request, development_id):
	development = Development.objects.get(id = development_id)
	sameDevelopments = Development.objects.filter(Category__id = development.Category.id)[:9]
	files = File.objects.filter(Development__id = development_id)	
	form = QuestionForm()

	return render(request, 'development.html', locals())