#_*_coding:utf-8_*_

from django.shortcuts import render
from django.http import JsonResponse
import json

from sdsecgui.tools.command import getServiceList, getNovaServiceList, getBlockStorageServiceList, getAgentList
# from sdsecgui.cmodels.network import 

# setLogDir()
# logger = getLogger()


def retrieveServiceList(request):
    # logger.info("retrieveServiceList")
    if request.is_ajax() and request.method == 'POST':
        serviceList = getServiceList()
        return JsonResponse({ 'serviceList' : serviceList })
    else:
        return render(request, 'admin/info/index.html', {})


def retrieveNovaServiceList(request):
    if request.is_ajax() and request.method == 'POST':
        novaServiceList = getNovaServiceList()
        return JsonResponse({ 'novaServiceList' : novaServiceList })

def retrieveBlockStorageServiceList(request):
    if request.is_ajax() and request.method == 'POST':
        blockStorageServiceList = getBlockStorageServiceList()
        return JsonResponse({ 'blockStorageServiceList' : blockStorageServiceList })

def retrieveAgentList(request):
    if request.is_ajax() and request.method == 'POST':
        agentList = getAgentList()
        return JsonResponse({ 'agentList' : agentList })