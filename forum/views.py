from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def fhome(request):
    return render(request, "forum/forum.html")

def question(request):
	return render(request, "forum/question.html")	