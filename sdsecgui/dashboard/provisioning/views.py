#_*_coding:utf-8_*_

from django.shortcuts import render
from django.http import JsonResponse

from skeletonLib import ControllerEngine

def provisioning(request):
    if request.is_ajax() and request.method == 'POST':
        controll = ControllerEngine()
        token = controll.getToken("admin", "http://192.168.10.6:35357/v2.0", "admin", "chiron")
        service_detail = controll.showService(token, "admin", "admin", "firstService")
        return JsonResponse({ 'node_list' : service_detail })
    else:
        return render(request, 'provisioning/index.html', {})