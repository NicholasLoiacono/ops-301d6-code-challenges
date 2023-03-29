#!/usr/bin/env python3

# Script: Ops 301d6 Class 12 Ops Challenge Solution
# Author: Nicholas Loiacono
# Date: 03/28/2023
# Purpose: Python Requests Library
# Resources: Chat GPT


# Start

import requests

# Prompt user for destination URL
url = input("Enter destination URL: ")

# Prompt user to select HTTP Method
http_method = input("Select HTTP Method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ")

# Print entire request and ask user to confirm before proceeding
print(f"Request: {http_method} {url}")
confirmation = input("Confirm request (y/n): ")

# Perform request if user confirms
if confirmation.lower() == 'y':
    response = requests.request(http_method, url)
    
    # Translate status code to plain terms and print to screen
    status_codes = {
        100: 'Continue',
        101: 'Switching Protocols',
        200: 'OK',
        201: 'Created',
        202: 'Accepted',
        203: 'Non-Authoritative Information',
        204: 'No Content',
        205: 'Reset Content',
        206: 'Partial Content',
        300: 'Multiple Choices',
        301: 'Moved Permanently',
        302: 'Found',
        303: 'See Other',
        304: 'Not Modified',
        305: 'Use Proxy',
        306: '(Unused)',
        307: 'Temporary Redirect',
        308: 'Permanent Redirect',
        400: 'Bad Request',
        401: 'Unauthorized',
        402: 'Payment Required',
        403: 'Forbidden',
        404: 'Not Found',
        405: 'Method Not Allowed',
        406: 'Not Acceptable',
        407: 'Proxy Authentication Required',
        408: 'Request Timeout',
        409: 'Conflict',
        410: 'Gone',
        411: 'Length Required',
        412: 'Precondition Failed',
        413: 'Request Entity Too Large',
        414: 'Request-URI Too Long',
        415: 'Unsupported Media Type',
        416: 'Requested Range Not Satisfiable',
        417: 'Expectation Failed',
        418: "I'm a teapot",
        422: 'Unprocessable Entity',
        423: 'Locked',
        424: 'Failed Dependency',
        426: 'Upgrade Required',
        428: 'Precondition Required',
        429: 'Too Many Requests',
        431: 'Request Header Fields Too Large',
        444: 'Connection Closed Without Response',
        451: 'Unavailable For Legal Reasons',
        499: 'Client Closed Request',
        500: 'Internal Server Error',
        501: 'Not Implemented',
        502: 'Bad Gateway',
        503: 'Service Unavailable',
        504: 'Gateway Timeout',
        505: 'HTTP Version Not Supported',
        506: 'Variant Also Negotiates',
        507: 'Insufficient Storage',
        508: 'Loop Detected',
        510: 'Not Extended',
        511: 'Network Authentication Required',
        599: 'Network Connect Timeout Error'
    }
    
    if response.status_code in status_codes:
        print(f"Status: {status_codes[response.status_code]} ({response.status_code})")
    else:
        print(f"Status: {response.status_code}")
    
    # Print response headers to screen
    print("\nHeaders:")
    for header, value in response.headers.items():
        print(f"{header}: {value}")

# End