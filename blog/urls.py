from django.urls import path
from .views import home, about



urlpatterns =[
    path('home/', home, name='home'),
    path('about/', about, name='about_page'),


]