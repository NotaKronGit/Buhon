from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

def authorization(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Пользователя ' + username + ' не существует или введен неправильный пароль.')
            return render(request, 'index.html', args)
    else:
        return render(request, 'index.html', args)


@login_required(login_url='/login/')
def main_menu(request):
    return render(request, 'base.html')


def logoutUser(request):
    logout(request)
    return redirect('login')
