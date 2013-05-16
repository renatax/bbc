from dajaxice.decorators import dajaxice_register
from dajax.core import Dajax
from infant.models import Nap
from infant.forms import * 
from django.core import serializers
@dajaxice_register

def say_hello(request,pk):
    dajax = Dajax()
    nap = Nap.objects.get(pk=pk)
    print nap.user
    dajax.assign('#idUser', 'innerHTML', nap.user)
    dajax.assign('#idInfant', 'innerHTML', nap.infant)
    dajax.alert("Hello World!")
    return dajax.json()

@dajaxice_register
def multiply(request, a, b):
    dajax = Dajax()
    result = int(a) * int(b)
    dajax.assign('#result','value',str(result))
    return dajax.json()
@dajaxice_register
def test(request):
    dajax = Dajax()
    dajax.alert("Nap")
    return dajax.json()
@dajaxice_register
def echo_select(request, option):
    dajax = Dajax()
    dajax.alert(option)
    return dajax.json()

@dajaxice_register
def action_select(request, option):
    dajax = Dajax()
    out = []
    if option is not u'':
        if option == u'FL':
            form = FeedingLiquidsForm()
        elif option == u'FS':
            form = FeedingSolidsForm()
        elif option == u'NP':
            form = NapForm()
        elif option == u'DP':
            form = DiaperingForm()
        out.append(form.as_table())
        dajax.assign('#id_form2','innerHTML', out)
    return dajax.json()

