from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
@login_required(login_url='/')
def home_view(request):
    context = {'html_title': 'WELCOME HOME'}
    return render(request, 'home.html', context)

def login_view(request):
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = str(request.POST.get('username')).lower()
        password = str(request.POST.get('password'))
        if (len(username) > 45 or len(password) > 50) or (len(username) == 0 or len(password) == 0):
            return redirect('/')

        user = authenticate(request=request,
                            username=username,
                            password=password)
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                login(request, user)
                return redirect('account:home')
                # return HttpResponse('Logged in')
        else:
            return HttpResponse('Login Failed. Plaese check username or password supplied.')
    else:
        return HttpResponse('Invalid Login')
    return


@login_required()
def logout_view(request):
    logout(request)
    return redirect('account:home')
