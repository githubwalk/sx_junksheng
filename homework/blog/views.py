from django.shortcuts import render, redirect

from django.http import HttpResponse

# Create your views here.

def index(request):
    # 从session中获取账号, 如果能获取到, 则跳转到home页面, 否则跳转回登陆页面
    account = request.session.get('account', None)
    if account:
        return render(request, 'index.html',{'account':account})
    else:
        return render(request, 'login.html',{'msg':'请先登录'})
   
def login(request):
    if request.POST:
        name = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if name == "admin" and password == "123":
            response = redirect('/index/')
            response.set_signed_cookie('account', name, salt='aaa')
            # 将账号信息存入session
            request.session['account']=name
            #登陆成功, 返回主页
            return response
        else:
            return render(request, 'login.html', {'msg':"账号或密码错误"})
        
    else:
        account = request.get_signed_cookie('account',"",salt='aaa')
        return render(request, 'login.html', {'account':account})

def regtips(request):
    return render(request, 'regtips.html')

def register(request):
    if request.POST:
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        name = request.POST.get('name', None)
        sex = request.POST.get('sex', None)
        signature = request.POST.get('signature', None)
        message = dict()
        message['username'] = username
        message['password'] = password
        message['name'] = name
        message['sex'] = sex
        message['signature'] = signature
        return render(request, 'regtips.html', message)
    else:
        return render(request, 'register.html')