from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('exams/', views.exams, name = 'exams'),
	path('article/<int:article_id>', views.article, name = 'article'),
	path('contact/', views.contact, name = 'contact'),
	path('portfolio/', views.portfolio, name = 'portfolio'),
	path('parents/', views.parents, name = 'parents'),
	path('students/', views.students, name = 'students')
]