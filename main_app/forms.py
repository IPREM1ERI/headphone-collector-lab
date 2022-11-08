from django.forms import ModelForm
from .models import Listened

class ListenedForm(ModelForm):
  class Meta:
    model = Listened
    fields = ['date', 'time_hrs', 'time_mins']