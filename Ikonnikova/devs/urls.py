from django.urls import path

from . import views

urlpatterns = [
	path('', views.myDevelopments, name = 'myDevelopments'),
	path('development/<int:development_id>', views.development, name = 'development')
]