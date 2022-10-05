#!/usr/bin/env python

import subprocess
import optparse

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


options = get_arguments()
# change_mac(options.interface, options.new_MAC)
ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
print(ifconfig_result)
# Old code
# interface = input("heyy")
# subprocess.call("ifconfig " + interface + " down", shell=True)
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
# subprocess.call("ifconfig " + interface + " up", shell=True)
