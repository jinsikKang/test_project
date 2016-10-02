# _*_coding:utf-8_*_
import json
import re

from sdsec.log_handler import setLogDir, getLogger
from ..tools.command import excuteCmd, login
from base import Base

# setLogDir()
# logger = getLogger()

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
        # logger.debug("showNetworkById")
        output = json.loads(excuteCmd("neutron net-show " + id + " -f json"))

        if output:
            return output
        else:
            return None

    def toJSON(self):
        # return json._default_encoder.encode(self.__dict__)
        return json.loads(json.dumps(self, default=lambda o:o.__dict__, sort_keys=True, indent=4))

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

        self.subnet_id_list = networkDic["subnets"].split("\n")
        self.subnets = self.getSubnetList()
        self.ports = self.getPortList()
        self.dhcpAgents = self.getDHCPagentList()

        self.description = networkDic["description"]
        self.tags = networkDic["tags"]
        self.updated_at = networkDic["updated_at"]
        self.name = networkDic["name"]
        self.admin_state_up = networkDic["admin_state_up"]
        self.tenant_id = networkDic["tenant_id"]
        self.created_at = networkDic["created_at"]
        self.mtu = networkDic["mtu"]

    def getSubnetList(self):
        subnets = []
        for subnet_id in self.subnet_id_list:
            subnet = Subnet()
            subnet.setById(subnet_id)
            subnets.append(subnet)
        return subnets

    def getPortList(self):
        ports = []
        tempPortList = json.loads(excuteCmd("neutron port-list -f json"))
        for tempPort in tempPortList:
            ports.append(json.loads(excuteCmd("neutron port-show " + tempPort["id"] + " -f json")))
        return ports

    def getDHCPagentList(self):
        output = json.loads(excuteCmd("neutron dhcp-agent-list-hosting-net " + self.id + " -f json"))
        return output
        

class Subnet(Base):
    def __init__(self):
        self.service_types = ""
        self.description = ""
        self.enable_dhcp = ""
        self.network_id = ""
        self.tenant_id = ""
        self.created_at = ""
        self.dns_nameservers = ""
        self.updated_at = ""
        self.ipv6_ra_mode = ""
        self.allocation_pools = ""
        self.gateway_ip = ""
        self.revision_number = ""
        self.ipv6_address_mode = ""
        self.ip_version = ""
        self.host_routes = ""
        self.cidr = ""
        self.project_id = ""
        self.id = ""
        self.subnetpool_id = ""
        self.name = ""
        pass

    def showInfoJsonById(cls, id):
        output = json.loads(excuteCmd("neutron subnet-show " + id + " -f json"))

        if output:
            return output
        else:
            return None

    def setById(cls, id):
        cls.subnetDic = cls.showInfoJsonById(id)
        if cls.subnetDic == None:
            raise Exception, unicode(id).encode("utf-8") + "의 세부 정보를 찾지 못했습니다."
        cls.service_types = cls.subnetDic["service_types"]
        cls.description = cls.subnetDic["description"]
        cls.enable_dhcp = cls.subnetDic["enable_dhcp"]
        cls.network_id = cls.subnetDic["network_id"]
        cls.tenant_id = cls.subnetDic["tenant_id"]
        cls.created_at = cls.subnetDic["created_at"]
        cls.dns_nameservers = cls.subnetDic["dns_nameservers"]
        cls.updated_at = cls.subnetDic["updated_at"]
        cls.ipv6_ra_mode = cls.subnetDic["ipv6_ra_mode"]
        cls.allocation_pools = []
        for allocation_pool in cls.subnetDic["allocation_pools"].split("\n"):
            cls.allocation_pools.append(json.loads(allocation_pool))
        cls.gateway_ip = cls.subnetDic["gateway_ip"]
        cls.revision_number = cls.subnetDic["revision_number"]
        cls.ipv6_address_mode = cls.subnetDic["ipv6_address_mode"]
        cls.ip_version = cls.subnetDic["ip_version"]
        cls.host_routes = cls.subnetDic["host_routes"]
        cls.cidr = cls.subnetDic["cidr"]
        cls.project_id = cls.subnetDic["project_id"]
        cls.id = cls.subnetDic["id"]
        cls.subnetpool_id = cls.subnetDic["subnetpool_id"]
        cls.name = cls.subnetDic["name"]
        ipv4_pattern = re.compile("[\d]+\.[\d]+\.[\d]+\.([\d]+)")
        ipv6_pattern = re.compile("[\w]+:[\w]+:[\w]+:[\w]*:([\w:]+)")
        """
        ^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]).){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]).){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$
        """
        print cls.allocation_pools
        if cls.ip_version == "4":
            print ipv4_pattern.match(cls.allocation_pools["end"]).group(1)
            print ipv4_pattern.match(cls.allocation_pools["start"]).group(1)
        elif cls.ip_version == "6":
            # ipv6_pattern
            pass
        # cls.remain_ip = cls.allocation_pools["start"]

class Port(Base):
    def showInfoJsonById(cls, id):
        output = json.loads(excuteCmd("neutron port-show " + id + " -f json"))
        if output:
            return output
        else:
            return None
    def setById(cls, id):
        cls.portDic = cls


class DHCPagent(Base):
    def __init__(self):
        self.host = ""
        self.id = ""
        self.alive = ""
        self.admin_state_up = ""
    def showInfoJsonById(cls, id):
        output = json.loads(excuteCmd("neutron dhcp-agent-list-hosting-net " + id + " -f json"))
        if output:
            return output
        else:
            return None

    def setById(cls, id):
        dhcpAgentDic = cls.showInfoJsonById(id)
        cls.host = dhcpAgentDic["host"]
        cls.id = dhcpAgentDic["id"]
        cls.alive = dhcpAgentDic["alive"]
        cls.admin_state_up = dhcpAgentDic["admin_state_up"]