# Calculate Unique IPs and DoS Check

import os
import argparse
import sys

# Step 1: Argument parser for accepting log file path
def argumentAcc():
    parser = argparse.ArgumentParser(description="Log Analyzer: Count Unique IPs and Detect DoS attempts.")
    parser.add_argument("-f", "--file", help="Enter log file-name or path to log file")
    return parser.parse_args()

# Step 2: Entry point
def main():
    args = argumentAcc()
    if not args.file:
        sys.exit("ERROR: No file argument provided.")
    
    filename = args.file
    if os.path.exists(filename) and os.path.isfile(filename):
        logAnalyzer(filename)
    else:
        print(f"ERROR: File '{filename}' does not exist or permission denied.")

# Step 3: Log analyzer logic
def logAnalyzer(filename):
    try:
        with open(filename, "r") as logsFile:
            content = logsFile.readlines()
            if not content:
                sys.exit("ERROR: Log file is empty.")

            ip_list = [eachLine.split()[0] for eachLine in content if eachLine.strip()]
            if ip_list:
                ipsCalculator(ip_list)

    except Exception as fe:
        print(f"ERROR: {fe}")

# Step 4: Calculate IPs and detect potential DoS
def ipsCalculator(ip_list):
    safe_range = 5
    dict_cal = {}

    for ip in ip_list:
        if ip in dict_cal:
            dict_cal[ip] += 1
        else:
            dict_cal[ip] = 1

    print(f"\nTotal Unique IPs: {len(dict_cal)}\n")

    for ip, count in dict_cal.items():
        print(f"IP: {ip} — Requests: {count}")
        if count > safe_range:
            print("-" * 10)
            print(f"⚠️  WARNING: {ip} may be performing a DoS attack!")
            print("-" * 10)

# Run the script & make it reusable
if __name__ == "__main__":
    main()
