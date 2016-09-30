#_*_coding:utf-8_*_

from django.shortcuts import render

from sdsec.log_handler import setLogDir, getLogger
from sdsecgui.tools.command import getVolumeList
from sdsecgui.cmodels.volume import Volume

setLogDir()
logger = getLogger()


def retrieveVolumeList(request):
    logger.info("retrieveVolumeList")
    volumeList = getVolumeList()
    tempList = []
    for volume in volumeList:
        volume_id = volume["id"]
        volume = Volume()
        volume.setById(volume_id)
        tempList.append(volume)
    volumeList = tempList
    return render(request, 'templates/index.html', { 'volumeList' : volumeList })

def retrieveVolumeById(request, volume_id):
    logger.info("retrieveVolumeById")
    volume = Volume()
    volume.setById(volume_id)
    return render(request, 'templates/info.html', { 'volume' : volume })