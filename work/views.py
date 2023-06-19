from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class About(TemplateView):
    template_name = 'about.html'

def work1(request):

    return HttpResponse("birinchi ish kuni")


def work2(request):
    return HttpResponse("<h1>ikkinchi ish kuni</h1>")
