#!/usr/bin/env python

#default MAC: 08:00:27:b4:46:30
# A simple script to change the MAC address of a host

import subprocess
import optparse
import re
def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC")  # defining the help option and parsed variable
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options,arguments) = parser.parse_args()
    if not options.interface:   #if options.interface is true
        #code to handle error case
        #print error
        parser.error("[-] Please specify an interface, use --help or -h for more info.")
    elif not options.new_mac:
        #code to handle error case
        parser.error("[-] Please specify a MAC address, use --help or -h for more info.")
    return options

def change_mac(interface, new_mac):
    print("[+] Changing the MAC address for " + interface + " to " + new_mac)
    #subprocess.call("ifconfig", shell=True)
    subprocess.call("ifconfig " + interface + " down", shell=True)
    subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
    subprocess.call("ifconfig " + interface + " up", shell=True)

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    # print(ifconfig_result)
    mac_address_search_result = re.search("\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    # if no MAC address was discovered, return the following error
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address.")

options = get_args()  #sets args
current_mac = get_current_mac(options.interface) #grabs the current MAC address
print ("Current MAC = " + str(current_mac)) #prints the current MAC
change_mac(options.interface,options.new_mac) #changes MAC
current_mac = get_current_mac(options.interface) #grabs the current MAC address

#test if the mac was changed to the provided value
if current_mac == options.new_mac:
    print("[+] MAC address was successfully changed to " + current_mac)
    print("[+] MAC address has been changed to: " + str(current_mac))
else:
    print("[-] MAC address was not changed")


# Testing: python MAC_flipper_10.py -i eth0 -m 22:33:33:aa:aa:aa
# Testing: python MAC_flipper_10.py -i lo -m 22:33:33:aa:aa:aa  , Linux Virtual interface contains no MAC 