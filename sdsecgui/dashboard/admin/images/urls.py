#_*_coding:utf-8_*_
from django.conf.urls import url

from sdsecgui.dashboard.admin.images import views

urlpatterns = [
    # 이미지 주소
    url(r'^$', views.retrieveImageList, name='imageList'),
    url(r'^(?P<image_id>[\w\-]+)/$', views.retrieveImageById, name='image'),
]