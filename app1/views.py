from django.db.models import Q, F
from django.shortcuts import render
# create your views here.
from app1 import models
from newone.form import RegisterForm, UserForm, SelfinfoForm, PlanForm, PlandoneForm, JobForm, JobnewsForm, \
    EselfinfoForm
from .models import Test
from django.shortcuts import render, redirect
from django import forms
from .static.forms import UserForm
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import re
from django.contrib import messages

# Create your views here.

# careerhelper 的子函数们
pattern = r',|\.|/|;|\'|`|\[|\]|<|>|\?|:|"|\{|\}|\~|!|@|#|\$|%|\^|&|\(|\)|-|=|\_|\+|，|。|、|；|‘|’|【|】|·|！| |…|（|）'


def cutcompare(txt, sth, score):
    result_list = re.split(pattern, txt)
    for result in result_list:
        if result in sth:
            score += 2
        print(result)
    return score


def edu_to_score(edu):  # 被eduscore引用
    global escore
    if edu == '中专及以下':
        escore = 0
    elif edu == '大专':
        escore = 1
    elif edu == '本科':
        escore = 2
    elif edu == '硕士':
        escore = 3
    elif edu == '博士及以上':
        escore = 4
    return escore


def eduscore(education, degree, major, major1, major2, major3, score):
    # 先处理degree学历
    if edu_to_score(education) >= edu_to_score(degree):
        score += 3
    # 专业匹配
    if major in major1:
        score += 3
    elif major in major2:
        score += 2
    elif major in major3:
        score += 1
    return score


def personalityscore(hobby, hobby1, hobby2, hobby3, score):  # 可用于hobby也可用于personality
    if hobby == hobby1:
        score += 3
    if hobby == hobby2:
        score += 2
    if hobby == hobby3:
        score += 1
    return score


# careerhelper 的子函数们


def index(request):  # request是什么？
    pass
    return render(request, 'index.html')  # 返回结果给浏览器


def login(request):
    global user
    if request.session.get('is_login', None):
        return redirect("/index/")
    if request.method == "POST":
        login_form = UserForm(request.POST)  # 加上global
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
                    # 及时创建计划，先只填名字，后来再改

                    return redirect("/index/")
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'login.html', locals())

    login_form = UserForm()
    return render(request, 'login.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/login/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/login/")


def elogout(request):
    if not request.session.get('is_login', None):
        return redirect("/elogin/")
    request.session.flush()
    return redirect("/elogin/")


def alogout(request):
    if not request.session.get('is_login', None):
        return render("/alogin/")
    request.session.flush()
    return redirect("/alogin/")


def planmaking(request):
    if request.method == "POST":
        plan_form = PlanForm(request.POST)
        if plan_form.is_valid():
            username = plan_form.cleaned_data['username']
            plan1 = plan_form.cleaned_data['plan1']
            plan2 = plan_form.cleaned_data['plan2']
            plan3 = plan_form.cleaned_data['plan3']

            if plan1 != '':
                models.Plan.objects.filter(name=username).update(plan1=plan1)
                models.Plandone.objects.filter(name=username).update(plan1_progress=0, plan1_learning_log='暂无记录')
            if plan2 != '':
                models.Plan.objects.filter(name=username).update(plan2=plan2)
                models.Plandone.objects.filter(name=username).update(plan2_progress=0, plan2_learning_log='暂无记录')
            if plan3 != '':
                models.Plan.objects.filter(name=username).update(plan3=plan3)
                models.Plandone.objects.filter(name=username).update(plan3_progress=0, plan3_learning_log='暂无记录')

            message = "提交成功！"

            return redirect('/ad_userinfo/')

    plan_form = PlanForm()
    return render(request, 'planmaking.html', locals())


def selfinfo(request):
    if request.method == "POST":
        selfinfo_form = SelfinfoForm(request.POST)
        if selfinfo_form.is_valid():  # 获取数据
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
            personality = selfinfo_form.cleaned_data['personality']

            if real_name != '':
                models.Selfinfo.objects.filter(name=user.name).update(real_name=real_name)
            if sex != '':
                models.Selfinfo.objects.filter(name=user.name).update(sex=sex)
            if phone_number != '':
                models.Selfinfo.objects.filter(name=user.name).update(phone_number=phone_number)
            if email != '':
                models.Selfinfo.objects.filter(name=user.name).update(email=email)
            if education != '':
                models.Selfinfo.objects.filter(name=user.name).update(education=education)
            if major != '':
                models.Selfinfo.objects.filter(name=user.name).update(major=major)
            if age != '':
                models.Selfinfo.objects.filter(name=user.name).update(age=age)
            if expected_salary != '':
                models.Selfinfo.objects.filter(name=user.name).update(expected_salary=expected_salary)
            if home_address != '':
                models.Selfinfo.objects.filter(name=user.name).update(home_address=home_address)
            if certificate_or_skills != '':
                models.Selfinfo.objects.filter(name=user.name).update(certificate_or_skills=certificate_or_skills)
            if professional_history != '':
                models.Selfinfo.objects.filter(name=user.name).update(professional_history=professional_history)
            if experience != '':
                models.Selfinfo.objects.filter(name=user.name).update(experience=experience)
            if hobby != '':
                models.Selfinfo.objects.filter(name=user.name).update(hobby=hobby)
            if selfintroduction != '':
                models.Selfinfo.objects.filter(name=user.name).update(selfintroduction=selfintroduction)
            if personality != '':
                models.Selfinfo.objects.filter(name=user.name).update(personality=personality)
            return redirect('/selfinfo_done/')  # 自动跳转到登录页面
    selfinfo_form = SelfinfoForm()
    return render(request, 'selfinfo.html', locals())


def eselfinfo(request):
    eselfinfo_forma = models.Euser.objects.get(ename=euser.ename)
    data = {
        'eselfinfo_forma': eselfinfo_forma
    }
    if request.method == "POST":
        eselfinfo_form = EselfinfoForm(request.POST)
        if eselfinfo_form.is_valid():  # 获取数据
            ename = eselfinfo_form.cleaned_data['ename']
            sex = eselfinfo_form.cleaned_data['sex']
            email = eselfinfo_form.cleaned_data['email']
            aspect = eselfinfo_form.cleaned_data['aspect']

            if sex != '':
                models.Euser.objects.filter(ename=ename).update(sex=sex)
            if email != '':
                models.Euser.objects.filter(ename=ename).update(email=email)
            if aspect != '':
                models.Euser.objects.filter(ename=ename).update(aspect=aspect)
            return redirect('/eselfinfo/')
    eselfinfo_form = EselfinfoForm()
    return render(request, 'eselfinfo.html', locals())


selfinfo_form = SelfinfoForm()
data = {}


def selfinfo_done(request):
    # selfinfo_formlist = models.Selfinfo.objects.all()
    # 这里首先想办法得到用户名name，不知道能不能用base页面那个{{ request.session.user_name }}

    selfinfo_form = models.Selfinfo.objects.get(name=user.name)
    data = {
        "selfinfo_form": selfinfo_form
    }
    return render(request, 'selfinfo_done.html', context=data)  # locals() dict_selfinfo


# 在你的函数前面加上csrf_exempt装饰器
@csrf_exempt
def careerhelper(request):
    user_a = models.Selfinfo.objects.get(name=user.name)
    education = user_a.education
    major = user_a.major
    professional_history = user_a.professional_history
    certificate_or_skills = user_a.certificate_or_skills
    hobby = user_a.hobby
    personality = user_a.personality

    joblist = models.Job.objects.all()
    for job in joblist:
        job.job_score = 0
        job.job_score = eduscore(education, job.degree, major, job.major1, job.major2, job.major3,
                                 score=0) + personalityscore(hobby, job.hobby1, job.hobby2, job.hobby3,
                                                             score=0) + personalityscore(personality, job.personality1,
                                                                                         job.personality2,
                                                                                         job.personality3,
                                                                                         score=0) + cutcompare(
            job.skill,certificate_or_skills , score=0) + cutcompare(job.experience, professional_history, score=0)
        models.Job.objects.filter(job_name=job.job_name).update(job_score=job.job_score)
    re_jobs = models.Job.objects.filter().order_by('-job_score')[:3]

    # 之前的推荐算法
    # re_jobs = models.Job.objects.filter(Q(job_name__contains=professional_history) | Q(job_name__contains=major) | Q(
    #     description__contains=professional_history) | Q(description__contains=selfintroduction) | Q(
    #     requirement__contains=certificate_or_skills) | Q(requirement__contains=major) | Q(
    #     requirement__contains=selfintroduction) | Q(skill__contains=certificate_or_skills))
    # 子函数

    data = {
        're_jobs': re_jobs
    }

    if request.method == "POST":
        jobchosena = request.POST.get('a')
        models.Selfinfo.objects.filter(name=user.name).update(jobchosen=jobchosena)

        return redirect('/careerhelper/')
    return render(request, 'careerhelper.html', locals())


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
                new_plan = models.Plan.objects.create()
                new_plan.name = username
                new_plan.save()
                # 注册时创建一条个人信息表数据，只保存下用户名字段，其他不填
                new_selfinfo = models.Selfinfo.objects.create()
                new_selfinfo.name = username
                new_selfinfo.sex = sex
                new_selfinfo.email = email
                new_selfinfo.save()
                # 注册时也创建一条计划进度数据，只保存下用户名字段，其他不填
                new_plandone = models.Plandone.objects.create()
                new_plandone.name = username
                new_plandone.save()

                return redirect('/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'register01.html', locals())


def Introduction(request):
    pass
    return render(request, 'Introduction.html')


def career(request):
    pass
    return render(request, 'career.html')


def elogin(request):
    global euser
    if request.method == "POST":
        login_form = UserForm(request.POST)  # 加上global
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                euser = models.Euser.objects.get(ename=username)
                if euser.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = euser.id
                    request.session['user_name'] = euser.ename

                    return redirect("/ad_userinfo/")
                else:
                    message = "密码不正确！"
            except:
                message = "非专家用户！"
        return render(request, 'elogin.html', locals())

    login_form = UserForm()
    return render(request, 'elogin.html', locals())


def alogin(request):
    if request.method == 'POST':
        alogin_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if alogin_form.is_valid():
            username = alogin_form.cleaned_data['username']
            password = alogin_form.cleaned_data['password']
            if username == '管理员':
                try:
                    auser = models.Test.objects.get(name='管理员')
                    if auser.password == password:
                        request.session['is_login'] = True
                        request.session['user_id'] = auser.id
                        request.session['user_name'] = auser.name
                        return redirect("/admin_eu/")
                    else:
                        message = "密码不正确！"
                except:
                    message = "非管理员用户！"
            else:
                message = "非管理员用户！"
        return render(request, 'alogin.html', locals())

    alogin_form = UserForm()
    return render(request, 'alogin.html', locals())


def ad_userinfo(request):
    selfinfo_formlist = models.Selfinfo.objects.filter(expert=euser.ename)
    plan_formlist = models.Plan.objects.filter(expert=euser.ename)
    plan_done_formlist = models.Plandone.objects.filter(expert=euser.ename)
    data = {
        "selfinfo_formlist": selfinfo_formlist,
        "plan_formlist": plan_formlist,
        "plan_done_formlist": plan_done_formlist
    }
    return render(request, 'ad_userinfo.html', context=data)


def admin_eu(request):
    selfinfo_formlist = models.Selfinfo.objects.all()
    eselfinfo_formlist = models.Euser.objects.all()
    data = {
        "selfinfo_formlist": selfinfo_formlist,
        "eselfinfo_formlist": eselfinfo_formlist,
    }

    if request.method == "POST":
        uname = request.POST.get('a')
        ename = request.POST.get('b')
        models.Selfinfo.objects.filter(name=uname).update(expert=ename)
        models.Plandone.objects.filter(name=uname).update(expert=ename)
        models.Plan.objects.filter(name=uname).update(expert=ename)
        models.Euser.objects.filter(ename=ename).update(usernumber=F('usernumber') + 1)

        return redirect('/admin_eu/')

    return render(request, 'admin_eu.html', context=data)


data_p = {}


def plan(request):
    plan_form = models.Plan.objects.get(name=user.name)
    plan_done_form = models.Plandone.objects.get(name=user.name)
    data_p = {
        "plan_form": plan_form,
        "plan_done_form": plan_done_form
    }
    return render(request, 'plan.html', context=data_p)


def plan_done(request):
    if request.method == "POST":
        # print('有POST')
        plan_done_form = PlandoneForm(request.POST)
        if plan_done_form.is_valid():
            # print('有valid判断') 是因为没有设置username required = False
            plan1_progress = plan_done_form.cleaned_data['plan1_progress']
            plan1_learning_log = plan_done_form.cleaned_data['plan1_learning_log']
            plan2_progress = plan_done_form.cleaned_data['plan2_progress']
            plan2_learning_log = plan_done_form.cleaned_data['plan2_learning_log']
            plan3_progress = plan_done_form.cleaned_data['plan3_progress']
            plan3_learning_log = plan_done_form.cleaned_data['plan3_learning_log']

            if plan1_progress != '':
                models.Plandone.objects.filter(name=user.name).update(plan1_progress=plan1_progress)
            if plan1_learning_log != '':
                models.Plandone.objects.filter(name=user.name).update(plan1_learning_log=plan1_learning_log)
            if plan2_progress != '':
                models.Plandone.objects.filter(name=user.name).update(plan2_progress=plan2_progress)
            if plan2_learning_log != '':
                models.Plandone.objects.filter(name=user.name).update(plan2_learning_log=plan2_learning_log)
            if plan3_progress != '':
                models.Plandone.objects.filter(name=user.name).update(plan3_progress=plan3_progress)
            if plan3_learning_log != '':
                models.Plandone.objects.filter(name=user.name).update(plan3_learning_log=plan3_learning_log)
            # print('有修改')
            return redirect('/plan/')
    plan_done_form = PlandoneForm()
    plan_form = models.Plan.objects.get(name=user.name)
    data = {
        "plan_form": plan_form
    }
    return render(request, 'plan_done.html', locals())  # context=data


def job(request):
    if request.method == "POST":
        job_form = JobForm(request.POST)
        if job_form.is_valid():
            job_name = job_form.cleaned_data['job_name']
            degree = job_form.cleaned_data['degree']
            major1 = job_form.cleaned_data['major1']
            major2 = job_form.cleaned_data['major2']
            major3 = job_form.cleaned_data['major3']
            skill = job_form.cleaned_data['skill']
            hobby1 = job_form.cleaned_data['hobby1']
            hobby2 = job_form.cleaned_data['hobby2']
            hobby3 = job_form.cleaned_data['hobby3']
            personality1 = job_form.cleaned_data['personality1']
            personality2 = job_form.cleaned_data['personality2']
            personality3 = job_form.cleaned_data['personality3']
            description = job_form.cleaned_data['description']
            requirement = job_form.cleaned_data['requirement']
            salary = job_form.cleaned_data['salary']
            experience = job_form.cleaned_data['experience']

            new_job = models.Job.objects.create()
            new_job.job_name = job_name
            new_job.degree = degree
            new_job.major1 = major1
            new_job.major2 = major2
            new_job.major3 = major3
            new_job.skill = skill
            new_job.hobby1 = hobby1
            new_job.hobby2 = hobby2
            new_job.hobby3 = hobby3
            new_job.personality1 = personality1
            new_job.personality2 = personality2
            new_job.personality3 = personality3
            new_job.description = description
            new_job.requirement = requirement
            new_job.experience = experience
            new_job.salary = salary

            new_job.save()
            return redirect('/job/')
    job_form = JobForm()
    return render(request, 'job.html', locals())  # context=data


def jobnews(request):
    if request.method == "POST":
        jobnews_form = JobnewsForm(request.POST)
        if jobnews_form.is_valid():
            title = jobnews_form.cleaned_data['title']
            content = jobnews_form.cleaned_data['content']

            new_jobnews = models.Jobnews.objects.create()
            new_jobnews.title = title
            new_jobnews.content = content
            new_jobnews.save()
            return redirect('/jobnews/')
    jobnews_form = JobnewsForm()
    return render(request, 'jobnews.html', locals())


def add_expert(request):
    if request.method == 'POST':
        expert_form = UserForm(request.POST)
        if expert_form.is_valid():
            username = expert_form.cleaned_data['username']
            password = expert_form.cleaned_data['password']

            new_expert = models.Euser.objects.create()
            new_expert.ename = username
            new_expert.password = password
            new_expert.save()

            return redirect('/add_expert/')
    expert_form = UserForm()
    return render(request, 'add_expert.html', locals())


def jobinfo(request):
    job_formlist = models.Job.objects.all()
    data = {
        "job_formlist": job_formlist
    }
    return render(request, 'jobinfo.html', locals())


def jobnews_show(request):
    jobnews_formlist = models.Jobnews.objects.all().order_by('-c_time')
    data = {
        "jobnews_formlist": jobnews_formlist
    }
    return render(request, 'jobnews_show.html', locals())


def jobdetail(request, nid):
    job_form = models.Job.objects.get(id=nid)
    data = {
        'job_form': job_form
    }
    return render(request, 'jobdetail.html', locals())


def jobnewsdetail(request, nid):
    jobnews_form = models.Jobnews.objects.get(id=nid)
    data = {
        'jobnews_form': jobnews_form
    }
    return render(request, 'jobnewsdetail.html', locals())


def deletejob(request, nid):
    models.Job.objects.filter(id=nid).delete()
    return redirect('/job/')


def login02(request):
    pass
    return render(request, 'login02.html')


def login_a(request):
    # html="""
    # <h2>欢迎登录！</h2>
    # <form method="post">
    #    <input type="text" name="username">
    #    <input type="password" name="password">
    #    <input type="submit" value="登录">
    # </form>
    # """
    return render(request, 'login.html')


def userinfo_test(request):
    eselfinfo_formlist = models.Euser.objects.all()
    data = {
        "eselfinfo_formlist": eselfinfo_formlist,
    }
    return render(request, 'userinfo_test.html', context=data)


def auserinfo(request):
    selfinfo_formlist = models.Selfinfo.objects.all()
    data = {
        "selfinfo_formlist": selfinfo_formlist,
    }
    return render(request, 'auserinfo.html', context=data)


def login_base(request):
    pass
    return render(request, 'login_base.html')


def jobelook(request):
    job_formlist = models.Job.objects.all()
    data = {
        "job_formlist": job_formlist
    }
    return render(request, 'jobelook.html', context=data)


def e_newscheck(request):
    jobnews_formlist = models.Jobnews.objects.all()
    data = {
        "jobnews_formlist": jobnews_formlist,
    }
    return render(request, 'e_newscheck.html', context=data)


def base(request):
    pass
    return redirect('/base/')
