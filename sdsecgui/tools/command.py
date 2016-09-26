#_*_coding:utf-8_*_

import os

from sdsec import log_handler
from sdsec.log_handler import setLogDir, getLogger

#로그불러왓!
setLogDir()
logger = getLogger()


def excuteCmd(command):
    # 명령 실행, 출력 반환
    logger.debug("excuteCmd>> "+command)
    f = os.popen(command)
    result = f.read()
    logger.debug(result)
    return result


def parsingOutputToList(output):
    # 출력을 받아 parsing함
    rows = output.splitlines()
    if rows:
        # index 0 = 테두리
        # index 1 = 키(컬럼명)
        keyList = rows[1][1:-1].split("|")
        for idx, key in enumerate(keyList):
            # 양끝 공백을 없애고 사이공백은 밑줄로 전환
            keyList[idx] = key.lower().strip().replace(" ", "_")
        resultList = []
        for row in rows[3:-1]:
            # index 3 ~ = 목록
            # 한 줄당 하나의 인스턴스
            # 하나의 인스턴스를 Dictionary에 담는다
            resultDic = {}
            cols = row[1:-1].split("|")
            for idx, col in enumerate(cols):
                key = keyList[idx]
                value = col.strip()
                resultDic[key] = value
            # Dictionary를 List에 담아 반환한다.
            resultList.append(resultDic)
        return resultList
    else:
        # 인스턴스가 하나도 없을 때
        logger.debug("List is empty")
        return None


def getInstanceList():
    logger.debug("getInstanceList")

    output = excuteCmd("nova list --all-tenants")
    instanceList = parsingOutputToList(output)

    return instanceList

def getImageList():
    logger.debug("getImageList")

    output = excuteCmd("glance image-list")
    imageList = parsingOutputToList(output)

    return imageList

def login(username, password, tenant_name, auth_url):
    excuteCmd("export OS_USERNAME=" + username)
    excuteCmd("export OS_PASSWORD=" + password)
    excuteCmd("export OS_TENANT_NAME=" + tenant_name)
    excuteCmd("export OS_AUTH_URL=http://" + auth_url + ":35357/v2.0")