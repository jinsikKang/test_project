#_*_coding:utf-8_*_
from django.conf.urls import url

from sdsecgui.dashboard.admin.info import views

urlpatterns = [
    url(r'^$', views.retrieveServiceList, name='serviceList'),
    url(r'^agent$', views.retrieveAgentList, name='agentList'),
    url(r'^nova_service$', views.retrieveNovaServiceList, name='agentList'),
]