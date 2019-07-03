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

def setCookies(request, company):
    rep = redirect('/app01/')
    rep.set_cookie('company', company)
    return rep

def addCookie(request, company):
    response = redirect('/app01/')
    # 保存cookie
    response.set_cookie('company', company)
    # 重定向
    return response

def getCookie(request):
    value = request.COOKIES.get('company',"")
    return render(request, 'app01/index.html', {'company':value})



def apphome(request):
    # 从session中获取账号, 如果能获取到, 则跳转到home页面, 否则跳转回登陆页面
    account = request.session.get('account', None)
    if account:
        return render(request, 'app01/home.html',{'account':account})
    else:
        return render(request, 'app01/login.html',{'msg':'请先登录'})
    


def applogin(request):
    if request.POST:
        name = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if name == "admin" and password == "123":
            response = redirect('/app01/apphome/')
            response.set_signed_cookie('account', name, salt='aaa')
            # 将账号信息存入session
            request.session['account']=name
            #登陆成功
            return response
        else:
            return render(request, 'app01/login.html', {'msg':"账号或密码错误"})
        
    else:
        account = request.get_signed_cookie('account',"",salt='aaa')
        return render(request, 'app01/login.html', {'account':account})

def logout(request):
    del request.session['account']
    return redirect('/app01/applogin/')