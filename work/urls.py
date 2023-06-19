from django.urls import path
from .views import work1, work2


urlpatterns =[
    path('work1/', work1, name='work'),
    path('work2/',work2, name='work2')
]