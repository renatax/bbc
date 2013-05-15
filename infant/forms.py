from django.forms import ModelForm 
from django import forms
from infant.models import *

class FeedingLiquidsForm(ModelForm):
  class Meta:
    model = FeedingLiquids
    exclude = ['user']

class FeedingSolidsForm(ModelForm):
  class Meta:
    model = FeedingSolids
    exclude = ['user']
class NapForm(ModelForm):
  class Meta:
    model = Nap
    exclude = ['user']
class DiaperingForm(ModelForm):
  class Meta:
    model = Diapering
    exclude = ['user']
class RouteForm(forms.Form):
  ACTION_CHOICE = (
      ('',   '-- choose an action --'),
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
  action.widget.attrs["onchange"]="Dajaxice.infant.action_select(Dajax.process, {'option':this.value})"