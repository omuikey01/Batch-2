from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def mainpage(request):

    name = "Django Course"
    
    print(name)

    # return render(request, "index.html", {"Django" : "This is Django Class", "2nd key" : "This is a Secound Value"} )

    return render(request, "index.html", {'O12': name} )




def application(request):
    return HttpResponse("This request come from project urls -> application.urls -> application.views")


def about(request):
    return render(request, "about.html")



def html_python(request):
    key = request.GET['J90']

    print("**************************************")
    print(key)