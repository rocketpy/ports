# The python-nmap library helps to programmatically manipulate scanned results of nmap to automate port scanning tasks. 
# To use this library you must have the Nmap software installed. This can be installed from https://nmap.org/download.html.
# Network Mapper (Nmap) is a free and open-source tool used for network discovery and security auditing. 
# It runs on all major computer operating systems, and official binary packages are available for Linux, Windows, and Mac OS X.
# For Windows 7 and later, you must also upgrade 'NCap' from https://nmap.org/npcap/ 
# For Windows, make sure nmap.exe is added to PATH.
# When you're ready, pip install python-nmap

import time
import nmap


nm = nmap.PortScanner() #initialize PortScanner object
host = '45.60.112.163'  #specify host
nm.scan(host, '1-100') #run the scan, specify host and range of ports to scan

#Optional steps for verification:

#Output: nmap -oX - -p 1-100 -sV 45.60.112.163
print(nm.command_line()) #command_line command to execute on nmap command prompt

#Output: {'tcp': {'method': 'syn', 'services': '1-100'}}
print(nm.scaninfo())   #nmap scan information

#Now we can scan all hosts
#From Official documentation at https://xael.org/pages/python-nmap-en.html
start_time = time.time()   #To get program execution time
for host in nm.all_hosts(): 
    print('----------------------------------------------------')
    print('Host : %s (%s)' % (host, nm[host].hostname()))
    print('State : %s' % nm[host].state())
    for proto in nm[host].all_protocols():
        print('----------')
        print('Protocol : %s' % proto)
        lport = nm[host][proto].keys()
        for key in sorted(lport):
            for port in lport:
                print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
print('Execution time: %s seconds' % (time.time() - start_time))


# To convert output to csv, use:
# print(nm.csv())
