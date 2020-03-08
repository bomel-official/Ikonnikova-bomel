from django.shortcuts import render
from .models import Regulation

def regulations(request):
	regulations = Regulation.objects.order_by('-Pub_date')	

	return render(request, 'regulations.html', locals())