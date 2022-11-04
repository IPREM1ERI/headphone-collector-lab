from django.shortcuts import render
from .models import Headphone

# Create your views here.
# Add the following import


# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def headphones_index(request):
  headphones = Headphone.objects.all()
  return render(request, 'headphones/index.html', { 'headphones': headphones })

def headphones_detail(request, headphone_id):
  headphone = Headphone.objects.get(id=headphone_id)
  return render(request, 'headphones/detail.html', { 'headphone': headphone })