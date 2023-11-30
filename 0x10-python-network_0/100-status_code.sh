#!/bin/bash
# Issue a GET request to a specified URL and show the status code of the response.
curl -s -o /dev/null -w "%{http_code}" "$1"
