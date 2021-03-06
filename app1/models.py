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

class Euser(models.Model):
    gender = (
        ('男', '男'),
        ('女', '女'),
    )
    ename = models.CharField(max_length=50, default=0, unique=True, blank=True)
    password = models.CharField(max_length=50, default=0, blank=True)
    # email=models.CharField(max_length=50)
    email = models.EmailField(default=0, blank=True)
    sex = models.CharField(max_length=32, choices=gender, default='男', blank=True)
    c_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    aspect = models.CharField(max_length=128, default='未填写', blank=True)
    usernumber = models.SmallIntegerField(default=0, blank=True)

    def __str__(self):
        return self.ename

    class Meta:
        ordering = ['c_time']
        verbose_name = '专家'
        verbose_name_plural = '专家'


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
        ('本科', '本科'),
        ('硕士', '硕士'),
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

    hobbies = (
        ('常规型', '常规型'),
        ('艺术型', '艺术型'),
        ('企业型', '企业型'),
        ('社会型', '社会型'),
        ('研究型', '研究型'),
        ('现实型', '现实型'),
    )

    gender = (
        ('男', '男'),
        #('female', '女'),
        ('女', '女'),
    )

    personalities = (
        ('ISTJ稽查员', 'ISTJ稽查员'),
        ('ISFJ保护者', 'ISFJ保护者'),
        ('ISTP操作者/演奏者', 'ISTP操作者/演奏者'),
        ('ISFP作曲家/艺术家', 'ISFP作曲家/艺术家'),
        ('INFJ咨询师', 'INFJ咨询师'),
        ('INFP治疗师/导师','INFP治疗师/导师'),
        ('INTJ智多星/科学家', 'INTJ智多星/科学家'),
        ('INTP建筑师/设计师', 'INTP建筑师/设计师'),
        ('ESTJ督导', 'ESTJ督导'),
        ('ESFJ供给者/销售员', 'ESFJ供给者/销售员'),
        ('ESTP发起者/创设者','ESTP发起者/创设者'),
        ('ESFP表演者/示范者', 'ESFP表演者/示范者'),
        ('ENFJ教师', 'ENFJ教师'),
        ('ENFP倡导者/激发者', 'ENFP倡导者/激发者'),
        ('ENTJ统帅/调度', 'ENTJ统帅/调度'),
        ('ENTP发明家', 'ENTP发明家'),
    )

    name = models.CharField(max_length=50, unique=True, default=0, blank=True)
    real_name = models.CharField(max_length=50, default='未填写', blank=True)
    sex = models.CharField(max_length=32, choices=gender, default='男', blank=True)
    phone_number = models.CharField(max_length=11, default='未填写', blank=True)
    email = models.EmailField(default=0, blank=True)
    education = models.CharField(max_length=50, choices=educations,default='中专及以下', blank=True)
    major = models.CharField(max_length=50, default='未填写', blank=True)
    age = models.CharField(max_length=50, choices=ages, default='20以下', blank=True)
    hobby = models.CharField(max_length=150, choices=hobbies, default='未填写', blank=True)
    personality = models.CharField(max_length=150, choices=personalities, default='未填写', blank=True)
    expected_salary = models.CharField(max_length=50, choices=salary, default='3000以下', blank=True)
    home_address = models.CharField(max_length=150, default='未填写', blank=True)
    certificate_or_skills = models.CharField(max_length=150, default='未填写', blank=True)
    professional_history = models.CharField(max_length=150, default='未填写',  blank=True)
    experience = models.CharField(max_length=150, default='未填写',  blank=True)
    selfintroduction = models.CharField(max_length=150, default='未填写',  blank=True)
    jobchosen = models.CharField(max_length=150, default='尚未确定', blank=True)
    expert = models.CharField(max_length=128, default='未分配', blank=True)

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
    hobbies = (
        ('常规型', '常规型'),
        ('艺术型', '艺术型'),
        ('企业型', '企业型'),
        ('社会型', '社会型'),
        ('研究型', '研究型'),
        ('现实型', '现实型'),
    )
    personalities = (
        ('ISTJ稽查员', 'ISTJ稽查员'),
        ('ISFJ保护者', 'ISFJ保护者'),
        ('ISTP操作者/演奏者', 'ISTP操作者/演奏者'),
        ('ISFP作曲家/艺术家', 'ISFP作曲家/艺术家'),
        ('INFJ咨询师', 'INFJ咨询师'),
        ('INFP治疗师/导师', 'INFP治疗师/导师'),
        ('INTJ智多星/科学家', 'INTJ智多星/科学家'),
        ('INTP建筑师/设计师', 'INTP建筑师/设计师'),
        ('ESTJ督导', 'ESTJ督导'),
        ('ESFJ供给者/销售员', 'ESFJ供给者/销售员'),
        ('ESTP发起者/创设者', 'ESTP发起者/创设者'),
        ('ESFP表演者/示范者', 'ESFP表演者/示范者'),
        ('ENFJ教师', 'ENFJ教师'),
        ('ENFP倡导者/激发者', 'ENFP倡导者/激发者'),
        ('ENTJ统帅/调度', 'ENTJ统帅/调度'),
        ('ENTP发明家', 'ENTP发明家'),
    )
    educations = (
        ('中专及以下', '中专及以下'),
        ('大专', '大专'),
        ('本科', '本科'),
        ('硕士', '硕士'),
        ('博士及以上', '博士及以上'),
    )
    job_name = models.CharField(max_length=100, default=0, unique=True, blank=True)
    description = models.CharField(max_length=512, default=0, blank=True)
    requirement = models.CharField(max_length=512, default=0, blank=True)
    salary = models.CharField(max_length=32, choices=job_salary, default='3000以下', blank=True)
    skill = models.CharField(max_length=256, default='无要求', blank=True) #新增
    experience = models.CharField(max_length=1024, default='无要求', blank=True) #新增
    degree = models.CharField(max_length=32, choices=educations, default='中专及以下', blank=True) #新增
    major1 = models.CharField(max_length=128, default='无限制', blank=True) #新增
    major2 = models.CharField(max_length=128, default='无限制', blank=True) #新增
    major3 = models.CharField(max_length=128, default='无限制', blank=True)
    hobby1 = models.CharField(max_length=32, choices=hobbies, default='常规型', blank=True)
    hobby2 = models.CharField(max_length=32, choices=hobbies, default='常规型', blank=True)
    hobby3 = models.CharField(max_length=32, choices=hobbies, default='常规型', blank=True)
    personality1 = models.CharField(max_length=128, choices=personalities, default='ISTJ稽查员', blank=True)
    personality2 = models.CharField(max_length=128, choices=personalities, default='ISTJ稽查员', blank=True)
    personality3 = models.CharField(max_length=128, choices=personalities, default='ISTJ稽查员', blank=True)
    job_score = models.SmallIntegerField(default=0, blank=True)

    def __str__(self):
        return self.job_name


class Plan(models.Model):
    name = models.CharField(max_length=50,default=0, unique=True, blank=True)
    plan1 = models.CharField(max_length=256, default='专家尚未制定，请耐心等待', blank=True)
    plan2 = models.CharField(max_length=256, default='专家尚未制定，请耐心等待', blank=True)
    plan3 = models.CharField(max_length=256, default='专家尚未制定，请耐心等待', blank=True)
    expert = models.CharField(max_length=128, default='未分配', blank=True)

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
    expert = models.CharField(max_length=128, default='未分配', blank=True)

    def __str__(self):
        return self.name