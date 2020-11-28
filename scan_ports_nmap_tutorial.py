#  python-nmap is a python library which helps in using nmap port scanner. 
#  DOCS:  https://xael.org/pages/python-nmap-en.html

#  pip install python-nmap

import nmap


nm = nmap.PortScanner()
nm.scan('127.0.0.1', '22-443')

nm.command_line()
# 'nmap -oX - -p 22-443 -sV 127.0.0.1'

nm.scaninfo()
# {'tcp': {'services': '22-443', 'method': 'connect'}}

nm.all_hosts()
# ['127.0.0.1']

nm['127.0.0.1'].hostname()
# 'localhost'

nm['127.0.0.1'].state()
# 'up'

nm['127.0.0.1'].all_protocols()
# ['tcp']

nm['127.0.0.1']['tcp'].keys()
# [80, 25, 443, 22, 111]

nm['127.0.0.1'].has_tcp(22)
# True

nm['127.0.0.1'].has_tcp(23)
#False

nm['127.0.0.1']['tcp'][22]
# {'state': 'open', 'reason': 'syn-ack', 'name': 'ssh'}

nm['127.0.0.1'].tcp(22)
# {'state': 'open', 'reason': 'syn-ack', 'name': 'ssh'}

nm['127.0.0.1']['tcp'][22]['state']
# 'open'

for host in nm.all_hosts():
    print('----------------------------------------------------')
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    print('State : %s' % nm[host].state())
    for proto in nm[host].all_protocols():
        print('----------')
        print('Protocol : %s' % proto)

        lport = nm[host][proto].keys()
        lport.sort()
        for port in lport:
            print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state'])
