#!/usr/bin/env python

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
import socket
import requests
import uuid
import ifaddr



# -----------------------------------------------------------------------------
# Variables
# -----------------------------------------------------------------------------
external_ip_resolver = 'http://icanhazip.com'



def network_info():
    print('Hostname:\t' + str(socket.gethostname()))
    print('FQDN:\t\t' + str(socket.getfqdn()))
    #print('Internal IP:\t' + str(socket.gethostbyname(socket.gethostname())))
    print('External IP:\t' + str(requests.get(external_ip_resolver).text.strip()))
    print('Connected MAC:\t' + str(__get_mac()))
    __print_network_adapter_info()



def __get_mac():
    mac_num = hex(uuid.getnode()).replace('0x', '').upper()
    mac = '-'.join(mac_num[i: i + 2] for i in range(0, 11, 2))
    return mac



def __print_network_adapter_info():
    adapters = ifaddr.get_adapters()

    for adapter in adapters:
        print('Network adapter: ' + str(adapter.nice_name))
        for ip in adapter.ips:
            if len(ip.ip) == 3:
                print('\tIPv6: ' + str(ip.ip[0]) + '/' + str(ip.network_prefix))
            else:
                print('\tIPv4: ' + str(ip.ip) + '/' + str(ip.network_prefix))
    


# not used right now
def __getHwAddr(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
    return ''.join(['%02x:' % ord(char) for char in info[18:24]])[:-1]




if __name__ == "__main__":
    network_info()
