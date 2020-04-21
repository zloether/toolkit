#!/usr/bin/env python

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
import requests




def download(url, verify=ca_cert):
    r = requests.get(url, verify=verify)
    return r.text

def use_session(url, verify=ca_cert):
    s = create_session()
    r = s.get(url, verify=verify)
    return r.text

if __name__ == "__main__":
    url = 'https://icanhazip.com'
    print(use_session(url))