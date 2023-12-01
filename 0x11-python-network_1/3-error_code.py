#!/usr/bin/python3
"""
 Python script that takes in a URL,
sends a request to the URL and displays the body of the response
Manages urllib.error.HTTPError exceptions and
print: Error code: followed by the HTTP status code
"""
import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as reply:
            print(reply.read().decode("ascii"))
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
