from django.shortcuts import render

def notes(request):
	return render(request, 'frontend/notes.html')

# Create your views here.
