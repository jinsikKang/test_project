#_*_coding:utf-8_*_

from django.shortcuts import render

from sdsec.log_handler import setLogDir, getLogger
from sdsecgui.tools.command import getFlavorList

setLogDir()
logger = getLogger()


def retrieveFlavorList(request):
    logger.info("retrieveInstanceList")
    flavorList = getFlavorList()

    return render(request, 'index.html', { 'flavorList' : flavorList })