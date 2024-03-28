from django.urls import path
from .views import *

urlpatterns = [
    path("", mainpage),
    path("py/", html_python, name="html-python"),
    path("save_data/", cokkiesFun, name="save_data_cokkies"),
    path("get_data/", getcokkiesFun, name="get_data"),
    path("data_session/", sessionFun, name="save_data_session"),
    path("get_data_session/", getsessionFun, name="get_data_session"),
]