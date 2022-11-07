from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Headphone

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

class HeadphoneCreate(CreateView):
  model = Headphone
  fields = '__all__'

class HeadphoneUpdate(UpdateView):
  model = Headphone
  fields = ['make', 'model', 'style', 'description']

class HeadphoneDelete(DeleteView):
  model = Headphone
  success_url = '/headphones/'