#_*_coding:utf-8_*_
from django.conf.urls import url

from sdsecgui.dashboard.admin.routers import views

urlpatterns = [
    url(r'^$', views.retrieveRouterList, name='routerList'),
    url(r'interface/$', views.retrieveInterfaceListInRouter, name='interface'),
    url(r'^(?P<router_id>[\w\-]+)/$', views.retrieveRouterById, name='router'),
]