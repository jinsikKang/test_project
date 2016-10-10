#_*_coding:utf-8_*_

from django.shortcuts import render
from django.http import JsonResponse
import json

from sdsecgui.tools.command import getServiceList, getAgentList
# from sdsecgui.cmodels.network import 

# setLogDir()
# logger = getLogger()


def retrieveServiceList(request):
    # logger.info("retrieveServiceList")
    if request.is_ajax() and request.method == 'POST':
        serviceList = getServiceList()
        return JsonResponse({ 'serviceList' : serviceList })
        pass
    else:
        return render(request, 'admin/info/index.html', {})

def retrieveServiceById(request, service_id):
    # logger.info("retrieveServiceById")
    if request.is_ajax() and request.method == 'POST':
        # service = Service()
        # service.setById(service_id)
        # service.setPortList()
        # return JsonResponse({ 'data' : service.toJSON() })
        pass
    else:
        return render(request, 'admin/info/info.html', { 'service_id' : service_id })

def retrieveAgentList(request):

    if request.is_ajax() and request.method == 'POST':
        agentList = getAgentList()
        return JsonResponse({ 'agentList' : agentList })