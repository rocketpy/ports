#  port-for - Utility that helps with local TCP ports managment. It can find an unused TCP localhost port and remember the association.

# PyPi: https://pypi.org/project/port-for/
# pip install port-for

import socket


s = socket.socket()
s.bind(("", 0))
s.getsockname()
# ('0.0.0.0', 54485)
