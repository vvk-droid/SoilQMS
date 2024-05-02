from django.shortcuts import render, redirect
from .forms import SignInForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
import numpy as np
import requests
import json

from .models import *


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


def ts_data():
    url = "https://api.thingspeak.com/channels/2511441/feeds.json?results=1"
    try:
        response = requests.get(url)
        datas = json.loads(response.text)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            return datas['feeds'][0]["field1"], datas['feeds'][0]["field2"], datas['feeds'][0]["field3"], \
                datas['feeds'][0]["field4"]
        else:
            print(f"Error: GET request failed with status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print("Error:", e)


target_names = ['Healthy', 'Diseased']


def predict(request):
    data = ts_data()
    print(data)
    if data is None:
        data = [0, 0, 0, 0]

    res = ""
    res1 = ""

    if request.method == "POST":
        print(request.POST)
        ph = float(request.POST['ph']) - 32

        temp = request.POST['temp']
        moisture = request.POST['moisture']
        humidity = request.POST['humidity']
        n = request.POST['n']
        p = request.POST['p']
        k = request.POST['k']
        res = "All Good"

        crop = Crop.objects.get(name=request.POST['crop'])
        ideal_ph = crop.ph_value
        ideal_temp = crop.temperature
        ideal_moisture = crop.moisture
        ideal_humidity = crop.humidity
        ideal_n = crop.nitrogen
        ideal_p = crop.phosphorous
        ideal_k = crop.potassium

        match crop.name:
            case "TOMATO":
                if int(moisture) > 400:
                    res = "Soil moisture is almost dry please fill the water"
                elif int(moisture) < 200:
                    res = "Moisture level is good"
                elif 200 < int(moisture) < 300:
                    res = "Moisture level is average"
                print('\n')

                if 25 <= float(temp) <= 30:
                    res1 += "Temperature is within the ideal range. "
                elif float(temp) < 25:
                    res1 += "Temperature is too low. Consider providing additional warmth. "
                else:
                    res1 += "Temperature is too high. Consider providing shade or cooling measures. "

                if 70 <= float(humidity) <= 90:
                    res1 += "Humidity is within the ideal range. "
                elif float(humidity) < 70:
                    res1 += "Humidity is too low. Consider increasing moisture levels. "
                else:
                    res1 += "Humidity is too high. Consider improving ventilation. "

                # pH conditions
                if 5.5 <= float(ph) <= 7:
                    res1 += "pH is within the ideal range. "
                elif float(ph) < 5.5:
                    res1 += "pH is too acidic. Consider adding lime to raise pH. "
                else:
                    res1 += "pH is too alkaline. Consider adding sulfur to lower pH. "
            # case "GREEN GRAM"
            #     hre code for green gram
            # case "BRINJAL":
            #     here code for brinjal
            # case ........ etc...

    return render(request, "SoilQMS/userprofile.html",
                  {"ph": float(data[2]) - 28, "temp": data[0], 'humidity': data[1], 'moisture': data[3], "result": res,
                   "result1": res1})
