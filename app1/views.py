from django.shortcuts import render

#create your views here.

from app1 import models
from newone.form import RegisterForm, UserForm
from .models import Test
from django.shortcuts import render, redirect
from django import forms
from .static.forms import UserForm
from django.shortcuts import render, HttpResponse
# Create your views here.

def index(request): #request是什么？
    pass
    return render(request,'index.html')#返回结果给浏览器
#改名
def login(request):
    if request.session.get('is_login', None):
        return redirect("/index/")
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.Test.objects.get(name=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect("/index/")
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'login.html', locals())

    login_form = UserForm()
    return render(request, 'login.html', locals())

#def register(request):
#    pass
#    return render(request, 'register.html')

def register01(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'register01.html', locals())
            else:
                same_name_user = models.Test.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'register01.html', locals())
                same_email_user = models.Test.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'register01.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = models.Test.objects.create()
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'register01.html', locals())

def login02(request):
    pass
    return render(request, 'login02.html')

def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/index/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/index/")

def base(request):
    pass
    return redirect('/base/')

def login_a(request):
    #html="""
    #<h2>欢迎登录！</h2>
    #<form method="post">
    #    <input type="text" name="username">
    #    <input type="password" name="password">
    #    <input type="submit" value="登录">
    #</form>
    #"""
    return render(request,'form.html')

def selfinfo(request):
    pass
    return render(request, 'selfinfo.html')

def careerhelper(request):
    pass
    return render(request, 'careerhelper.html')
def Introduction(request):
    pass
    return render(request, 'Introduction.html')
