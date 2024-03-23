from django.shortcuts import HttpResponse


def indexfun(request):
    return HttpResponse("This is a function of Project views ")