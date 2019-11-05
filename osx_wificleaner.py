#!/usr/bin/python

import os
import plistlib
import re
import subprocess
import sys

if os.geteuid() != 0:
    os.execvp("sudo", ["sudo"] + sys.argv)

interfacelist = subprocess.Popen(["/usr/sbin/networksetup","-listallhardwareports"], stdout=subprocess.PIPE).communicate()[0]
try:
	interface = re.search('Wi-Fi\nDevice:\ (.+?)\n', interfacelist.decode()).group(1)
except Exception as e:
	print( "Can't find wireless device, exiting...")
	print(str(e))
	quit()

try:
	networklist = plistlib.readPlist('/Library/Preferences/SystemConfiguration/com.apple.airport.preferences.plist')["KnownNetworks"]
except:
	print( "PList for Network is missing or no networks saved")
	quit()

opennetworks = []

print( "====== List of preferred networks ======")

for wifilist in networklist:
	wifi = networklist["{0}".format(wifilist)]
	print( "[-] Saved Network {0} - Encryption: {1}".format(wifi["SSID"].data, wifi["SecurityType"]))
	if (wifi["SecurityType"] == "Open"):
		opennetworks.append(wifi["SSID"].data)

print( "\n")
print( "====== Removing 'Open' networks from list ======")
print( "++++++++++++++++++++++++++++++++++++++++++++++++")

for network in opennetworks:
	print( "[+] Removing {0}".format(network))
	subprocess.call(["/usr/sbin/networksetup", "-removepreferredwirelessnetwork", interface, network])
