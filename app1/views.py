from django.shortcuts import render
#create your views here.

from app1 import models
from newone.form import RegisterForm, UserForm, SelfinfoForm
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
    if request.method == "POST":
        selfinfo_form = SelfinfoForm(request.POST)
        if selfinfo_form.is_valid():  # 获取数据
            username = selfinfo_form.cleaned_data['username']
            real_name = selfinfo_form.cleaned_data['real_name']
            sex = selfinfo_form.cleaned_data['sex']
            phone_number = selfinfo_form.cleaned_data['phone_number']
            email = selfinfo_form.cleaned_data['email']
            education = selfinfo_form.cleaned_data['education']
            major = selfinfo_form.cleaned_data['major']
            age = selfinfo_form.cleaned_data['age']
            expected_salary = selfinfo_form.cleaned_data['expected_salary']
            home_address = selfinfo_form.cleaned_data['home_address']
            certificate_or_skills = selfinfo_form.cleaned_data['certificate_or_skills']
            professional_history = selfinfo_form.cleaned_data['professional_history']
            experience = selfinfo_form.cleaned_data['experience']
            hobby = selfinfo_form.cleaned_data['hobby']
            selfintroduction = selfinfo_form.cleaned_data['selfintroduction']
            # 当一切都OK的情况下，创建新信息
            new_selfinfo = models.Selfinfo.objects.create()
            new_selfinfo.name = username
            new_selfinfo.real_name = real_name
            new_selfinfo.sex = sex
            new_selfinfo.phone_number = phone_number
            new_selfinfo.email = email
            new_selfinfo.education = education
            new_selfinfo.major = major
            new_selfinfo.age = age
            new_selfinfo.expected_salary = expected_salary
            new_selfinfo.home_address = home_address
            new_selfinfo.certificate_or_skills = certificate_or_skills
            new_selfinfo.professional_history = professional_history
            new_selfinfo.experience = experience
            new_selfinfo.hobby = hobby
            new_selfinfo.selfintroduction = selfintroduction
            new_selfinfo.save()

            return redirect('/selfinfo_done/')  # 自动跳转到登录页面
    selfinfo_form = SelfinfoForm()
    return render(request, 'selfinfo.html', locals())

selfinfo_form=SelfinfoForm()
data={}

#dict_selfinfo = {}
def selfinfo_done(request):
    #selfinfo_formlist = models.Selfinfo.objects.all()
    #这里首先想办法得到用户名name，不知道能不能用base页面那个{{ request.session.user_name }}
    selfinfo_form = models.Selfinfo.objects.get(name='Jane')
    data = {
        "selfinfo_form": selfinfo_form
    }
    return render(request, 'selfinfo_done.html', context=data)  # locals() dict_selfinfo
    #if request.method == "POST":
        #selfinfo_formlist = models.Test.objects.all()
        # models.Selfinfo.objects.filter(real_name='王敬莹')
        # selfinfo_form=RegisterForm

        # 实例化一个图书对象，使用book.id查询该书籍数据
        # 建立空字典存储booklist
        # 存储book书名

        #selfinfo_form = models.Test.objects.get(name='Jane')
        #dict_selfinfo['name'] = selfinfo_form.name
        #dict_selfinfo['email'] = selfinfo_form.eamil

    #pass
    #return render(request, 'selfinfo_done.html',)#  locals())

def careerhelper(request):
    pass
    return render(request, 'careerhelper.html')

def Introduction(request):
    pass
    return render(request, 'Introduction.html')

def plan(request):
    pass
    return render(request, 'plan.html')
