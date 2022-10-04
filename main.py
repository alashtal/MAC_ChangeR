#!/usr/bin/env python

import subprocess
interface = "eth0"
new_mac = "00:77:66:55:44:43"
print("[+] Changing MAC address of " + interface + " to " + new_mac)

subprocess.call("ifconfig " + interface + " down", shell=True)
subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
subprocess.call("ifconfig " + interface + " up", shell=True)

print(subprocess.call("ifconfig"), shell=True)
