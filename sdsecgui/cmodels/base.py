# _*_coding:utf-8_*_

from sdsec.log_handler import setLogDir, getLogger
from ..tools.command import excuteCmd, login

setLogDir()
logger = getLogger()

class Instance:
    @classmethod
    def outputToInfo(cls, infoDic, outputList):
        for row in outputList[3:-1]:
            cols = row[1:-1].split("|")
            key = cols[0].strip().replace(" ", "_")
            value = cols[1].strip()
            infoDic[key] = value
        return infoDic

    @classmethod
    def showInfoById(cls, id):
        pass

    @classmethod
    def setById(cls, id):
        pass