from django.urls import path
from .views import *

urlpatterns = [
    path("", mainpage),
    # path("about/", about)
]