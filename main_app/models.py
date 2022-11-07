from django.db import models
from django.urls import reverse

# Create your models here.

class Headphone(models.Model):
  make = models.CharField(max_length=100)
  model = models.CharField(max_length=100)
  style = models.CharField(max_length=100)
  description = models.TextField(max_length=250)

  def __str__(self):
    return (f'{self.make}: {self.model}')

  def get_absolute_url(self):
      return reverse("headphones_detail", kwargs={"headphone_id": self.id})

class Listened(models.Model):
  date = models.DateField('Last Session')
  time_hrs = models.IntegerField(default=0)
  time_mins = models.IntegerField(default=0)  

  headphone = models.ForeignKey(Headphone, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.time_hrs}hrs {self.time_mins}mins listened to on {self.date}'