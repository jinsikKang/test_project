#_*_coding:utf-8_*_

from django.shortcuts import render
from django.http import JsonResponse
import json

from sdsec.log_handler import setLogDir, getLogger
from sdsecgui.tools.command import login, networkIndexCmd, networkInfoCmd, subnetInfoCmd, portInfoCmd
from sdsecgui.cmodels.network import Port

# setLogDir()
# logger = getLogger()


def retrieveNetworkList(request):
    if request.is_ajax() and request.method == 'POST':
        sess = login("admin", "chiron", "admin", "http://192.168.10.6/identity/v3")
        networks = networkIndexCmd("", sess)
        return JsonResponse({ 'networkList' : networks })
    else:
        return render(request, 'admin/networks/index.html', {})

def retrieveNetworkById(request, network_id):
    # logger.info("retrieveNetworkById")
    if request.is_ajax() and request.method == 'POST':
        sess = login("admin", "chiron", "admin", "http://192.168.10.6/identity/v3")
        network = networkInfoCmd(sess, network_id)
        return JsonResponse({ 'data' : network })
    else:
        return render(request, 'admin/networks/info.html', { 'network_id' : network_id })

def retrieveSubnetById(request, subnet_id):
    if request.is_ajax() and request.method == 'POST':
        sess = login("admin", "chiron", "admin", "http://192.168.10.6/identity/v3")
        subnet = subnetInfoCmd(sess, subnet_id)
        return JsonResponse({ 'subnet' : subnet })
    else:
        # print "is ajax : ", request.is_ajax(), " method:", request.method
        return render(request, 'admin/networks/subnets/info.html', {'subnet_id': subnet_id})
    # else:
    #     print "뭐지대체?", request.is_ajax(), request.method

def retrievePortById(request, port_id):
    if request.is_ajax() and request.method == 'POST':
        sess = login("admin", "chiron", "admin", "http://192.168.10.6/identity/v3")
        port = portInfoCmd(sess, port_id)
        return JsonResponse({ 'port' : port })
    else:
        return render(request, 'admin/networks/ports/info.html', {'port_id': port_id})