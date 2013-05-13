from django.db import models
import datetime
from django.forms import ModelForm

class feedingL(models.Model):
  user=models.TextField()
  helper=models.TextField()
  help_type =models.TextField()
  infant=models.TextField()
  type=models.TextField()
  amount=models.TextField()
  time=models.DateTimeField(default=datetime.datetime.now)


class feedingS(models.Model):
  user=models.TextField()
  helper=models.TextField()
  help_type =models.TextField()
  infant=models.TextField()
  type=models.TextField()
  amount=models.TextField()
  time=models.DateTimeField(default=datetime.datetime.now)

class nap(models.Model):
  user=models.TextField()
  infant=models.TextField()
  startAt=models.DateTimeField(default=datetime.datetime.now)
  endAt=models.DateTimeField(default=datetime.datetime.now)

class diapering(models.Model):
  CHOICES = (
        (True, 'Yes'),
        (False, 'No'),
           )
  user=models.TextField()
  infant=models.TextField()
  type=models.TextField()
  ointment=models.BooleanField(choices = CHOICES, default = False)
  time=models.DateTimeField(default=datetime.datetime.now)

class FeedingLForm(ModelForm):
  class Meta:
    model = feedingL

class FeedingSForm(ModelForm):
  class Meta:
    model = feedingS

class napForm(ModelForm):
  class Meta:
    model = nap

class diaperingForm(ModelForm):
  class Meta:
    model = diapering


# Create your models here.
