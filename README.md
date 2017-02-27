# osx-wificleaner
Cleans out "open" wireless connections from OSX machines

- Inspired by: https://isc.sans.edu/forums/diary/Investigating+OffPremise+Wireless+Behaviour+or+I+Know+What+You+Connected+To/22089/
- For a Windows / Powershell script you can find `Get-OpenWifiNetworks.ps1` here: https://github.com/secopsconsult/powershell

Example run:
```
wpad:osx-wificleaner mubix$ sudo ./osx_wificleaner.py
Password:
====== List of preferred networks ======
[-] Saved Network hhonors - Encryption: Open
[-] Saved Network MyHomeWif - Encryption: WPA/WPA2 Personal
[-] Saved Network UnitedWifi - Encryption: Open
[-] Saved Network GuestNetwork - Encryption: Open
[-] Saved Network gogoinflight - Encryption: Open
[-] Saved Network PhoneHotspot - Encryption: WPA2 Personal
[-] Saved Network WorkWifi - Encryption: WPA2 Personal
[-] Saved Network iPadHotSpot - Encryption: WPA2 Personal
[-] Saved Network FreePublicWifi - Encryption: Open
[-] Saved Network Ruxcon - Encryption: WPA2 Personal

====== Removing 'Open' networks from list ======
++++++++++++++++++++++++++++++++++++++++++++++++
[+] Removing hhonors
Removed hhonors from the preferred networks list
[+] Removing UnitedWifi
Removed UnitedWifi from the preferred networks list
[+] Removing GuestNetwork
Removed GuestNetwork from the preferred networks list
[+] Removing gogoinflight
Removed gogoinflight from the preferred networks list
[+] Removing FreePublicWifi
Removed FreePublicWifi from the preferred networks list
wpad:osx-wificleaner mubix$
```
