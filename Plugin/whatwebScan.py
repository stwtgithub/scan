import requests

class whatwebScan:
    
    def scan(self):
        url = 'https://www.whatweb.net/whatweb.php'
        

        res = requests.post(url, data={'target':'{}'.format(self.target)})
        return res.text
    
    def __init__(self, target):
        self.target = target


# what = whatwebScan('www.baid.com')
# what.scan()