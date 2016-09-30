#_*_coding:utf-8_*_
from django.conf.urls import url
from sdsecgui.dashboard.provisioning import views

urlpatterns = [
    url(r'^$', views.provisioning, name='provisioning'),
]