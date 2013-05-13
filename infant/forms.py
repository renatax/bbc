from django.forms import ModelForm
from infant.models import *
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