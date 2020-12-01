import logging
# logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy import *


logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

dst_ip = "10.0.0.1"
src_port = RandShort()
dst_port = 80

tcp_connect_scan_resp = sr1(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=10)

if(str(type(tcp_connect_scan_resp))=="<type 'NoneType'>"):
    print("Closed")

elif(tcp_connect_scan_resp.haslayer(TCP)):
    if(tcp_connect_scan_resp.getlayer(TCP).flags == 0x12):
        send_rst = sr(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="AR"),timeout=10)
        print("Open")

elif (tcp_connect_scan_resp.getlayer(TCP).flags == 0x14): 
    print("Closed")
    
"""
TCP connect is a three-way handshake between the client and the server.
If the three-way handshake takes place, then communication has been established.
A client trying to connect to a server on port 80 initializes the connection by sending a TCP packet,
with the SYN flag set and the port to which it wants to connect (in this case port 80).
If the port is open on the server and is accepting connections,
it responds with a TCP packet with the SYN and ACK flags set.
The connection is established by the client sending an acknowledgement ACK and RST flag in the final handshake.
If this three-way handshake is completed, then the port on the server is open.
The client sends the first handshake using the SYN flag and port to connect to the server in a TCP packet.
If the server responds with a RST instead of a SYN-ACK, then that particular port is closed on the server.
"""
