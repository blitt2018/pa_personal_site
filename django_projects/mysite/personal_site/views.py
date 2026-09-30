from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'personal_site/index.html')

def cv(request):
    return render(request, 'personal_site/cv.html')
