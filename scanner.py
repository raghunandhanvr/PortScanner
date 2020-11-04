import socket

target="IP"                                                            #Add the IP need to be scanned

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False

for port in range(1, 1024):
    result = portscan(port)
    if(result):
        print("Port {} - Open".format(port))
