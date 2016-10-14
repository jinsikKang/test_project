#_*_coding:utf-8_*_

from django.shortcuts import render
from django.http import JsonResponse
import json

from sdsec.log_handler import setLogDir, getLogger
from sdsecgui.tools.command import getNetworkList, login, networkCmd
from sdsecgui.cmodels.network import Network, Subnet, DHCPagent, Port

# setLogDir()
# logger = getLogger()


def retrieveNetworkList(request):
    sess = login("admin", "chiron", "admin", "19.168.10.6", ":35357/v3")
    networkCmd("", sess)
    # logger.info("retrieveNetworkList")
    networkList = getNetworkList()
    tempList = []
    for network in networkList:
        network_id = network["id"]
        network = Network()
        network.setById(network_id)
        tempList.append(network)
    networkList = tempList
    return render(request, 'admin/networks/index.html', { 'networkList' : networkList })

def retrieveNetworkById(request, network_id):
    # logger.info("retrieveNetworkById")
    if request.is_ajax() and request.method == 'POST':
        network = Network()
        network.setById(network_id)
        network.setPortList()
        return JsonResponse({ 'data' : network.toJSON() })
    else:
        return render(request, 'admin/networks/info.html', { 'network_id' : network_id })

def retrieveSubnetById(request, subnet_id):
    if request.is_ajax() and request.method == 'POST':
        # print "ajax, POST", request.is_ajax(), request.method
        subnet = Subnet()
        subnet.setById(subnet_id)
        return JsonResponse({ 'subnet' : subnet.toJSON() })
    else:
        # print "is ajax : ", request.is_ajax(), " method:", request.method
        return render(request, 'admin/networks/subnets/info.html', {'subnet_id': subnet_id})
    # else:
    #     print "뭐지대체?", request.is_ajax(), request.method

def retrievePortById(request, port_id):
    if request.is_ajax() and request.method == 'POST':
        port = Port()
        port.setById(port_id)
        return JsonResponse({ 'port' : port.portDic })
    else:
        return render(request, 'admin/networks/ports/info.html', {'port_id': port_id})