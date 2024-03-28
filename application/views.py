from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
name1 = "Django"

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


def cokkiesFun(request):

    name1 = request.GET['n1']
    email1 = request.GET['e1']
    pass1 = request.GET['p1']
 

    data = render(request, "about.html")

    data.set_cookie('Localname', name1),
    data.set_cookie("Localemail", email1),
    data.set_cookie("LocalPass", pass1),
    data.set_cookie("myValue", "Just Demo"),
    
    return data


def getcokkiesFun(req) :
    # name = req.cookie.get('Localname')
    name = req.COOKIES.get('Localname')
    mail = req.COOKIES.get("LocalPass")
    my = req.COOKIES.get("myValue")
    # csrf = req.COOKIES.get('csrftoken')

    print("*****************************")
    print(name)
    print(mail)
    print(my)
    # print(csrf)

    print("*****************************")
    return HttpResponse("Data get from Cookies")


def sessionFun(request):
    val1 = request.GET['n2']
    val2 = request.GET['e2']
    val3 = request.GET['p2']

    request.session["key"] = "value"

    request.session["v1"] = val1
    request.session["v2"] = val2
    request.session["v3"] = val3
    # request.session['ur_name'] = name1
    return HttpResponse("Data Save")

def getsessionFun(request):

    session_name = request.session.get("v1")
    print("***************************")
    print(session_name)
    print("***************************")

    return HttpResponse("Data get from Session")
