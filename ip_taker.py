from urllib.request import urlopen
import re as r

class IP():
    def getIP(self):
        d = str(urlopen('http://checkip.dyndns.com/').read())
        print(d)
        return r.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(d).group(1)