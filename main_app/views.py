from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Headphone, Equipment
from .forms import ListenedForm
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView


class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def headphones_index(request):
  headphones = Headphone.objects.filter(user=request.user)
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

class HeadphoneCreate(LoginRequiredMixin, CreateView):
  model = Headphone
  fields = ['make', 'model', 'style', 'description']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

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

def signup(request):
  error_message = ""
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('headphones_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)