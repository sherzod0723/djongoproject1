from django.urls import path
from .views import work1, work2, HomePageView, About


urlpatterns =[
    path('work1/', work1, name='work'),
    path('work2/', work2, name='work2'),
    path('', HomePageView.as_view(), name='home'),
    path('about3/', About.as_view(), name='about')
]