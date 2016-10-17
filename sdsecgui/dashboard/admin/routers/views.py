#_*_coding:utf-8_*_
import pprint

from django.shortcuts import render
from django.http import JsonResponse
import json

from keystoneauth1 import session

from sdsecgui.tools.command import getRouterList, getInterfaceListInRouter, login, routersIndexCmd
from sdsecgui.tools.converter import dictionaryEncodeConvert
from sdsecgui.cmodels.router import Router


def retrieveRouterList(request):
    # logger.info("retrieveRouterList")
    if request.is_ajax() and request.method == 'POST':
        sess = session.Session(request)
        # sess = login("admin", "chiron", "admin", "http://192.168.10.6/identity/v3")
        routers = routersIndexCmd(sess)
        return JsonResponse({'data': routers})
    else:
        return render(request, 'admin/routers/index.html', { })

def retrieveRouterById(request, router_id):
    if request.is_ajax() and request.method == 'POST':
        router = Router()
        router.setById(router_id)
        return JsonResponse({ 'router' : router.routerDic })
    else:
        return render(request, 'admin/routers/info.html', {'router_id': router_id})

def retrieveInterfaceListInRouter(request):
    if request.is_ajax() and request.method == 'POST':
        router_id = request.POST.dict()["id"]
        interfaceList = getInterfaceListInRouter(router_id)
        return JsonResponse({ 'interface' : interfaceList })