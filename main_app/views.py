from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Headphone, Equipment
from .forms import ListenedForm
from django.views.generic import ListView, DetailView


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def headphones_index(request):
  headphones = Headphone.objects.all()
  return render(request, 'headphones/index.html', { 'headphones': headphones })

def headphones_detail(request, headphone_id):
  headphone = Headphone.objects.get(id=headphone_id)
  equipment_headphone_doesnt_have = Equipment.objects.exclude(id__in = headphone.equipment.all().values_list('id'))
  listened_form = ListenedForm()
  return render(request, 'headphones/detail.html', { 
    'headphone': headphone, 'listened_form': listened_form, 'equipment': equipment_headphone_doesnt_have
  })
  
def add_listened(request, headphone_id):
  form = ListenedForm(request.POST)
  if form.is_valid():
    new_listened = form.save(commit=False)
    new_listened.headphone_id = headphone_id
    new_listened.save()
  return redirect('headphones_detail', headphone_id=headphone_id)

class HeadphoneCreate(CreateView):
  model = Headphone
  fields = ['make', 'model', 'style', 'description']

class HeadphoneUpdate(UpdateView):
  model = Headphone
  fields = ['make', 'model', 'style', 'description']

class HeadphoneDelete(DeleteView):
  model = Headphone
  success_url = '/headphones/'

class EquipmentCreate(CreateView):
  model = Equipment
  fields = '__all__'

class EquipmentList(ListView):
  model = Equipment

class EquipmentDetail(DetailView):
  model = Equipment

class EquipmentUpdate(UpdateView):
  model = Equipment
  fields = ['make', 'model']

class EquipmentDelete(DeleteView):
  model = Equipment
  success_url = '/equipment/'

def assoc_equipment(request, headphone_id, equipment_id):
  Headphone.objects.get(id=headphone_id).equipment.add(equipment_id)
  return redirect('headphones_detail', headphone_id=headphone_id)