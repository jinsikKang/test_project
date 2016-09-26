#_*_coding:utf-8_*_

import os

from django.shortcuts import render

from sdsec.log_handler import setLogDir, getLogger
from sdsecgui.tools.command import login

setLogDir()
logger = getLogger()


def new_page(request):
    logger.info("test")
    return render(request, 'test/main.html', {})

def retrieveUsage(request):

    start = request.start
    end = request.end
    login("admin", "chiron", "admin", "192.168.10.6")
    f = os.popen("openstack useage list --start " + start + " --end " + end)
    str =  f.read()