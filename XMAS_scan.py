import logging
# logging.getLogger(“scapy.runtime”).setLevel(logging.ERROR)
from scapy.all import *


logging.getLogger(“scapy.runtime”).setLevel(logging.ERROR)
dst_ip = "10.0.0.1"
src_port = RandShort()
dst_port = 80

"""
In the XMAS scan, a TCP packet with the PSH, FIN, and URG flags set, along with the port to connect to,
is sent to the server. If the port is open, then there will be no response from the server.
If the server responds with the RST flag set inside a TCP packet, the port is closed on the server.
If the server responds with the ICMP packet with an ICMP unreachable error type 3 and ICMP code 1, 2, 3, 9, 10, or 13,
then the port is filtered and it cannot be inferred from the response whether the port is open or closed.
"""
