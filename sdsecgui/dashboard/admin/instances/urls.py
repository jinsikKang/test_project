#_*_coding:utf-8_*_
from django.conf.urls import url, include

from sdsecgui.dashboard.admin.flavors import views
from sdsecgui.dashboard.admin.images import views
from sdsecgui.dashboard.admin.instances import views
from sdsecgui.dashboard.admin.networks import views
from sdsecgui.dashboard.admin.volumes import views
from sdsecgui.dashboard.provisioning import views

urlpatterns = [
    # url(r'^$', postlist.post_list, name='post_list'),
    # url(r'^add_post/$', postlist.write_post, name='write_post'),
    # url(r'^new_page/$', test.new_page, name='new_page'),
    # url(r'^d3test/(?P<page_name>\w+)/$', d3test.page, name='page'),
    # include(r'', include('sdsecgui.urls')),
    # # 인스턴스 주소
    # url(r'^dashboard/admin/instances/$', views.retrieveInstanceList, name='instanceList'),
    # url(r'^dashboard/admin/instances/(?P<instance_id>[\w\-]+)/$', views.retrieveInstanceById, name='instance'),
    # # 볼륨 주소
    # url(r'^dashboard/admin/volumes/$', views.retrieveVolumeList, name='volumeList'),
    # url(r'^dashboard/admin/volumes/(?P<volume_id>[\w\-]+)/$', views.retrieveVolumeById, name='volume'),
    # # flavor 주소
    # url(r'^dashboard/admin/flavors/$', views.retrieveFlavorList, name='flavorList'),
    # # 이미지 주소
    # url(r'^dashboard/admin/images/$', views.retrieveImageList, name='imageList'),
    # url(r'^dashboard/admin/images/(?P<image_id>[\w\-]+)/$', views.retrieveImageById, name='image'),
    #
    # url(r'^dashboard/admin/networks/$', views.retrieveNetworkList, name='networkList'),
    # url(r'^dashboard/admin/networks/(?P<network_id>[\w\-]+)/$', views.retrieveNetworkById, name='network'),
    #
    # url(r'^dashboard/$', views.provisioning, name='provisioning'),
]