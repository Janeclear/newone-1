#！/usr/bin/env python
# -*-coding:utf-8 -*-
# Author:Jane time:2020-02-21
from django import forms


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128)
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput)
