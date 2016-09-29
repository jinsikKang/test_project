# _*_coding:utf-8_*_

from sdsec.log_handler import setLogDir, getLogger
from ..tools.command import excuteCmd, login

setLogDir()
logger = getLogger()

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
        # id로 인스턴스를 찾는다.
        logger.debug("showVolumeById")
        output = excuteCmd("openstack volume show " + id)

        outputList = output.splitlines()
        if outputList:
            return self.outputToInfo(outputList)
        else:
            logger.debug(str("'" + unicode(id).encode("utf-8") + "' 에 해당하는 인스턴스가 없습니다."))
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
        self.volume_image_metadat = ""

    def setById(self, id):
        volumeDic = self.showInfoById(id)
        print volumeDic
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
        self.name = volumeDic["name"]
        self.os_vol_host_attr["host"] = volumeDic["os_vol_host_attr:host"]
        self.os_vol_mig_status_attr["migstat"] = volumeDic["os_vol_mig_status_attr:migstat"]
        self.os_vol_mig_status_attr["name_id"] = volumeDic["os_vol_mig_status_attr:name_id"]
        self.os_vol_tenant_attr["tenant_id"] = volumeDic["os_vol_tenant_attr:tenant_id"]
        self.properties = volumeDic["properties"]
        self.replication_status = volumeDic["replication_status"]
        self.size = volumeDic["size"]
        self.snapshot_id = volumeDic["snapshot_id"]
        self.source_volid = volumeDic["source_volid"]
        self.status = volumeDic["status"]
        self.type = volumeDic["type"]
        self.updated_at = volumeDic["updated_at"]
        self.user_id = volumeDic["user_id"]
        self.volume_image_metadata = volumeDic["volume_image_metadata"]











        self.os_dce["diskConfig"] = volumeDic["OS-DCF:diskConfig"]
        self.os_ext_az["availability_zone"] = volumeDic["OS-EXT-AZ:availability_zone"]
        self.os_ext_srv_attr["host"] = volumeDic["OS-EXT-SRV-ATTR:host"]
        self.os_ext_srv_attr["hostname"] = volumeDic["OS-EXT-SRV-ATTR:hostname"]
        self.os_ext_srv_attr["hypervisor_hostnam"] = volumeDic["OS-EXT-SRV-ATTR:hypervisor_hostnam"]
        self.os_ext_srv_attr["volume_name"] = volumeDic["OS-EXT-SRV-ATTR:volume_name"]
        self.os_ext_srv_attr["kernel_id"] = volumeDic["OS-EXT-SRV-ATTR:kernel_id"]
        self.os_ext_srv_attr["launch_index"] = volumeDic["OS-EXT-SRV-ATTR:launch_index"]
        self.os_ext_srv_attr["ramdisk_id"] = volumeDic["OS-EXT-SRV-ATTR:ramdisk_id"]
        self.os_ext_srv_attr["reservation_id"] = volumeDic["OS-EXT-SRV-ATTR:reservation_id"]
        self.os_ext_srv_attr["root_device_name"] = volumeDic["OS-EXT-SRV-ATTR:root_device_name"]
        self.os_ext_srv_attr["user_data"] = volumeDic["OS-EXT-SRV-ATTR:user_data"]
        self.os_ext_sts["power_state"] = volumeDic["OS-EXT-STS:power_state"]
        self.os_ext_sts["task_state"] = volumeDic["OS-EXT-STS:task_state"]
        self.os_ext_sts["vm_state"] = volumeDic["OS-EXT-STS:vm_state"]
        self.os_extended_volumes["volumes_attached"] = volumeDic["os-extended-volumes:volumes_attached"]
        self.os_srv_usg["launched_at"] = volumeDic["OS-SRV-USG:launched_at"]
        self.os_srv_usg["terminated_at"] = volumeDic["OS-SRV-USG:terminated_at"]

        self.accessIPv4 = volumeDic["accessIPv4"]
        self.accessIPv6 = volumeDic["accessIPv6"]
        self.config_drive = volumeDic["config_drive"]
        self.created = volumeDic["created"]
        self.description = volumeDic["description"]
        self.flavor = volumeDic["flavor"]
        self.hostId = volumeDic["hostId"]
        self.host_status = volumeDic["host_status"]
        self.id = volumeDic["id"]
        self.image = volumeDic["image"]
        self.key_name = volumeDic["key_name"]
        self.locked = volumeDic["locked"]
        self.metadata = volumeDic["metadata"]
        self.name = volumeDic["name"]
        self.progress = volumeDic["progress"]
        self.public_network = volumeDic["public_network"]
        self.security_groups = volumeDic["security_groups"]
        self.status = volumeDic["status"]
        self.tags = volumeDic["tags"]
        self.tenant_id = volumeDic["tenant_id"]
        self.updated = volumeDic["updated"]
        self.user_id = volumeDic["user_id"]