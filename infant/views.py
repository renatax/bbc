from django.shortcuts import render,redirect

from infant.models import diapering,nap,feedingS,feedingL

from retro.forms import diapperingForm,napForm,feedingSForm,feedingLForm

from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def activitySelection(request):
  if request.method=='POST':
    if form.is_valid():
      


# Create your views here.
