
"""
This technique is similar to the TCP connect scan. The client sends a TCP packet with the SYN flag set and the port number to connect to.
If the port is open, the server responds with the SYN and ACK flags inside a TCP packet.
But this time the client sends a RST flag in a TCP packet and not RST+ACK, which was the case in the TCP connect scan.
This technique is used to avoid port scanning detection by firewalls.
The closed port check is same as that of TCP connect scan.
The server responds with an RST flag set inside a TCP packet to indicate that the port is closed on the server
"""
