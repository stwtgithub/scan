import sys
import os
import inspect


currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from config import settings
import base64
import requests

class riskiq:

    def __init__(self,target):
        authkey = base64.b64encode((settings.riskiq_user + ':' + settings.riskiq_key).encode('utf8')).decode()
        self.header = {
            'Authorization': 'Basic {}'.format(authkey)
        }

        self.target = target

    def passivedns(self):
        url = 'https://api.riskiq.net/pt/v2/dns/passive?query={}&timeout=7'.format(self.target)
        res = requests.get(url,headers=self.header)
        return res.text


# rq = riskiq('www.target.com')
# rq.passivedns()