# _*_coding:utf-8_*_
import json

from sdsec.log_handler import setLogDir, getLogger
from ..tools.command import excuteCmd, login

setLogDir()
logger = getLogger()

class Network:
    def outputToInfo(self, outputList):
        infoDic = {}
        for row in outputList[3:-1]:
            cols = row[1:-1].split("|")
            key = cols[0].strip().replace(" ", "_")
            value = cols[1].strip()
            infoDic[key] = value
        return infoDic

    def showInfoJsonById(self, id):
        # id로 네트워크를 찾는다.
        logger.debug("showNetworkById")
        output = json.loads(excuteCmd("neutron net-show " + id + " -f json"))

        if output:
            return output
        else:
            logger.debug(str("'" + unicode(id).encode("utf-8") + "' 에 해당하는 인스턴스가 없습니다."))
            return None

    def __init__(self):
        self.provider = {}
        self.router = {}
        self.ipv6_address_scope = ""
        self.revision_number = ""
        self.port_security_enabled = ""
        self.id = ""
        self.availability_zone_hints = ""
        self.availability_zones = ""
        self.ipv4_address_scope = ""
        self.shared = ""
        self.project_id = ""
        self.status = ""
        self.subnets = ""
        self.description = ""
        self.tags = ""
        self.updated_at = ""
        self.name = ""
        self.admin_state_up = ""
        self.tenant_id = ""
        self.created_at = ""
        self.mtu = ""
        pass

    def setById(self, id):
        networkDic = self.showInfoJsonById(id)
        if networkDic == None:
            raise Exception, unicode(id).encode("utf-8") + "의 세부 정보를 찾지 못했습니다."
        self.provider["physical_network"] = networkDic["provider:physical_network"]
        self.provider["network_type"] = networkDic["provider:network_type"]
        self.provider["segmentation_id"] = networkDic["provider:segmentation_id"]
        self.router["external"] = networkDic["router:external"]
        self.ipv6_address_scope = networkDic["ipv6_address_scope"]
        self.revision_number = networkDic["revision_number"]
        self.port_security_enabled = networkDic["port_security_enabled"]
        self.id = networkDic["id"]
        self.availability_zone_hints = networkDic["availability_zone_hints"]
        self.availability_zones = networkDic["availability_zones"]
        self.ipv4_address_scope = networkDic["ipv4_address_scope"]
        self.shared = networkDic["shared"]
        self.project_id = networkDic["project_id"]
        self.status = networkDic["status"]
        self.subnets = networkDic["subnets"]
        self.description = networkDic["description"]
        self.tags = networkDic["tags"]
        self.updated_at = networkDic["updated_at"]
        self.name = networkDic["name"]
        self.admin_state_up = networkDic["admin_state_up"]
        self.tenant_id = networkDic["tenant_id"]
        self.created_at = networkDic["created_at"]
        self.mtu = networkDic["mtu"]

class subnet:
