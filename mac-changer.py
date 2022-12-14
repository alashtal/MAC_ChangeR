#!/usr/bin/env python
import subprocess
import optparse
import re

# -h or --help can help you see how to use the program


def change_mac(interface, new_mac):
    print("[+]Changing MAC address of " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_arguments():
    parse = optparse.OptionParser()
    parse.add_option("-i", "--interface", dest="interface", help="The interface you wish to change its MAC address")
    parse.add_option("-m", "--mac", dest="new_MAC", help="The new MAC address you wish to change to")

    (options, arguments) = parse.parse_args()
    if not options.interface:
        parse.error("[-] Please enter an interface '-i' or check '-h' for further help ")
    elif not options.new_MAC:
        parse.error("[-] Please enter an interface '-i' or check '-h' for further help ")
    return options


def process_mac_result(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    regex_mac_results = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result.decode('utf-8')) # another solution for py vs py 3 is str(ifconfig_result)
    if regex_mac_results:
        return regex_mac_results.group(0)
    else:
        print("[-] Could not read MAC address, Please check again.")


options = get_arguments()

current_mac = process_mac_result(options.interface)
# print("Current MAC = " + str(current_mac))

change_mac(options.interface, options.new_MAC)
current_mac = process_mac_result(options.interface)

if current_mac == options.new_MAC:
    print("[+] MAC address has successfully been changed to " + current_mac)
else:
    print("[-] Could not change the MAC address, Please try again.")
