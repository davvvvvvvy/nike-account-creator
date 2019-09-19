from datetime import datetime
import requests
import json
import time
import urllib

class VerSMS:

    def getmobile_cn(token, username, pid):
        try:
            url = "http://www.smscin.com/do.php?action=getmobile&username={}&token={}&pid={}&channel=[channel]".format(username, token, pid)
            t = []
            k=0
            data = requests.post(url)
            '''for k in range(2, 14):
                t.append(data[k])'''
            return data.json()
        except Exception as e:
            print(e)

    def getsms_cn(token, username, pid):
        url = "http://www.smscin.com/do.php?action=getmobile&username={}&token={}&pid={}&channel=[channel]".format(username, token, pid)
        mobile = requests.post(url)
        try:
            url2 = "http://www.smscin.com/do.php?action=getsms&username={}&token={}&pid={}&mobile={}".format(username, token, pid, mobile.json())
            t = []
            k=0
            data = requests.post(url2)
            '''for k in range(0, 14):
                t.append(data[k])'''
            return data.json()
        except Exception as e:
            print(e)

#print(VerSMS.getmobile_cn('594bb8921717645ee6e29c0e79bab72a', 'jayzus@r3seller.fun', 462))
#print(VerSMS.getsms_cn('594bb8921717645ee6e29c0e79bab72a', 'jayzus@r3seller.fun', 462))

#http://www.smscin.com/do.php?action=getmobile&username=jayzus@r3seller.fun&token=594bb8921717645ee6e29c0e79bab72a&pid=628&channel=[channel]
