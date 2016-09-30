#_*_coding:utf-8_*_
from django.conf.urls import url, include

from sdsecgui.dashboard.admin.instances import views

urlpatterns = [
    # 인스턴스 주소
    url(r'$', views.retrieveInstanceList, name='instanceList'),
    url(r'(?P<instance_id>[\w\-]+)/$', views.retrieveInstanceById, name='instance'),
]