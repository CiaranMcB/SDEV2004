from django.urls import path
from about.views import *

urlpatterns = [
    path('', index, name='index'),
]
