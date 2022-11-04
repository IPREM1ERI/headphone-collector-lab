from django.db import models

# Create your models here.

class Headphone(models.Model):
  make = models.CharField(max_length=100)
  model = models.CharField(max_length=100)
  style = models.CharField(max_length=100)
  description = models.TextField(max_length=250)

  def __str__(self):
    return (f'{self.make}: {self.model}')