#!/usr/bin/env python3
import subprocess
from colorama import Fore, Style, init
init(autoreset=True)
import platform
import time
from datetime import datetime

# ===========================
# 🛡️  PING + NMAP RECON TOOL
# ===========================

def pingingTool(ip_list, verbose):
    hosts_up = 0
    if ip_list:
        ping_flag = "-c" if platform.system().lower() != "windows" else "-n"

        for each_ip in ip_list:
            try:
                if verbose:
                    print(Fore.YELLOW + f"\n[🔍] Pinging {each_ip}...")

                result = subprocess.run(["ping", ping_flag, "2", each_ip], capture_output=True, text=True, timeout=4)

                if result.returncode == 0 and ("received" in result.stdout.lower() or "reply from" in result.stdout.lower()):
                    print(Fore.GREEN + f"{each_ip} is UP ✔️")
                    hosts_up += 1

                    print(Fore.CYAN + f"\n[SUMMARY] {hosts_up}/{len(ip_list)} hosts are up.")

                    if verbose:
                        print(Fore.YELLOW + f"[⚙️ ] Launching Nmap on {each_ip}...")

                    NmapTool(each_ip, verbose)

                else:
                    print(Fore.RED + f"{each_ip} is DOWN ❌ or INVALID.")

            except FileNotFoundError:
                print(Fore.RED + "[❌] PING not found! Is it installed and in PATH?")
            except subprocess.TimeoutExpired:
                print(Fore.RED + f"[⏰] Timeout! {each_ip} didn’t respond.")


def NmapTool(each_ip, verbose):
    try:
        time.sleep(0.5)
        result = subprocess.run(["nmap", "-sS", each_ip], capture_output=True, text=True, timeout=20)

        if result.returncode == 0:
            open_ports = checkPortsOpen(each_ip, result.stdout)

            if open_ports:
                print(Fore.WHITE + f"\n[✅] Open ports found for {each_ip}")
                saved = save_to_file(each_ip, result.stdout)
                if saved and verbose:
                    print(Fore.GREEN + "[💾] Results saved to file")
            else:
                print(Fore.RED + f"[❌] No open ports found for {each_ip}")
        else:
            print(Fore.RED + f"[⚠️] Nmap scan failed on {each_ip}")

    except FileNotFoundError:
        print(Fore.RED + "[❌] NMAP not installed or not in PATH!")
    except subprocess.TimeoutExpired:
        print(Fore.RED + f"[⏰] Timeout! Scan incomplete for {each_ip}")


def checkPortsOpen(each_ip, result):
    lines = result.splitlines()
    found_any = False

    for line in lines:
        parts = line.strip().split()
        if len(parts) >= 3 and "/" in parts[0] and parts[1] in ["open", "closed", "filtered"]:
            port_str, state, service = parts[0], parts[1], parts[2]
            port_no = int(port_str.split("/")[0])
            proto = port_str.split("/")[1].upper()

            print(Fore.YELLOW + f"{proto} PORT {port_no} is {state} - SERVICE: {service}")

            if state == "open" and port_no in [80, 443]:
                runWhois(each_ip)

            found_any = True

    return found_any


def save_to_file(each_ip, output):
    try:
        filename = f"cmd_{each_ip}.log"
        with open(filename, "a") as f:
            f.write(f"\n{'='*50}\n[SCAN RESULT] {each_ip}\n{'-'*50}\n")
            f.write(output + "\n")
        return True
    except Exception as e:
        print(Fore.RED + f"[ERROR] Could not save output: {e}")
        return False


def runWhois(domain):
    try:
        result = subprocess.run(["whois", domain], capture_output=True, text=True, timeout=10)

        if result.returncode == 0:
            fields = ["domain name", "registrar", "creation date", "expiry date", "expiration date", "name server", "updated date"]
            found_fields = {}

            for line in result.stdout.splitlines():
                line_lower = line.lower()
                for field in fields:
                    if field in line_lower and field not in found_fields:
                        found_fields[field] = line.strip()

            if found_fields:
                print(Fore.BLUE + f"\n[WHOIS INFO] for {domain}")
                for key in fields:
                    if key in found_fields:
                        print(found_fields[key])
            else:
                print(Fore.RED + f"[WHOIS] No relevant fields found for {domain}.")

        else:
            print(Fore.RED + f"[WHOIS] Lookup failed for {domain}.")

    except FileNotFoundError:
        print(Fore.RED + "[❌] WHOIS not installed or missing from PATH")
    except subprocess.TimeoutExpired:
        print(Fore.RED + f"[⏰] WHOIS timed out for {domain}")