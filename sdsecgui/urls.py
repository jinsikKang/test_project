#_*_coding:utf-8_*_
from django.conf.urls import url, include

from sdsecgui.dashboard.provisioning import urls as provisioning_urls
from sdsecgui.dashboard.admin.instances import urls as instances_urls
from sdsecgui.dashboard.admin.volumes import urls as volumes_urls
from sdsecgui.dashboard.admin.flavors import urls as flavors_urls
from sdsecgui.dashboard.admin.images import urls as images_urls
from sdsecgui.dashboard.admin.networks import urls as networks_urls
from sdsecgui.dashboard.admin.routers import urls as routers_urls
from views import postlist, test, d3test

urlpatterns = [
    url(r'^$', postlist.post_list, name='post_list'),
    url(r'^add_post/$', postlist.write_post, name='write_post'),
    url(r'^new_page/$', test.new_page, name='new_page'),
    url(r'^d3test/(?P<page_name>\w+)/$', d3test.page, name='page'),

    url(r'^dashboard/provisioning/', include(provisioning_urls, namespace='provisioning')),

    url(r'^dashboard/admin/instances/', include(instances_urls, namespace='instances')),
    url(r'^dashboard/admin/volumes/', include(volumes_urls, namespace='volumes')),
    url(r'^dashboard/admin/flavors/', include(flavors_urls, namespace='flavors')),
    url(r'^dashboard/admin/images/', include(images_urls, namespace='images')),
    url(r'^dashboard/admin/networks/', include(networks_urls, namespace='networks')),
    url(r'^dashboard/admin/routers/', include(routers_urls, namespace='routers')),
]