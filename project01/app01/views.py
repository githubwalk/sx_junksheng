from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def gotoIndex(request):
    return render(request, 'app01/index.html')


def Homework01Login(request):
    return render(request, 'homework01/login.html')

def Homework01Register(request):
    return render(request, 'homework01/register.html')

def getData(request):
    var = request.GET.get('params', 0)

    print('....{0} :::: {1}'.format(var, str(type(var))))
    return HttpResponse(var)