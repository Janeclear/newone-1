"""newone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import *
from django.contrib import admin

from app1.views import index, login, plan_done, jobinfo, jobnews, jobdetail, jobnews_show, jobnewsdetail, alogout, \
    add_expert, eselfinfo, auserinfo, login_base, jobelook, e_newscheck
from app1.views import plan,alogin,admin_eu,userinfo_test
from app1.views import register01, selfinfo, logout, careerhelper
from app1.views import base, Introduction, selfinfo_done, career
from app1.views import elogin, ad_userinfo, planmaking, elogout, job,deletejob
from app1.views import login02,login_a
from . import testdb

from . import *
from app1 import views

urlpatterns = (
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login),
    url(r'^index/', index),
    url(r'^login02/', login02),
    url(r'^login_a', login_a),
    url(r'^logout', logout),
    url(r'^elogout', elogout),
    url(r'alogout', alogout),
    url(r'^register01/', register01),
    url(r'^base/', base),
    url(r'^testdb$', testdb.testdb),
    url(r'^selfinfo/', selfinfo),
    url(r'^selfinfo_done/', selfinfo_done),
    url(r'^careerhelper/', careerhelper),
    url(r'^Introduction/', Introduction),
    url(r'^plan/', plan),
    url(r'^plan_done', plan_done),
    url(r'^career/', career),
    url(r'^elogin/', elogin),
    url(r'^ad_userinfo/', ad_userinfo),
    url(r'^planmaking/', planmaking),
    url(r'^job/', job),
    url(r'^jobinfo/', jobinfo),
    url(r'^jobnews/', jobnews),
    url(r'^jobdetail/(?P<nid>\d+)$', jobdetail, name='jobdetail'),
    url(r'^deletejob/(?P<nid>\d+)$', deletejob, name='deletejob'),
    #url(r'^detail-(?P<nid>\d+)-(?P<uid>\d+).html', views.detail),
    url(r'^jobnews_show/', jobnews_show),
    url(r'^jobnewsdetail/(?P<nid>\d+)$', jobnewsdetail,name='jobnewsdetail'),
    url(r'^alogin/', alogin),
    url(r'^admin_eu/', admin_eu),
    url(r'^add_expert/', add_expert),
    url(r'^eselfinfo', eselfinfo),
    url(r'^userinfo_test', userinfo_test),
    url(r'^auserinfo', auserinfo),
    url(r'^login_base', login_base),
    url(r'^jobelook', jobelook),#专家-职业信息查看
    url(r'^e_newscheck', e_newscheck),#专家-咨询查看
    #url(r'^remove_userinfo(?P<nid>\d+)/',views.removeuserinfo,name='reinfo'),
    # index
    # logout
    #url(r'^register/', register),
    # url(r'^hello$', view.hello),
)
