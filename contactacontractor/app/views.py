from django.shortcuts import render
from django.contrib.auth.models import User
from app.models import Account
from django.http import HttpResponseRedirect

def home(request):
    context = {}
    return render(request, "app/home.html", context)

def register(request):
    if request.method == "POST":
                username = request.POST.get("username")
                first_name = request.POST.get("first_name")
                last_name = request.POST.get("last_name")
                email = request.POST.get("email")
                password = request.POST.get("password")
                contractor = request.POST.get("contractor")

                user = User.objects.create_user(username = username, password = password, email = email, first_name = first_name, last_name = last_name)
                user.save()

                account = Account(user = user, first_name = first_name, last_name = last_name, balance = 0, contractor = True if contractor == "on" else False)
                account.save()
                return HttpResponseRedirect(
                       redirect_to= '/'
                )
    context = {}
    return render(request, "registration/register.html", context)

def dashboard(request):
    context = {}
    return render(request, "registration/dashboard.html", context)