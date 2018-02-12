from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	context_dict = {'boldmessage': "I am bold font from the context"}
	return render(request, 'rango/index.html', context_dict)
	#return HttpResponse("Hello ... is it me your looking for! <br/> <a href='/rango/about/'>About</a>")
def about(request):
	return HttpResponse("So you want to know all about rango huh? <br/> <a href='/rango/'>Index</a>")