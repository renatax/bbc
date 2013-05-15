# Create your views here.
from infant.models import *
from infant.forms import *
from django.shortcuts import render
from django.http import HttpResponse
#django Mixin for class-based views???
def test(request):
    return render(request,'test.html',{'routeform':RouteForm()})
