from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.



def home(request):
    return render(request, 'blog/home1.html')


def about(request):
    return render(request, 'blog/about1.html')







# def home(request):
#     return HttpResponse('hi bro ')
#
# def about(request):
#     return HttpResponse(f"biz haqimizda shu sahifada kuzatib yuborin, {request }")





# class HomePageView(TemplateView):
#     template_name = 'home.html'
#
#
#
# class AboutPageView(TemplateView):
#     template_name = 'about.html'
