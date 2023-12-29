import requests
import argparse
import sys
import os
from colorama import Fore
import validators
import time

# Validations

def check(url_list):
    for url in url_list:
        if not validators.url(url):
            print("You must specify a valid URL: {}".format(url))
            print("Exiting...")
            sys.exit(1)

def exploit(url_list, timeout, outfile):
    
    try:

        with open(outfile, "w") as f:
            f.write("Vulnerable domains\n\t")

            for url in url_list:

                print(Fore.WHITE + "Target Url {}".format(url))
                print(Fore.RED+"------------------------------------------------------------------------")

                try:
                    response = requests.get(url, timeout=timeout)

                    if 'X-Frame-Options' not in response.headers or 'frame-ancestors' not in response.headers:
                        print(Fore.GREEN + "\nYour target is vulnerable")
                        print(Fore.GREEN + "Saving Vulnerable Url into Output File")
                        time.sleep(3)
                        f.write(url + "\n")
                    else:
                        print("Not vulnerable: {}".format(url))

                except requests.exceptions.RequestException:
                    print(f"An error occurred while connecting to the application: {url}")

    except Exception:

        print(Fore.RED+"An error occurred while opening or writing to the output file: {}".format(outfile))
        print("Thank You For Using")
        time.sleep(2)
        sys.exit()   



if __name__ == '__main__':

    print(Fore.LIGHTWHITE_EX +"-------------------------------------------------------------------------------------------------")
    print(Fore.RED + '''
        ░█████╗░██╗░░░░░██╗░█████╗░██╗░░██╗░░░░░██╗░█████╗░░█████╗░██╗░░██╗░██████╗░█████╗░░█████╗░███╗░░██╗"
        "██╔══██╗██║░░░░░██║██╔══██╗██║░██╔╝░░░░░██║██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗██╔══██╗████╗░██║"
        "██║░░╚═╝██║░░░░░██║██║░░╚═╝█████═╝░░░░░░██║███████║██║░░╚═╝█████═╝░╚█████╗░██║░░╚═╝███████║██╔██╗██║"
        "██║░░██╗██║░░░░░██║██║░░██╗██╔═██╗░██╗░░██║██╔══██║██║░░██╗██╔═██╗░░╚═══██╗██║░░██╗██╔══██║██║╚████║"
        "╚█████╔╝███████╗██║╚█████╔╝██║░╚██╗╚█████╔╝██║░░██║╚█████╔╝██║░╚██╗██████╔╝╚█████╔╝██║░░██║██║░╚███║"
        "░╚════╝░╚══════╝╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝\n''')
    print(Fore.LIGHTGREEN_EX + "\t\t\t\t\tWelcome to Albus Security")
    print(Fore.LIGHTWHITE_EX + '\t\t\t\t\tAuthor: Aniket Tyagi\n\n')

    # Argument Controller
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-U', '--url', help='Specify a single URL')
    group.add_argument('-L', '--list', help='Specify a file containing a list of URLs')
    parser.add_argument('-T', '--timeout', help='Maximum number of seconds to wait while requesting a web page (Default: 10)', default=10, type=int)
    parser.add_argument('-O', '--output', help='Specify the output file name')

    args = parser.parse_args()

    if args.url:
        url_list = [args.url]
    elif args.list:
        if not os.path.exists(args.list):
            print("The specified path to the URL list does not exist!")
            print("Exiting...")
            sys.exit(1)

        with open(args.list, 'r') as f:
            url_list = [line.strip() for line in f]

    check(url_list)
    exploit(url_list, args.timeout, args.output)

    print(Fore.GREEN + "The list of vulnerable domains has been stored in the specified file.\n")
    print(Fore.GREEN + "Thank you! Happy hacking!")
