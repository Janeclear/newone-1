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

from app1.views import login, selfinfo, logout, careerhelper, Introduction, selfinfo_done
from app1.views import login02, plan
from app1.views import register01
from app1.views import base
from app1.views import index
from app1.views import login_a
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

    url(r'^register01/', register01),
    url(r'^base/', base),

    url(r'^testdb$', testdb.testdb),
    url(r'^selfinfo/', selfinfo),
    url(r'^selfinfo_done/', selfinfo_done),
    url(r'^careerhelper/', careerhelper),
    url(r'^Introduction/', Introduction),
    url(r'^plan/', plan),
    # index
    # logout
    #url(r'^register/', register),
    # url(r'^hello$', view.hello),

)
