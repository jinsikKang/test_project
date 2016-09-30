#_*_coding:utf-8_*_

from django.shortcuts import render

from sdsec.log_handler import setLogDir, getLogger

setLogDir()
logger = getLogger()


def provisioning(request):
    return render(request, 'provisioning/index.html', {})