#_*_coding:utf-8_*_

from django.shortcuts import render

from skeletonLib import ControllerEngine

def provisioning(request):
    controll = ControllerEngine()
    # controll.createMap()
    return render(request, 'provisioning/index.html', {})