from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    #return HttpResponse("<h1>Ola, tudo bem?<h1>")
    return render(request, "home.html")
