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
