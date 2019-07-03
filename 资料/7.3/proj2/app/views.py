from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

def gotoIndex(request):
    return render(request, 'index.html')

def getData(request):
    # 接收请求参数
    val = request.GET.get('params',0)
    result = '请求参数的值:{0},参数的数据类型:{1}'.format(val,str(type(val)))
    return HttpResponse(result)

def add(request):
    num1 = int(request.GET.get('num1',0))
    num2 = int(request.GET.get('num2',0))
    result = num1 + num2
    return HttpResponse('计算结果:{0}'.format(result))

def bookinfo(request, bookname, year):
    result = '书名：{0},出版年份：{1}'.format(bookname, year)
    return HttpResponse(result)

def hello(request):
    # 处理post请求，接受表单提交的数据
    if request.POST:
        name = request.POST.get('inputName',None)
        result = '你好,{0}'.format(name) if name.lower() != 'monster' else '我不和怪物说话'
        return HttpResponse(result)
    else:
        # 处理get请求，跳转到hello.html页面
        return render(request, 'hello.html')

def search(request):
    if request.POST:
        # 接受表单提交的数据
        keyWords = request.POST.get('kw',None)
        # 将要传递到页面你的数据放入字典中
        data = dict()
        data['kw'] = keyWords
        return render(request, 'search.html',data)
    else:
        # return render(request, 'search.html')
        # 重定向
        return redirect('/app/gotosearch/')

def gotosearch(request):
    return render(request, 'search.html')

def addCookie(request,company):
    print('='*50)
    print(company)
    # 创建响应对象
    response = redirect('/app/index/')
    # 保存cookie
    response.set_cookie('company',company)
    
    # 重定向
    return response

def getCookie(request):
    # 从cookie中获取数据
    val = request.COOKIES.get('company',"")
    # 跳转会首页，并显示cookie的值
    return render(request, 'index.html', {'company':val})

def home(request):
    # 从session中获取账号，如果能获取到，跳转到home页面，否则跳转回登录页面
    account = request.session.get('account', None)
    if account:
        return render(request, 'home.html',{'account':account})
    else:
        return render(request, 'login.html',{'msg':'请先登录'})

def login(request):
    if request.POST:
        # 获取账号密码
        name = request.POST.get('username', None)
        pwd = request.POST.get('userpwd', None)
        if name == 'admin' and pwd == '123':
            # 将账号信息加密存入cookie
            response = redirect('/app/home/')
            response.set_signed_cookie('account',name,salt='aaa')
            # 将账号存入session
            request.session['account'] = name
            # 登录成功，跳转到home页面
            return response
        else:
            # 账号密码错误 
            return render(request, 'login.html',{'msg':'账号或密码错误'})
    else:
        # 从cookie中读取账号信息，将信息传递到页面
        account = request.get_signed_cookie('account',"", salt='aaa')
        return render(request, 'login.html',{'account':account})

def logout(request):
    # 删除session中的account
    del request.session['account']
    return redirect('/app/login/')

    

