# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


def login_user(request):
    state = "Please log in below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                #state = "You're successfully logged in!"
                return redirect('entrycheck.views.enter', {'username': username,})
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."
    return render_to_response('registration/login.html',{'state':state, 'username': username})

def logout_view(request):
    logout(request)
    return redirect('login')