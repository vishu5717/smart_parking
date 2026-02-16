from django.http import HttpResponse
from django.shortcuts import render


def test (request):
    return HttpResponse("I AM VISHVA")

def aboutus (request): 
    return render(request,"aboutus.html")