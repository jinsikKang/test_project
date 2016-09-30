#_*_coding:utf-8_*_
from django.conf.urls import url, include

from sdsecgui.dashboard.admin.volumes import views

urlpatterns = [
    # 볼륨 주소
    url(r'$', views.retrieveVolumeList, name='volumeList'),
    url(r'(?P<volume_id>[\w\-]+)/$', views.retrieveVolumeById, name='volume'),
]