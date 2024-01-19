from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


# Create your views here.
def profile(request):
    return render(request, "profile.html")


def register(request):
    if request.method == "POST":
        register_form = forms.RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect("register")

    else:
        register_form = forms.RegistrationForm()
    mail_subject = "Registration Email"
    message = render_to_string("reg_msg.html", {"user": request.user})
    to_email: request.user.email
    send_email = EmailMessage(mail_subject, message, to=[to_email])
    send_email.send()
    return render(
        request, "authentication.html", {"form": register_form, "type": "Registration"}
    )


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data["username"]
            user_pass = form.cleaned_data["password"]
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                print("Normal uSER")
                login(request, user)
                return redirect("profile")

            else:
                return redirect("register")
    else:
        form = AuthenticationForm()
        return render(request, "authentication.html", {"form": form, "type": "Login"})


def user_logout(request):
    logout(request)
    return redirect("user_login")
