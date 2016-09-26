# _*_coding:utf-8_*_

from sdsec.log_handler import setLogDir, getLogger
from ..tools.command import excuteCmd, login

setLogDir()
logger = getLogger()

class Image:
    def outputToInfo(self, infoDic, outputList):
        for row in outputList[3:-1]:
            cols = row[1:-1].split("|")
            key = cols[0].strip().replace(" ", "_")
            value = cols[1].strip()
            infoDic[key] = value
        return infoDic

    def showInfoById(self, id):
        # id로 인스턴스를 찾는다.
        logger.debug("showImageById")
        output = excuteCmd("glance image-show " + id)
        outputList = output.splitlines()
        if outputList:
            imageDic = {
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
            return self.outputToInfo(imageDic, outputList)
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
        imageDic = self.showInfoById(id)
        if imageDic == None:
            raise Exception, unicode(id).encode("utf-8") + "에 해당하는 인스턴스가 없습니다."
        self.checksum = imageDic["checksum"]
        self.container_format = imageDic["container_format"]
        self.created_at = imageDic["created_at"]
        self.disk_format = imageDic["disk_format"]
        self.id = imageDic["id"]
        self.kernel_id = imageDic["kernel_id"]
        self.min_disk = imageDic["min_disk"]
        self.min_ram = imageDic["min_ram"]
        self.name = imageDic["name"]
        self.owner = imageDic["owner"]
        self.protected = imageDic["protected"]
        self.ramdisk_id = imageDic["ramdisk_id"]
        self.size = imageDic["size"]
        self.status = imageDic["status"]
        self.tags = imageDic["tags"]
        self.updated_at = imageDic["updated_at"]
        self.virtual_size = imageDic["virtual_size"]
        self.visibility = imageDic["visibility"]
