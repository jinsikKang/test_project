# _*_coding:utf-8_*_

from sdsec.log_handler import setLogDir, getLogger
from ..tools.command import excuteCmd

setLogDir()
logger = getLogger()

class Flavor:
    def outputToInfo(self, infoDic, outputList):
        for row in outputList[3:-1]:
            cols = row[1:-1].split("|")
            key = cols[0].strip().replace(" ", "_")
            value = cols[1].strip()
            infoDic[key] = value
        return infoDic

    def showInfoById(self, id):
        # id로 이미지를 찾는다.
        logger.debug("showFlavorById")
        output = excuteCmd("glance image-show " + id)
        outputList = output.splitlines()
        if outputList:
            flavorDic = {
                "checksum" : "",
                "container_format" : "",
                "created_at" : "",
                "disk_format" : "",
                "id" : "",
                "kernel_id" : "",
                "min_disk" : "",
                "min_ram" : "",
                "name" : "",
                "owner" : "",
                "protected" : "",
                "ramdisk_id" : "",
                "size" : "",
                "status" : "",
                "tags" : "",
                "updated_at" : "",
                "virtual_size" : "",
                "visibility" : "",
            }
            return self.outputToInfo(flavorDic, outputList)
        else:
            logger.debug(str("'" + unicode(id).encode("utf-8") + "' 에 해당하는 이미지가 없습니다."))
            return None

    def __init__(self):
        self.checksum = ""
        self.container_format = ""
        self.created_at = ""
        self.disk_format = ""
        self.id = ""
        self.kernel_id = ""
        self.min_disk = ""
        self.min_ram = ""
        self.name = ""
        self.owner = ""
        self.protected = ""
        self.ramdisk_id = ""
        self.size = ""
        self.status = ""
        self.tags = ""
        self.updated_at = ""
        self.virtual_size = ""
        self.visibility = ""

    def setById(self, id):
        flavorDic = self.showInfoById(id)
        if flavorDic == None:
            raise Exception, unicode(id).encode("utf-8") + "에 해당하는 이미지가 없습니다."
        self.checksum = flavorDic["checksum"]
        self.container_format = flavorDic["container_format"]
        self.created_at = flavorDic["created_at"]
        self.disk_format = flavorDic["disk_format"]
        self.id = flavorDic["id"]
        self.kernel_id = flavorDic["kernel_id"]
        self.min_disk = flavorDic["min_disk"]
        self.min_ram = flavorDic["min_ram"]
        self.name = flavorDic["name"]
        self.owner = flavorDic["owner"]
        self.protected = flavorDic["protected"]
        self.ramdisk_id = flavorDic["ramdisk_id"]
        self.size = flavorDic["size"]
        self.status = flavorDic["status"]
        self.tags = flavorDic["tags"]
        self.updated_at = flavorDic["updated_at"]
        self.virtual_size = flavorDic["virtual_size"]
        self.visibility = flavorDic["visibility"]
