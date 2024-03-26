from django.urls import path
from .views import *

urlpatterns = [
    path("", mainpage),
    path("py/", html_python, name="html-python")
]