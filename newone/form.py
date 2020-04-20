#！/usr/bin/env python
# -*-coding:utf-8 -*-
# Author:Jane time:2020-04-05
from django import forms

class SelfinfoForm(forms.Form):
    educations = (
        ('中专及以下', '中专及以下'),
        ('大专', '大专'),
        #('undergratuate', '本科'),
        ('本科', '本科'),
        ('硕士', '硕士'),
        ('博士及以上', '博士及以上'),
    )
    ages = (
        ('20以上', '20以下'),
        ('20-30', '20-30'),
        ('30-40', '30-40'),
        ('40-50', '40-50'),
        ('50以上', '50以上'),
    )
    salary = (
        ('3000以下', '3000以下'),
        ('3000-5000', '3000-5000'),
        ('5000-8000', '5000-8000'),
        ('8000-10000', '8000-10000'),
        ('10000以上', '10000以上'),
    )

    gender = (
        ('男', '男'),
        #('female', '女'),
        ('女', '女'),
    )
    username = forms.CharField(label="用户名　", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    real_name = forms.CharField(label="姓　名　", max_length=128, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性　别　', choices=gender)
    phone_number = forms.CharField(label="手机号码", max_length=11, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    education = forms.ChoiceField(label="学　历　", required=False, choices=educations)
    major = forms.CharField(label="专　业　", max_length=256, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.ChoiceField(label="年　龄　", required=False, choices=ages)
    expected_salary = forms.ChoiceField(label="期望月薪",required=False, choices=salary)
    home_address = forms.CharField(label="家庭住址", max_length=256, required=False, widget=forms.TextInput(attrs={'class': 'form-controla'}))
    certificate_or_skills = forms.CharField(label="证书技能", max_length=256, required=False, widget=forms.TextInput(attrs={'class': 'form-controla'}))
    professional_history = forms.CharField(label="职业经历", max_length=256, required=False, widget=forms.TextInput(attrs={'class': 'form-controla'}))
    experience = forms.CharField(label="实践经历", max_length=256, required=False, widget=forms.TextInput(attrs={'class': 'form-controla'}))
    hobby = forms.CharField(label="兴趣爱好", max_length=256, required=False, widget=forms.TextInput(attrs={'class': 'form-controla'}))
    selfintroduction = forms.CharField(label="自我介绍", max_length=256, required=False, widget=forms.TextInput(attrs={'class': 'form-controla'}))
    jobchosen = forms.CharField(label='目标职业', max_length=150, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密　码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class RegisterForm(forms.Form):
    gender = (
        ('男', "男"),
        ('女', "女"),
    )
    username = forms.CharField(label="用户名　", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密　码　", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性　别　', choices=gender)


class PlanForm(forms.Form):
    username = forms.CharField(label="用户名　", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    plan1 = forms.CharField(label="计划1", max_length=256, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    plan2 = forms.CharField(label="计划2", max_length=256, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    plan3 = forms.CharField(label="计划3", max_length=256, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))


class PlandoneForm(forms.Form):
    percent = (
        ('0', '未开始'),
        ('25%', '完成了1/4'),
        ('50%', '完成了一半'),
        ('75%', '完成了3/4'),
        ('100%', '全部完成'),
    )
    username = forms.CharField(label="用户名　", required=False, max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    plan1_progress = forms.ChoiceField(label="计划1执行进度",required=False, choices=percent)
    plan1_learning_log = forms.CharField(label="计划1学习日志", max_length=1024, required=False, widget=forms.TextInput(attrs={'class': 'form-controla'}))
    plan2_progress = forms.ChoiceField(label="计划2执行进度", required=False, choices=percent)
    plan2_learning_log = forms.CharField(label="计划2学习日志", max_length=1024, required=False, widget=forms.TextInput(attrs={'class': 'form-controla'}))
    plan3_progress = forms.ChoiceField(label="计划3执行进度", required=False, choices=percent)
    plan3_learning_log = forms.CharField(label="计划3学习日志", max_length=1024, required=False, widget=forms.TextInput(attrs={'class': 'form-controla'}))


class JobForm(forms.Form):
    job_salary = (
        ('3000以下', '3000以下'),
        ('3000-5000', '3000-5000'),
        ('5000-8000', '5000-8000'),
        ('8000-10000', '8000-10000'),
        ('10000以上', '10000以上'),
    )
    job_name = forms.CharField(label="职业名称", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label="职业描述", max_length=512, widget=forms.Textarea(attrs={'class': 'form-control'}))
    requirement = forms.CharField(label="任职资格", max_length=512, widget=forms.Textarea(attrs={'class': 'form-control'}))
    salary = forms.ChoiceField(label="薪资水平", choices=job_salary)
    character = forms.CharField(label="性格要求", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))