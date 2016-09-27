#_*_coding:utf-8_*_
from django.conf.urls import url

from views import postlist, test, d3test, instances, images, flavors, base

urlpatterns = [
    url(r'^$', postlist.post_list, name='post_list'),
    url(r'^add_post/$', postlist.write_post, name='write_post'),
    url(r'^new_page/$', test.new_page, name='new_page'),
    url(r'^d3test/(?P<page_name>\w+)/$', d3test.page, name='page'),
    url(r'^dashboard/admin/instances/$', instances.retrieveInstanceList, name='instanceList'),
    url(r'^dashboard/admin/instances/(?P<instance_id>[\w\-]+)/$', instances.retrieveInstanceById, name='instance'),
    url(r'^dashboard/admin/images/$', images.retrieveImageList, name='imageList'),
    url(r'^dashboard/admin/images/(?P<image_id>[\w\-]+)/$', images.retrieveImageById, name='image'),
    url(r'^dashboard/admin/flavors/$', flavors.retrieveFlavorList, name='flavorList'),
    url(r'^dashboard/$', base.base, name='base'),
]