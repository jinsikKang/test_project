#_*_coding:utf-8_*_
from django.conf.urls import url

from sdsecgui.dashboard.admin.flavors import views

urlpatterns = [
    # flavor 주소
    url(r'^$', views.retrieveFlavorList, name='flavorList'),
]