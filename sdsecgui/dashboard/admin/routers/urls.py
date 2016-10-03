#_*_coding:utf-8_*_
from django.conf.urls import url

from sdsecgui.dashboard.admin.routers import views

urlpatterns = [
    # 볼륨 주소
    url(r'^$', views.retrieveRouterList, name='routerList'),
    url(r'(?P<router_id>[\w\-]+)/$', views.retrieveRouterById, name='router'),
]