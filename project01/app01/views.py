from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.

def gotoIndex(request):
    if request.POST:
        name = request.POST.get('search', None)
        data = dict()
        data['kw'] = name
        return render(request, 'app01/index.html', data)
    else:
        return redirect('/app01/gotoindex')


def Homework01Login(request):
    return render(request, 'homework01/login.html')

def Homework01Register(request):
    return render(request, 'homework01/register.html')

def getData(request):
    account = request.POST.get('account')
    return HttpResponse("Hello,"+account)

def sum(request, num1, num2):
    result = num1 + num2
    return HttpResponse("结果为:{0}".format(result))

def hello(request):
    if request.POST:
        name = request.POST.get('name', None)
        result = '你好, {0}'.format(name) if name.lower() != 'monster' else '我不和怪物说话'
        return HttpResponse(result)
    else:
        return render(request, 'hello.html')

def gotoindex(request):
    return render(request, 'app01/index.html')