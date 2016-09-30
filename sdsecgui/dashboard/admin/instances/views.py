#_*_coding:utf-8_*_

from django.shortcuts import render

from sdsec.log_handler import setLogDir, getLogger
from sdsecgui.tools.command import getInstanceList, login
from sdsecgui.cmodels.instance import Instance

setLogDir()
logger = getLogger()


def retrieveInstanceList(request):
    logger.info("retrieveInstanceList")
    login("admin", "chiron", "admin", "192.168.10.6", ":35357/v2.0")
    instanceList = getInstanceList()
    return render(request, 'dashboard/admin/instances/index.html', { 'instanceList' : instanceList })

def retrieveInstanceById(request, instance_id):
    logger.info("retrieveInstanceById")
    instance = Instance()
    instance.setById(instance_id)
    return render(request, 'admin/instances/info.html', { 'instance' : instance })