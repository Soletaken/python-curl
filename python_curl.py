import argparse

import requests
import simplejson as json


def getArgs():
    parser = argparse.ArgumentParser(description='curl in python.')
    parser.add_argument('--url', '-u')
    parser.add_argument('--User', '-U')
    parser.add_argument('--Password', '-P')
    parser.add_argument('--Headers', '-H', nargs='+')
    return parser.parse_args()


def getUrl(args):
    if args.url is None:
        print("You have to specify url with argument -u")
        exit(2)
    return args.url


def getHeaders(args):
    if args.Headers is None:
        return {}
    return {header.split(":")[0]: header.split(":")[1].strip() for header in args.Headers}


def sendRequest(url, headers, user, password):
    if user is not None and password is not None:
        return requests.get(url, headers=headers, auth=(user, password))
    return requests.get(url, headers=headers)


class Result:
    def __init__(self, response, request_url, request_headers):
        self.status_code = response.status_code
        self.response = Response(response).__dict__
        self.request = Request(request_url, request_headers).__dict__


class Response:
    def __init__(self, response):
        self.data = json.loads(response.content or "{}")
        self.headers = dict(response.headers)


class Request:
    def __init__(self, request_url, request_headers):
        self.url = request_url
        self.headers = request_headers


args = getArgs()
headers = getHeaders(args)
url = getUrl(args)
httpResponse = sendRequest(url, headers, args.User, args.Password)
result = Result(httpResponse, url, headers)

print(json.dumps(result.__dict__, indent=2))
