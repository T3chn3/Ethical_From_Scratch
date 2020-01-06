#!/usr/bin/env python

import scapy.all as scapy

# def scan(ip):
#     scapy.arping(ip)

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    #print(arp_request.summary())
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether()) #print all the fields for Ether object

    # dst: DestMACField = 'ff:ff:ff:ff:ff:ff'(None)
    # src: SourceMACField = '08:00:27:b4:46:30'(None)
    # type: XShortEnumField = 36864(36864)

    #print(broadcast.summary())

    #merge the two request into one packet with scapy
    arp_request_broadcast = broadcast/arp_request


    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0] #srp allows custom Ether packets / two list are returned  [0] forces the return of only the first list

    #print("ANSWERED")
    #print(answered_list.summary()) #prints verbose output
    print("IP\t\t\t\tMAC Address\n------------------------------------")
    for element in answered_list:
       print(element[1].psrc + "\t\t" + element[1].hwsrc)

    # print("UNANSWERED")
    # print(unanswered_list.summary())
    # print(arp_request_broadcast.summary()) #.show can also be used to display the request
    # arp_request.show()
    # broadcast.show()
    # arp_request_broadcast.show()

#     Ether / ARP
#     who
#     has
#     192.168
#     .0
#     .1
#     says
#     192.168
#     .0
#     .37
#     ###[ ARP ]###
#     hwtype = 0x1
#     ptype = IPv4
#     hwlen = None
#     plen = None
#     op = who - has
#     hwsrc = 0
#     8: 00:27: b4:46: 30
#     psrc = 192.168
#     .0
#     .37
#     hwdst = 00:00: 00:00: 00:00
#     pdst = 192.168
#     .0
#     .1
#
#     ###[ Ethernet ]###
#     dst = ff:ff: ff:ff: ff:ff
#     src = 0
#     8: 00:27: b4:46: 30
#     type = 0x9000
#
#     ###[ Ethernet ]###
#     dst = ff:ff: ff:ff: ff:ff
#     src = 0
#     8: 00:27: b4:46: 30
#     type = ARP
#     ###[ ARP ]###
#     hwtype = 0x1
#     ptype = IPv4
#     hwlen = None
#     plen = None
#     op = who - has
#     hwsrc = 0
#     8: 00:27: b4:46: 30
#     psrc = 192.168
#     .0
#     .37
#     hwdst = 00:00: 00:00: 00:00
#     pdst = 192.168
#     .0
#     .1
#
#
# Process
# finished
# with exit code 0

scan("192.168.0.1/24")