#!/usr/bin/python3
import urllib.request

"""Fetchs https://alx-intranet.hbtn.io/status
"""


def fetch_url():
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status')\
                                as response:
        res = response.read()
        print("Body response:")
        print("\t - type: {}".format(type(res)))
        print("\t - content: {}".format(res))
        print("\t - utf8 content: {}".format(res.decode('utf-8')))


if __name__ == "__main__":
    fetch_url()
