from datetime import datetime
import requests
import json
import time
import urllib

class VerifySMS:

    def getmobile(token, location):
        try:
            url = "http://simsms.org/priemnik.php?metod=get_number&country={}&service=opt86&apikey={}".format(location, token)
            t = []
            k=0
            data = json.loads(requests.get(url).text)["number"]
            for k in range(2, len(data)):
                t.append(data[k])
            return t
        except Exception as e:
            print(e)
            print("No balance!")

    def getsms(token, location):
        try:
            url2 = "http://simsms.org/priemnik.php?metod=get_sms&country={}&service=opt86&id=25623&apikey={}".format(location, token)
            f = []
            i=0
            data = json.loads(requests.get(url2).text)["sms"]
            for i in range(0, len(data)):
                f.append(data[i])
            return f
        except Exception as e:
            print(e)
            print("No balance!")

#print(VerifySMS.getmobile('0MP3nw6Q2JCyneIwMzaFMDXrOrA6ir', 'UK'))
#print(VerifySMS.getsms('0MP3nw6Q2JCyneIwMzaFMDXrOrA6ir', 'UK'))
