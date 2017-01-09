# coding=utf-8
import urllib2
import urllib
import socket
import json
import random
from IPProxyPool.settings import *

ip_check_url = 'http://ip.chinaz.com/getip.aspx'
socket_timeout = 3



# Check proxy
def check_proxy(protocol, pip):
    try:
        proxy_handler = urllib2.ProxyHandler({protocol: pip})
        opener = urllib2.build_opener(proxy_handler)
        urllib2.install_opener(opener)

        headers = {}
        headers['User-Agent'] = random.choice(USER_AGENTS)

        req = urllib2.Request(ip_check_url, headers = headers)
        conn = urllib2.urlopen(req)
        # conn = urllib2.urlopen(ip_check_url)
        context = conn.read()
        print "READ: ", context

        proxy_detected = True

    except urllib2.HTTPError, e:
        print "ERROR: Code ", e.code
        return False
    except Exception, detail:
        print "ERROR: ", detail
        return False

    return proxy_detected

def main():
    socket.setdefaulttimeout(socket_timeout)

    i = 0
    r = open('data.json', 'r').read().decode("utf-8")
    PROXIES = json.loads(r)

    while i < len(PROXIES):
        proxy = PROXIES[i]
        protocol = "http"
        current_proxy = proxy['ip_port']
        proxy_detected = check_proxy(protocol, current_proxy)
        if proxy_detected:
            print (" WORKING: " + current_proxy)
        else:
            print " FAILED: %s " % (current_proxy,)
            PROXIES.pop(i)
            i -= 1

        i += 1
    print PROXIES


if __name__ == '__main__':
    main()