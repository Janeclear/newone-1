from django.db import models
# Create your models here.
from django.db import models

class Test(models.Model):
    gender = (
        ('male', '男'),
        ('female', '女'),
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

class Selfinfo(models.Model):
    educations = (
        ('technical secondary school and above', '中专及以下'),
        ('jonior college', '大专'),
        #('undergratuate', '本科'),
        ('本科', '本科'),
        ('master','硕士'),
        ('doctor and above', '博士及以上'),
    )
    ages = (
        ('below 20', '20以下'),
        ('20-30', '20-30'),
        ('30-40', '30-40'),
        ('40-50', '40-50'),
        ('above 50', '50以上'),
    )
    salary = (
        ('below 3000', '3000以下'),
        ('3000-5000', '3000-5000'),
        ('5000-8000', '5000-8000'),
        ('8000-10000', '8000-10000'),
        ('above 10000', '10000以上'),
    )

    gender = (
        ('male', '男'),
        #('female', '女'),
        ('女', '女'),
    )
    name = models.CharField(max_length=50, default=0, blank=True)
    real_name = models.CharField(max_length=50, unique=True, default=0, blank=True)
    sex = models.CharField(max_length=32, choices=gender, default='男', blank=True)
    phone_number = models.CharField(max_length=11, default=0, blank=True)
    email = models.EmailField(default=0, blank=True)
    education = models.CharField(max_length=50, choices=educations,default='中专及以下', blank=True)
    major = models.CharField(max_length=50, default=0, blank=True)
    age = models.CharField(max_length=50, choices=ages, default='20以下', blank=True)
    expected_salary = models.CharField(max_length=50, choices=salary, default='3000以下', blank=True)
    home_address = models.CharField(max_length=150, default=0, blank=True)
    certificate_or_skills = models.CharField(max_length=150, default=0, blank=True)
    professional_history = models.CharField(max_length=150, default=0,  blank=True)
    experience = models.CharField(max_length=150, default=0,  blank=True)
    hobby = models.CharField(max_length=150, default=0, blank=True)
    selfintroduction = models.CharField(max_length=150, default=0,  blank=True)

    def __str__(self):
        return self.name