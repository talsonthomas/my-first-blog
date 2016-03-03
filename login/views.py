from django.shortcuts import render


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.conf import settings
from django.core.urlresolvers import reverse


def login(request):
        next = request.GET.get('next', '/home/')
        if request.method == "POST":
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(username=username, password=password)


                if user is not None:
                        if user.is_active:
                                auth.login(request, user)
#                               return HttpResponse("<h1>Loggedin</h1>")
                                return HttpResponseRedirect(next)
                        else:
                                return HttpResponse("Inactive user.")
                else:
                        return HttpResponseRedirect(settings.LOGIN_URL)
        return render(request, "login.html", {'redirect_to': next})

def logout(request):
        auth.logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)

#@login_required
def home(request):
        return render (request, "home.html")



