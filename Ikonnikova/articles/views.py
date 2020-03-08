from django.shortcuts import render
from .models import Article, File, Award
from content.models import Text, Contact, Image
from questions.forms import QuestionForm

def index(request):
	articles = Article.objects.order_by('-Pub_date')[:9]
	mainImage = Image.objects.get(id = 1)
	position = Text.objects.get(id = 1)
	quoteText = Text.objects.get(id = 2)
	quoteAuthor = Text.objects.get(id = 3)

	return render(request, 'index.html', locals())

def exams(request):
	exams = Article.objects.filter(Category__id = 6)

	return render(request, 'exams.html', locals())

def article(request, article_id):
	article = Article.objects.get(id = article_id)
	sameArticles = Article.objects.filter(Category__id = article.Category.id)[:6]
	files = File.objects.filter(Article__id = article_id)
	form = QuestionForm()

	return render(request, 'article.html', locals())

def contact(request):
	articles = Article.objects.order_by('-Pub_date')[:9]
	personalContacts = Contact.objects.filter(Category__id = 1)
	schoolContacts = Contact.objects.filter(Category__id = 2)
	school = Text.objects.get(id = 4)
	form = QuestionForm()

	return render(request, 'contact.html', locals())

def portfolio(request):	
	awards = Award.objects.order_by('-Year')
	quoteText = Text.objects.get(id = 5)
	quoteAuthor = Text.objects.get(id = 6)

	return render(request, 'portfolio.html', locals())

def parents(request):
	articles = Article.objects.filter(Category__id = 7).order_by('-Pub_date')[:9]
	section = 'Родителям'
	img = Image.objects.get(id = 7)
	text = Text.objects.get(id = 7)
	quoteText = Text.objects.get(id = 8)
	quoteAuthor = Text.objects.get(id = 9)
	form = QuestionForm()

	return render(request, 'others.html', locals())

def students(request):
	articles = Article.objects.filter(Category__id = 8).order_by('-Pub_date')[:9]
	section = 'Ученикам'
	img = Image.objects.get(id = 8)
	text = Text.objects.get(id = 10)
	quoteText = Text.objects.get(id = 11)
	quoteAuthor = Text.objects.get(id = 12)
	form = QuestionForm()

	return render(request, 'others.html', locals())