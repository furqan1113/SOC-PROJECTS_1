#!/usr/bin/env python3
import argparse
import sys
import os
from colorama import Fore, Style, init
from main1 import pingingTool

init(autoreset=True)

def reconArgCollector():
    parser = argparse.ArgumentParser(
        description="""
🛡️ RECON TOOL - v0.1 
---------------------
Ping + Nmap Scanner + Banner Grabber(in future)

Examples:
  python3 recon.py -i 192.168.1.1 -t single --verbose
  python3 recon.py -l targets.txt -t lines
  python3 recon.py -l domains.csv -t csv --verbose
""",
        formatter_class=argparse.RawTextHelpFormatter
    )

    # Input source
    input_group = parser.add_argument_group("Target Input")
    input_group.add_argument("-i", "--ip", type=str, metavar="TARGET IP", help="🎯 Single IP or domain to scan")
    input_group.add_argument("-l", "--iplist", type=str, metavar="Target IPs FILE", help="📂 File containing IPs/domains list")

    # File format
    parser.add_argument(
        "-t", "--filetype", type=str, required=True, metavar="", choices=["single", "lines", "csv"],
        help="📄 File format: single / lines / csv"
    )

    # Flags
    parser.add_argument("--verbose", action="store_true", help="🗣️  Enable verbose mode for detailed output")

    return parser.parse_args()

def parsingArgs():
    args = reconArgCollector()

    if not args.ip and not args.iplist:
        sys.exit(Fore.RED + "[❌] Please provide a target IP (-i) or a file list (-l)")

    ip = args.ip
    filename = args.iplist
    filetype = args.filetype
    verbose = args.verbose

    if filename:
        try:
            if os.path.exists(filename) and os.path.isfile(filename) and os.path.getsize(filename) != 0:
                with open(filename, "r") as ip_file:
                    if filetype == "csv":
                        domain_list = ip_file.read().strip().split(',')
                    elif filetype == "lines":
                        domain_list = ip_file.read().strip().splitlines()
                    else:
                        sys.exit(Fore.RED + "[⚠️] Unsupported file type provided!")
                    
                    pingingTool(domain_list, verbose)
            else:
                print(Fore.RED + "[❌] File is empty or does not exist!")
        except PermissionError:
            print(Fore.RED + f"[🚫] Permission denied: {filename}")
        except Exception as fe:
            print(Fore.RED + f"[💥] Error reading file: {fe}")

    elif ip and filetype == "single":
        pingingTool([ip], verbose)
    else:
        print(Fore.RED + "[❌] Invalid input. Please specify a valid target.")

if __name__ == "__main__":
    print("=" * 60)
    print(Fore.RED + " RECON TOOL - PING + NMAP SCANNER |", Style.RESET_ALL, Fore.BLUE + " v0.1 ")
    print("=" * 60)
    parsingArgs()
