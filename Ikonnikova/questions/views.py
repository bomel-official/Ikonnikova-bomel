from django.shortcuts import render, HttpResponseRedirect
from questions.forms import QuestionForm
from questions.models import Question

def questionCreate(request):
	qf = QuestionForm(request.POST)
	new_question = qf.save()
	print(request.get_full_path())

	return HttpResponseRedirect('/')
