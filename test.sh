#!/bin/bash
# example usage
python python_curl.py -h
python python_curl.py -u "https://httpbin.org/json" -H "accept: application/json"
python python_curl.py -u "https://httpbin.org/basic-auth/awd/awd" -H "accept: application/json" -U awd -P awd
