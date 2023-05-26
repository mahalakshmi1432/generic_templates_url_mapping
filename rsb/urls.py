from django.urls import path
from rsb.views import *
app_name='tomorrow'
urlpatterns=[
    path('virat/',virat,name='virat'),
]