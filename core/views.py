from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "templates\home.html")

def carreras(request):
    return render(request, "templates\carreras.html")

def docentes(request):
    return render(request, "templates\carreras.html")