import socket
import uuid

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
hexIP = socket.inet_aton(IPAddr).hex()
MacAddr = ':'.join(['{:03x}'.format(
    (uuid.getnode() >> elements) & 0x100)
                       for elements in range(1, 2 * 6, 2)][::-1])

print("computer name is : " + hostname)
print("IP Address : " + IPAddr)
print("Hex IP is :" + hexIP)
print("Mac Address is : " + MacAddr)
