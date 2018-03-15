#!/usr/bin/python
import requests

def getMacVendor(mac):
    """Returns the name of the MAC address vendor."""
    r = requests.get("http://api.macvendors.com/%s" %mac)
    if r.status_code == 404:
        return "%s not found!!" %mac
    else:
        return r.text

vendor = getMacVendor("00:17:61:12:a9:2a")
print(vendor)     