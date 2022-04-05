import socket
from IPy import IP

# secondry choice if user scan multi target
def scan(_targets, _port_start, _port_end):
    print('\n' + '[-_0 scanning] ' + str(_targets))
    for port in range(_port_start, _port_end):
        scan_port(_targets, port)

# method to check targets it,s ip or not and convert to ip if it not
def convert_ip(_target):
    try:
        IP(_target)
        return _target
    except ValueError:
        return socket.gethostbyname(_target)

# get banner service info method after descover ports 
def get_banner(get):
    return get.recv(1024)

# main method scanner
def scan_port(_ipaddress, _port):
    try:
        sock = socket.socket()
        sock.settimeout(0.2)
        sock.connect((_ipaddress, _port))
        try:
            service_name=socket.getservbyport(_port)
            banner = get_banner(sock)
            print('[+] port ' + str(_port) + ' service name ' + service_name + ' is open : ' + str(banner.decode().strip('\n')))
        except:
            print('[+] port ' + str(_port) + ' service name ' + service_name + ' is open ')
    except:
        pass

if __name__ == "__main__":
    #receve host from user
    targets = input('[+] Enter target/s without (http) To scan(multiply targets with (,): ')
    #receve start port from user
    port_start = int(input('Enter port start :'))
    #receve end port from user
    port_end = int(input('Enter port end :'))
    #check target input indevdual target or multi target
    if ',' in targets:
        for ip_addr in targets.split(','):
            scan(ip_addr.strip(' '), port_start, port_end)
    else:
        scan(targets, port_start, port_end)
