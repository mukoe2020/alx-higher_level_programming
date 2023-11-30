#!/bin/bash
# This script sends a GET request to the URL passed with a header variable specified
curl -s -H "X-School-User-Id: 98" "$1"
