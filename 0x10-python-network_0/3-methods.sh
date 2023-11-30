#!/bin/bash
# A bash script that displays the list of HTTP methods allows
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
