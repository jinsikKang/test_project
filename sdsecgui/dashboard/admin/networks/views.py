#_*_coding:utf-8_*_

from django.shortcuts import render

from sdsec.log_handler import setLogDir, getLogger
from sdsecgui.tools.command import getNetworkList
from sdsecgui.cmodels.network import Network

setLogDir()
logger = getLogger()


def retrieveNetworkList(request):
    logger.info("retrieveNetworkList")
    networkList = getNetworkList()
    tempList = []
    for network in networkList:
        network_id = network["id"]
        network = Network()
        network.setById(network_id)
        tempList.append(network)
    networkList = tempList
    return render(request, 'templates/index.html', { 'networkList' : networkList })

def retrieveNetworkById(request, network_id):
    logger.info("retrieveNetworkById")
    network = Network()
    network.setById(network_id)
    return render(request, 'templates/info.html', { 'network' : network })