#_*_coding:utf-8_*_
import pprint

from django.shortcuts import render
from django.http import JsonResponse
import json

from sdsecgui.tools.command import getRouterList
from sdsecgui.tools.converter import dictionaryEncodeConvert
from sdsecgui.cmodels.router import Router


def retrieveRouterList(request):
    # logger.info("retrieveRouterList")
    if request.is_ajax() and request.method == 'POST':
        tempList = []
        # POST.body의 데이터(QueryDic)를 dictionary 형태로 바꾸어 얻음
        data = json.loads(request.POST.dict()["routerList"])
        for router in data:
            router_id = router["id"]
            router = Router()
            router.setById(router_id)
            tempList.append(router.showInfoJsonById(router_id))
        routerList = tempList
        return JsonResponse({'data': routerList})
    else:
        # json.stringify 형태로 넘겨줌("str")
        routerList = getRouterList("str")
        return render(request, 'admin/routers/index.html', { 'routerList' : routerList })

def retrieveRouterById(request, router_id):
    if request.is_ajax() and request.method == 'POST':
        router = Router()
        router.setById(router_id)
        return JsonResponse({ 'router' : router.routerDic })
    else:
        return render(request, 'admin/routers/routers/info.html', {'router_id': router_id})