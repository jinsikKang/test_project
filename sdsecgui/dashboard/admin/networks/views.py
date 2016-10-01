#_*_coding:utf-8_*_

from django.shortcuts import render
from django.http import JsonResponse

from sdsec.log_handler import setLogDir, getLogger
from sdsecgui.tools.command import getNetworkList
from sdsecgui.cmodels.network import Network, Subnet, DHCPagent

# setLogDir()
# logger = getLogger()


def retrieveNetworkList(request):
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
    network = Network()
    network.setById(network_id)
    return render(request, 'admin/networks/info.html', { 'network' : network })

def retrieveSubnetById(request, subnet_id):
    if not request.POST.get("id"):
        return render(request, 'admin/networks/subnets/info.html', { 'subnet_id' : subnet_id })
    else:
        subnet = Subnet()
        subnet.setById(subnet_id)
        print "id", request.POST["id"], "subnet : ", subnet
        return JsonResponse({ 'subnet' : subnet })