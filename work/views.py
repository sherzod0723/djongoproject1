from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def work1(request):
    return HttpResponse("birinchi ish kuni")


def work2(request):
    return HttpResponse("<h1>ikkinchi ish kuni</h1>")
