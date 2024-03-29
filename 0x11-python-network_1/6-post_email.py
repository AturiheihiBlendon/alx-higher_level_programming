#!/usr/bin/python3
"""cript that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter
and displays the body of the response (decoded in utf-8)
"""
import requests
import sys


def Post_email():
    """sends a POST request to the passed URL with the email as a parameter
    and displays the body of the response (decoded in utf-8)
    """
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)


if __name__ == "__main__":
    Post_email()
