from django.shortcuts import render, redirect
from .forms import SignInForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout


def index(request):
    return render(request, "SoilQMS/index.html")


def about(request):
    return render(request, "SoilQMS/about.html")


def service(request):
    return render(request, "SoilQMS/service.html")


def signin(request):
    if request.method == "POST":
        if request.POST["action"] == "signin":
            form = SignInForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)  # Authenticate the user
                if user is not None:
                    login(request, user)
                    return redirect('index')
            else:
                signup_form = CustomUserCreationForm()
                for field in signup_form.fields:
                    signup_form.fields[field].widget.attrs['class'] = 'form-control'

                for field in form.fields:
                    form.fields[field].widget.attrs['class'] = 'form-control'

                return render(request, "SoilQMS/signin.html", {
                    "signin_form": form,
                    "signup_form": signup_form
                })

        elif request.POST["action"] == "signup":
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')  # Use 'password1' since it's the raw password
                user = authenticate(username=username, password=password)  # Authenticate the user
                login(request, user)
                return redirect("index")
            else:
                signin_form = SignInForm()
                for field in signin_form.fields:
                    signin_form.fields[field].widget.attrs['class'] = 'form-control'

                for field in form.fields:
                    form.fields[field].widget.attrs['class'] = 'form-control'

                return render(request, "SoilQMS/signin.html", {
                    "signin_form": signin_form,
                    "signup_form": form,
                    "switch": True
                })

    signin_form = SignInForm()
    for field in signin_form.fields:
        signin_form.fields[field].widget.attrs['class'] = 'form-control'

    signup_form = CustomUserCreationForm()
    for field in signup_form.fields:
        signup_form.fields[field].widget.attrs['class'] = 'form-control'

    return render(request, "SoilQMS/signin.html", {
        "signin_form": signin_form,
        "signup_form": signup_form
    })


def signout(request):
    logout(request)
    return redirect('index')


def why(request):
    return render(request, "SoilQMS/why.html")


def crop_list(request):
    return render(request, "SoilQMS/list.html")


def check(request):
    return render(request, "SoilQMS/check.html")

