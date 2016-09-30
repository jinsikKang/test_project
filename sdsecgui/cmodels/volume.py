# _*_coding:utf-8_*_

from sdsec.log_handler import setLogDir, getLogger
from ..tools.command import excuteCmd, login

# setLogDir()
# logger = getLogger()

class Volume:
    def outputToInfo(self, outputList):
        infoDic = {}
        for row in outputList[3:-1]:
            cols = row[1:-1].split("|")
            key = cols[0].strip().replace(" ", "_")
            value = cols[1].strip()
            infoDic[key] = value
        return infoDic

    def showInfoById(self, id):
        # id로 볼륨을 찾는다.
        # logger.debug("showVolumeById")
        output = excuteCmd("openstack volume show " + id)

        outputList = output.splitlines()
        if outputList:
            return self.outputToInfo(outputList)
        else:
            # logger.debug(str("'" + unicode(id).encode("utf-8") + "' 에 해당하는 인스턴스가 없습니다."))
            return None

    def __init__(self):
        self.attachments = ""
        self.availability_zone = ""
        self.bootable = ""
        self.consistencygroup_id = ""
        self.created_at = ""
        self.description = ""
        self.encrypted = ""
        self.id = ""
        self.migration_status = ""
        self.multiattach = ""
        self.name = ""
        self.os_vol_host_attr = {}
        self.os_vol_tenant_attr = {}
        self.os_vol_mig_status_attr = {}
        self.os_vol_host_attr["host"] = ""
        self.os_vol_tenant_attr["tenant_id"] = ""
        self.os_vol_mig_status_attr["migstat"] = ""
        self.os_vol_mig_status_attr["name_id"] = ""
        self.properties = ""
        self.replication_status = ""
        self.size = ""
        self.snapshot_id = ""
        self.source_volid = ""
        self.status = ""
        self.type = ""
        self.updated_at = ""
        self.user_id = ""
        self.volume_image_metadata = ""

    def setById(self, id):
        volumeDic = self.showInfoById(id)
        if volumeDic == None:
            raise Exception, unicode(id).encode("utf-8") + "에 해당하는 인스턴스가 없습니다."
        self.attachments = volumeDic["attachments"]
        self.availability_zone = volumeDic["availability_zone"]
        self.bootable = volumeDic["bootable"]
        self.consistencygroup_id = volumeDic["consistencygroup_id"]
        self.created_at = volumeDic["created_at"]
        self.description = volumeDic["description"]
        self.encrypted = volumeDic["encrypted"]
        self.id = volumeDic["id"]
        self.migration_status = volumeDic["migration_status"]
        self.multiattach = volumeDic["multiattach"]
        self.name = volumeDic["name"] if volumeDic["name"] else volumeDic["id"]
        self.os_vol_host_attr["host"] = volumeDic["os-vol-host-attr:host"]
        self.os_vol_mig_status_attr["migstat"] = volumeDic["os-vol-mig-status-attr:migstat"]
        self.os_vol_mig_status_attr["name_id"] = volumeDic["os-vol-mig-status-attr:name_id"]
        self.os_vol_tenant_attr["tenant_id"] = volumeDic["os-vol-tenant-attr:tenant_id"]
        self.properties = volumeDic["properties"]
        self.replication_status = volumeDic["replication_status"]
        self.size = volumeDic["size"]
        self.snapshot_id = volumeDic["snapshot_id"]
        self.source_volid = volumeDic["source_volid"]
        self.status = volumeDic["status"]
        self.type = volumeDic["type"]
        self.updated_at = volumeDic["updated_at"]
        self.user_id = volumeDic["user_id"]
        if volumeDic.get("volume_image_metadata"):
            self.volume_image_metadata = volumeDic["volume_image_metadata"]






