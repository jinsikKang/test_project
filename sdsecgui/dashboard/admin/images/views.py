#_*_coding:utf-8_*_

from django.shortcuts import render

from sdsec.log_handler import setLogDir, getLogger
from sdsecgui.tools.command import getImageList
from sdsecgui.cmodels.image import Image

setLogDir()
logger = getLogger()


def retrieveImageList(request):
    logger.info("retrieveInstanceList")
    imageList = getImageList()
    tempList = []
    for image in imageList:
        image_id = image["id"]
        image = Image()
        image.setById(image_id)
        tempList.append(image)
    imageList = tempList

    return render(request, 'templates/index.html', { 'imageList' : imageList })

def retrieveImageById(request, image_id):
    logger.info("retrieveInstanceById")
    image = Image()
    image.setById(image_id)
    return render(request, 'templates/info.html', { 'image' : image })