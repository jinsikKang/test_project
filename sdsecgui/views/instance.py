#_*_coding:utf-8_*_

from django.shortcuts import render

from sdsec import log_handler
from sdsec.log_handler import setLogDir, getLogger
from sdsecgui.tools.command import getInstanceList
from sdsecgui.cmodels.instance import Instance

#로그불러왓!
setLogDir()
logger = getLogger()


def retrieveInstanceList(request):
    logger.info("retrieveInstanceList")
    instanceList = getInstanceList()
    return render(request, 'instance/index.html', { 'instanceList' : instanceList })

def retrieveInstanceById(request, instance_id):
    logger.info("retrieveInstanceById")
    instance = Instance()
    instance.setById(instance_id)
    return render(request, 'instance/info.html', { 'instance' : instance })