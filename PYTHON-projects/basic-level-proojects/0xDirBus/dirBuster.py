import requests
import argparse
import sys
import os
from colorama import Fore, init
init(autoreset=True)
def argumentsParsing():
    parser = argparse.ArgumentParser(
        description="DIRECOTRY ENUMERATOR (safe use only!)",epilog="usecase eg - >  dirBuster.py -u url.com ")
    parser.add_argument("-u","--url",help="Enter the url after -u ")
    parser.add_argument("-v","--verbose",action="store_true")
    parser.add_argument("-o","--output",help="output file where to save the outputs -o ")
    parser.add_argument("-w", "--wordlist", default="dirFile.txt", help="Wordlist file for directory enumeration")
    #now return the args with values of users
    return parser.parse_args()
def main():
    args = argumentsParsing()
    if not args.url:
        sys.exit(f"{Fore.RED}[ERROR] Please provide a URL with -u")
    if args.verbose:
        print(f"{Fore.BLUE}[INFO] VERBOSE MODE ON...")
    url = args.url
    output_file = args.output or "output.txt"
    if not args.wordlist:
        print(f'{Fore.YELLOW}[WARN] No wordlist file provided, using default: dirFile.txt')
        dirEnumerator(url, "dirFile.txt", output_file)
    else:
        if os.path.exists(args.wordlist) and os.path.getsize(args.wordlist) != 0:
            wordlist_file = args.wordlist
            print(f"{Fore.GREEN}[OK] Using your wordlist file: {wordlist_file}")
            dirEnumerator(url, wordlist_file, output_file)
        else:
            print(f"{Fore.RED}[ERROR] Path doesn't exist or file is empty.")

def dirEnumerator(url, filename, output_file):
    try:
        with open(filename, "r", encoding="utf-8") as dirFile:
            with open(output_file, "w", encoding="utf-8") as newFile:
                tabs = "\t" * 10
                newFile.write(f"{tabs}WORKING LINKS / DIRECTORIES\n")
            for eachLine in dirFile:
                eachLine = eachLine.strip()
                if eachLine and eachLine[0] == "/":
                    full_url = url.rstrip("/") + "/" + eachLine.lstrip("/") #strips right and left side /
                    try:
                        response = requests.get(full_url)
                        if response.status_code == 200:
                            print(f"{Fore.GREEN}[FOUND] {eachLine} [200]")
                            save_to_file(output_file, full_url)
                        elif response.status_code in [301, 302]:
                            print(f"{Fore.YELLOW}[REDIRECTED] {eachLine} [{response.status_code}]")
                        else:
                            print(f"{Fore.RED}[NOT FOUND] {eachLine} [{response.status_code}]")
                    except requests.RequestException as e:
                        print(f"{Fore.RED}[ERROR] {e}")
    except PermissionError:
        print(f"{Fore.RED}[ERROR] Permission denied to read wordlist file.")
    except Exception as e:
        print(f"{Fore.RED}[ERROR] {e}")

def save_to_file(output_file, full_url):
    try:
        with open(output_file, "a") as newFile:
            newFile.write(f"{full_url}\n")
    except ValueError:
        print(f'{Fore.RED}[ERROR] Please enter a valid output file name.')
    except Exception as e:
        print(f'{Fore.RED}[ERROR] {e}')
if __name__ == "__main__":
    main()
    print("DONE !!")