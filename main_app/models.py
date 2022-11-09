from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.
TYPES = (
  ('A', 'Amplifier'),
  ('D', 'DAC'),
)

class Equipment(models.Model):
  equipment_type = models.CharField(
    max_length=1,
    choices=TYPES,
    default=TYPES[0][0]
  )
  make = models.CharField(max_length=100)
  model = models.CharField(max_length=100) 

  def __str__(self):
    return self.make

  def get_absolute_url(self):
    return reverse('equipment_detail', kwargs={'pk': self.id})

# ///////////////////////////////////////////////////////////////////////////////

class Headphone(models.Model):
  make = models.CharField(max_length=100)
  model = models.CharField(max_length=100)
  style = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  equipment = models.ManyToManyField(Equipment)

  def __str__(self):
    return (f'{self.make}: {self.model}')

  def get_absolute_url(self):
      return reverse("headphones_detail", kwargs={"headphone_id": self.id})

  def listened_for_today(self):
    return self.listened_set.filter(date=date.today()).count() > 0

# /////////////////////////////////////////////////////////////////////////////

class Listened(models.Model):
  date = models.DateField('Last Session')
  time_hrs = models.IntegerField(default=0)
  time_mins = models.IntegerField(default=0)  

  headphone = models.ForeignKey(Headphone, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.time_hrs}hrs {self.time_mins}mins listened to on {self.date}'

  class Meta:
    ordering = ['-date']

