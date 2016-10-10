#_*_coding:utf-8_*_

from django.shortcuts import render
from django.http import JsonResponse
import json

from sdsecgui.tools.command import retrieveServiceList
# from sdsecgui.cmodels.network import 

# setLogDir()
# logger = getLogger()


def retrieveServiceList(request):
    # logger.info("retrieveServiceList")
    if request.is_ajax() and request.method == 'POST':
        serviceList = retrieveServiceList()
        return JsonResponse({ 'data' : serviceList })
        pass
    else:
        return render(request, 'admin/services/index.html', {})

def retrieveServiceById(request, service_id):
    # logger.info("retrieveServiceById")
    if request.is_ajax() and request.method == 'POST':
        # service = Service()
        # service.setById(service_id)
        # service.setPortList()
        # return JsonResponse({ 'data' : service.toJSON() })
        pass
    else:
        return render(request, 'admin/services/info.html', { 'service_id' : service_id })