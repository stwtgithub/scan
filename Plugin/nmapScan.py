import nmap

# 需要安装nmap，添加到环境变量
class nmapScan:
    def __init__(self, iplist, param):
        self.iplist = iplist 
        self.param = param
    
    def scan(self):
        result_dict = dict()
        nm = nmap.PortScanner()
        ip = ",".join(str(i) for i in self.iplist)
     
        nm.scan(ip, arguments=self.param)
        result_dict['command'] = nm.command_line()
     
        result_dict['all_hosts'] = nm.all_hosts()
        for ip in self.iplist:
            result_dict[ip] = nm[ip]
        return result_dict


# nm1 = nmapScan(iplist=['127.0.0.1'],param='-sS -Pn -p 80')
# result = nm1.scan()
# print(str(result))