from requests import *


def isConnected(url):
    try:
        test = get(url=url, timeout=2)
        return True
    except Exception as ex:
        return False


print(isConnected('http://180.97.33.108/'))
