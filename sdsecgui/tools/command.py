#_*_coding:utf-8_*_
import json
import os

from keystoneauth1.identity import v3
from keystoneauth1 import session
from novaclient import client

from sdsec import log_handler
# from sdsec.log_handler import setLogDir, getLogger
import logging

#로그불러왓!
# setLogDir()
# logger = getLogger()

def novaCmd(command, sess):
    nova = client.Client("2.1", session=sess)
    print nova.flavors.list()
    print nova.servers.list()
    print nova.keypairs.list()

def excuteCmd(command):
    # 명령 실행, 출력 반환
    # logger.debug("excuteCmd>> "+command)
    # print "excuteCmd>> " + command
    f = os.popen(command)
    result = f.read()
    # print result
    # logger.debug(result)
    return result


def parsingOutputToList(output):
    # 출력을 받아 parsing함
    rows = output.splitlines()
    if rows:
        # index 0 = 테두리
        # index 1 = 키(컬럼명)
        keyList = rows[1][1:-1].split("|")
        for idx, key in enumerate(keyList):
            # 양끝 공백을 없애고 사이공백은 밑줄로 전환
            keyList[idx] = key.lower().strip().replace(" ", "_")
        resultList = []
        for row in rows[3:-1]:
            # index 3 ~ = 목록
            # 한 줄당 하나의 인스턴스
            # 하나의 인스턴스를 Dictionary에 담는다
            resultDic = {}
            cols = row[1:-1].split("|")
            for idx, col in enumerate(cols):
                key = keyList[idx]
                value = col.strip()
                resultDic[key] = value
            # Dictionary를 List에 담아 반환한다.
            resultList.append(resultDic)
        return resultList
    else:
        # 인스턴스가 하나도 없을 때
        # logger.debug("List is empty")
        return None


def getInstanceList():
    # logger.debug("getInstanceList")

    output = excuteCmd("nova list --all-tenants")
    instanceList = parsingOutputToList(output)

    return instanceList

def getVolumeList():
    # logger.debug("getVolumeList")

    output = excuteCmd("openstack volume list --all-projects")
    volumeList = parsingOutputToList(output)

    return volumeList

def getImageList():
    # logger.debug("getImageList")

    output = excuteCmd("glance image-list")
    imageList = parsingOutputToList(output)

    return imageList

def getFlavorList():
    # logger.debug("getFlavorList")
    output = excuteCmd("nova flavor-list")
    flavorList = parsingOutputToList(output)
    return flavorList

def getNetworkList():
    # logger.debug("getNetworkList")

    networkList = json.loads(excuteCmd("neutron net-list -f json"))

    return networkList

def getRouterList(type="json"):
    if type == "json":
        routerList = json.loads(excuteCmd("neutron router-list -f json"))
    elif type == "str":
        routerList = excuteCmd("neutron router-list -f json")
    else:
        routerList = None
    return routerList

def getInterfaceListInRouter(router_id, type="json"):
    if type == "json":
        interfaceList = json.loads(excuteCmd("neutron router-port-list " + router_id + " -f json"))
    elif type == "str":
        interfaceList = excuteCmd("neutron router-port-list " + router_id + " -f json")
    else:
        interfaceList = None
    return interfaceList

def getServiceList():
    serviceList = json.loads(excuteCmd("openstack service list -f json"))
    return serviceList


def getNovaServiceList():
    output = excuteCmd("nova service-list")
    novaServiceList = parsingOutputToList(output)
    return novaServiceList

def getBlockStorageServiceList():
    output = excuteCmd("cinder service-list")
    blockStorageServiceList = parsingOutputToList(output)
    return blockStorageServiceList

def getAgentList(type="json"):
    if type == "json":
        agentList = json.loads(excuteCmd("neutron agent-list -f json"))
    elif type == "str":
        agentList = excuteCmd("neutron agent-list -f json")
    else:
        agentList = None
    return agentList

def login(username, password, tenant_name, controller, auth_url):
    # logger.debug("login")
    os.environ["OS_USERNAME"] = username
    os.environ["OS_PASSWORD"] = password
    os.environ["OS_TENANT_NAME"] = tenant_name
    os.environ["OS_AUTH_URL"] = "http://" + controller + auth_url
    aa = "http://" + controller + auth_url
    auth = v3.Password(auth_url=aa, username=username, password=password, project_name=tenant_name, user_domain_id='default', project_domain_id='default')
    # print auth
    sess = session.Session(auth=auth)
    novaCmd("",sess)
    return sess
