# _*_coding:utf-8_*_

import json


class Base:
    @classmethod
    def outputToInfo(cls, infoDic, outputList):
        for row in outputList[3:-1]:
            cols = row[1:-1].split("|")
            key = cols[0].strip().replace(" ", "_")
            value = cols[1].strip()
            infoDic[key] = value
        return infoDic

    @classmethod
    def toJSON(self):
        return json.loads(json.dumps(self, default=lambda o:o.__dict__, sort_keys=True, indent=4))

    @classmethod
    def showInfoById(cls, id):
        pass

    @classmethod
    def showInfoJsonById(cls, id):
        pass

    @classmethod
    def setById(cls, id):
        pass