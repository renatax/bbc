from django.forms import ModelForm 
from django import forms
from infant.models import *

class FeedingLForm(ModelForm):
  class Meta:
    model = FeedingL

class FeedingSForm(ModelForm):
  class Meta:
    model = FeedingS

class NapForm(ModelForm):
  class Meta:
    model = Nap

class DiaperingForm(ModelForm):
  class Meta:
    model = Diapering

class RouteForm(forms.Form):
  ACTION_CHOICE = (
      ('FL', 'Feed Liqid Food'),
      ('FS', 'Feed Solid Food'),
      ('NP', 'Take A Nap'),
      ('DP', 'Change Diaper'),
  )  
  SOLID_CHOICE = (
      ('P', 'Prepared Food'),
      ('C', 'Can Food'),
      ('O', 'Other'),
  )
  LIQUID_CHOICE = (
      ('F', 'Formula'),
      ('B', 'Breast Milk'),
      ('O', 'Other'),
  )


  action = forms.ChoiceField(choices=ACTION_CHOICE)
  solid = forms.ChoiceField(choices=SOLID_CHOICE)
  liquid = forms.ChoiceField(choices=LIQUID_CHOICE)
