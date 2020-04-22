from django.db import models
# Create your models here.
from django.db import models

class Test(models.Model):
    gender = (
        ('男', '男'),
        ('女', '女'),
    )
    name = models.CharField(max_length=50,default=0,unique=True,blank=True)
    password = models.CharField(max_length=50,default=0,blank=True)
    #email=models.CharField(max_length=50)
    email = models.EmailField(default=0,unique=True,blank=True)
    sex = models.CharField(max_length=32, choices=gender, default='男',blank=True)
    c_time = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'

class Jobnews(models.Model):
    title = models.CharField(max_length=128, default='无标题', blank=True)
    content = models.CharField(max_length=4096, default='未编辑',blank=True)
    c_time = models.DateTimeField(auto_now_add=True, null=True,blank=True)
    def __str__(self):
        return  self.title
    class Meta:
        ordering = ['c_time']
        verbose_name = '职业资讯'
        verbose_name_plural = '职业资讯'


class Selfinfo(models.Model):
    educations = (
        ('中专及以下', '中专及以下'),
        ('大专', '大专'),
        #('undergratuate', '本科'),
        ('本科', '本科'),
        ('硕士','硕士'),
        ('博士及以上', '博士及以上'),
    )
    ages = (
        ('20以下', '20以下'),
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
        ('above 10000', '10000以上'),
    )

    gender = (
        ('男', '男'),
        #('female', '女'),
        ('女', '女'),
    )
    name = models.CharField(max_length=50, unique=True, default=0, blank=True)
    real_name = models.CharField(max_length=50, default='未填写', blank=True)
    sex = models.CharField(max_length=32, choices=gender, default='男', blank=True)
    phone_number = models.CharField(max_length=11, default='未填写', blank=True)
    email = models.EmailField(default=0, blank=True)
    education = models.CharField(max_length=50, choices=educations,default='中专及以下', blank=True)
    major = models.CharField(max_length=50, default='未填写', blank=True)
    age = models.CharField(max_length=50, choices=ages, default='20以下', blank=True)
    expected_salary = models.CharField(max_length=50, choices=salary, default='3000以下', blank=True)
    home_address = models.CharField(max_length=150, default='未填写', blank=True)
    certificate_or_skills = models.CharField(max_length=150, default='未填写', blank=True)
    professional_history = models.CharField(max_length=150, default='未填写',  blank=True)
    experience = models.CharField(max_length=150, default='未填写',  blank=True)
    hobby = models.CharField(max_length=150, default='未填写', blank=True)
    selfintroduction = models.CharField(max_length=150, default='未填写',  blank=True)
    jobchosen = models.CharField(max_length=150, default='尚未确定', blank=True)

    def __str__(self):
        return self.name

class Plan(models.Model):
    name = models.CharField(max_length=50,default=0, unique=True, blank=True)
    plan1 = models.CharField(max_length=256, default='专家尚未制定，请耐心等待', blank=True)
    plan2 = models.CharField(max_length=256, default='专家尚未制定，请耐心等待', blank=True)
    plan3 = models.CharField(max_length=256, default='专家尚未制定，请耐心等待', blank=True)

    def __str__(self):
        return self.name


class Plandone(models.Model):
    percent = (
        ('0', '未开始'),
        ('25%', '完成了1/4'),
        ('50%', '完成了一半'),
        ('75%', '完成了3/4'),
        ('100%', '全部完成'),
    )

    name = models.CharField(max_length=50, default=0, unique=True, blank=True)
    plan1_progress = models.CharField(max_length=50, choices=percent, default='未开始', blank=True)
    plan1_learning_log = models.CharField(max_length=1024, default='暂无记录', blank=True)
    plan2_progress = models.CharField(max_length=50, choices=percent, default='未开始', blank=True)
    plan2_learning_log = models.CharField(max_length=1024, default='暂无记录', blank=True)
    plan3_progress = models.CharField(max_length=50, choices=percent, default='未开始', blank=True)
    plan3_learning_log = models.CharField(max_length=1024, default='暂无记录', blank=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    job_salary = (
        ('3000以下', '3000以下'),
        ('3000-5000', '3000-5000'),
        ('5000-8000', '5000-8000'),
        ('8000-10000', '8000-10000'),
        ('10000以上', '10000以上'),
    )
    job_name = models.CharField(max_length=100, default=0, unique=True, blank=True)
    description = models.CharField(max_length=512, default=0, blank=True)
    requirement = models.CharField(max_length=512, default=0, blank=True)
    salary = models.CharField(max_length=32, choices=job_salary, default='3000以下', blank=True)
    character = models.CharField(max_length=256, default=0, blank=True)

    def __str__(self):
        return self.job_name


