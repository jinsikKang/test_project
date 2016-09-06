#_*_coding:utf-8_*_

import os

from sdsec import log_handler
from sdsec.log_handler import setLogDir, getLogger

#로그불러왓!
setLogDir()
logger = getLogger(level=log_handler.INFO)


def excuteCmd(command):
    logger.debug("excuteCmd")
    f = os.popen(command)
    logger.debug(command)
    logger.debug(f.read())
    return f

def parsingOutputToList(output):
    rows = output.read().splitlines()
    keyList = rows[1][1:-1].split("|")
    for idx, key in enumerate(keyList):
        keyList[idx] = key.lower().strip().replace(" ", "_")
    resultList = []
    for row in rows[3:-1]:
        resultDic = {}
        cols = row[1:-1].split("|")
        for idx, col in enumerate(cols):
            key = keyList[idx]
            value = col.strip()
            resultDic[key] = value
        resultList.append(resultDic)
    return resultList


def getInstanceList():
    logger.debug("getInstanceList")
    f = excuteCmd("nova list")
    instanceList = parsingOutputToList(f)
    return instanceList