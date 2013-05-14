from dajaxice.decorators import dajaxice_register
from dajax.core import Dajax
from infant.models import Nap

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