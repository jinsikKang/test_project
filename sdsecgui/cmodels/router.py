# _*_coding:utf-8_*_
import json
import re

from ..tools.command import excuteCmd
from base import Base

class Router(Base):
    def showInfoJsonById(cls, id):
        output = json.loads(excuteCmd("neutron router-show " + id + " -f json"))
        if output:
            return output
        else:
            return None

    def setById(cls, id):
        cls.routerDic = cls.showInfoJsonById(id)