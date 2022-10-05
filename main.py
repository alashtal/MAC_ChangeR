#!/usr/bin/env python

import subprocess
import optparse

# -h or --help can help you see how to use the program
parse = optparse.OptionParser()
parse.add_option("-i", "--interface", dest="interface", help="The interface you wish to change its MAC address")
parse.add_option("-m", "--mac", dest="new_MAC", help="The new MAC address you wish to change to")

(options, arguments) = parse.parse_args()

interface = options.interface
new_mac = options.new_MAC


print("[+]Changing MAC address of " + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

# Oldie but goldie
# interface = input("heyy")
# subprocess.call("ifconfig " + interface + " down", shell=True)
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
# subprocess.call("ifconfig " + interface + " up", shell=True)

print(subprocess.call("ifconfig"))
