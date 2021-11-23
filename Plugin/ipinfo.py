import requests
import dns.resolver

class ipinfo:
    # riskiq
    # def riskiq(self):


    #nslookup
    def dnsresolver(self):
        result_dict = dict()
        for domain in self.domainlist:
            domain_dict = dict()
            try:
                A = dns.resolver.resolve(domain,"A")
            except Exception as e:
                print(e)

            # print (type(A))
            for i in A.response.answer:
                if (i.rdtype == 5):
                    cnamelist = list()
                    for j in i.items:
                        # print("CNAME:" + str(j.target))
                        cnamelist.append(str(j.target))
                    domain_dict['CNAME'] = cnamelist
                
                if (i.rdtype == 1):
                    ipinfolist = list()
                    for j in i.items:
                        # print("IP:" + j.address)
                        ipinfolist.append(j.address)
                    domain_dict['IP'] = ipinfolist
            result_dict[domain] = domain_dict
        return result_dict
        #{'www.baidu.com': {'CNAME': ['www.a.shifen.com.'], 'IP': ['220.181.38.149', '220.181.38.150']}, 'www.qq.com': {'CNAME': ['ins-r23tsuuf.ias.tencent-cloud.net.'], 'IP': ['101.91.42.232', '101.91.22.57']}}


def __init__(self, domainlist):
    self.domainlist = domainlist




# newquery = ipinfo()
# result = newquery.dnsresolver(domainlist)
# print(str(result))
