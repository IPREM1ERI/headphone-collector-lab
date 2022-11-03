from django.shortcuts import render

# Create your views here.
# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Headphones Home Page</h1>')

def about(request):
  return render(request, 'about.html')

def headphones_index(request):
  return render(request, 'headphones/index.html', { 'headphones': headphones })