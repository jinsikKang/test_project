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
        # id로 볼륨을 찾는다.
        logger.debug("showNetworkById")
        output = json.loads(excuteCmd("neutron net-show " + id + " -f json"))

        if output:
            print output
        else:
            logger.debug(str("'" + unicode(id).encode("utf-8") + "' 에 해당하는 인스턴스가 없습니다."))
            return None

    def __init__(self):
        pass
    def setById(self, id):
        networkDic = self.showInfoById(id)
        if networkDic == None:
            raise Exception, unicode(id).encode("utf-8") + "에 해당하는 인스턴스가 없습니다."
        self.attachments = networkDic["attachments"]
        self.availability_zone = networkDic["availability_zone"]
        self.bootable = networkDic["bootable"]
        self.consistencygroup_id = networkDic["consistencygroup_id"]
        self.created_at = networkDic["created_at"]
        self.description = networkDic["description"]
        self.encrypted = networkDic["encrypted"]
        self.id = networkDic["id"]
        self.migration_status = networkDic["migration_status"]
        self.multiattach = networkDic["multiattach"]
        self.name = networkDic["name"] if networkDic["name"] else networkDic["id"]
        self.os_vol_host_attr["host"] = networkDic["os-vol-host-attr:host"]
        self.os_vol_mig_status_attr["migstat"] = networkDic["os-vol-mig-status-attr:migstat"]
        self.os_vol_mig_status_attr["name_id"] = networkDic["os-vol-mig-status-attr:name_id"]
        self.os_vol_tenant_attr["tenant_id"] = networkDic["os-vol-tenant-attr:tenant_id"]
        self.properties = networkDic["properties"]
        self.replication_status = networkDic["replication_status"]
        self.size = networkDic["size"]
        self.snapshot_id = networkDic["snapshot_id"]
        self.source_volid = networkDic["source_volid"]
        self.status = networkDic["status"]
        self.type = networkDic["type"]
        self.updated_at = networkDic["updated_at"]
        self.user_id = networkDic["user_id"]
        if networkDic.get("network_image_metadata"):
            self.network_image_metadata = networkDic["network_image_metadata"]






