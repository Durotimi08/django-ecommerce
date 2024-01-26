from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib import messages

def register(request):
    if request.method == "POST":
        u_form = RegistrationForm(request.POST)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, "Registration Successfull")
            return redirect("homepage")
    else:
        u_form = RegistrationForm()

    context = {"user_form": u_form}
    return render(request, "users/register.html", context)