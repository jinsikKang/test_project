#_*_coding:utf-8_*_
from django.conf.urls import url, include

from sdsecgui.dashboard.admin.networks import views

urlpatterns = [
    url(r'$', views.retrieveNetworkList, name='networkList'),
    url(r'(?P<network_id>[\w\-]+)/$', views.retrieveNetworkById, name='network'),
]