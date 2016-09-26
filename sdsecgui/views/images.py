#_*_coding:utf-8_*_

from django.shortcuts import render

from sdsec.log_handler import setLogDir, getLogger
from sdsecgui.tools.command import getImageList, login
from sdsecgui.cmodels.images import Image

setLogDir()
logger = getLogger()


def retrieveImageList(request):
    logger.info("retrieveInstanceList")
    imageList = getImageList()
    print imageList
    # for image in imageList:
    #     imageObj = Image()
    #     image.setById(image)

    return render(request, 'images/index.html', { 'imageList' : imageList })

def retrieveImageById(request, image_id):
    logger.info("retrieveInstanceById")
    image = Image()
    image.setById(image_id)
    return render(request, 'images/info.html', { 'image' : image })