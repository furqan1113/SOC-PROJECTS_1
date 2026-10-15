#SYSTEM INFO VIEWER TOOL for all os's
import argparse
import platform
import sys
import os
def argParser():
    parser = argparse.ArgumentParser(description="SYSTEM INFO TOOL",epilog="syntax - ")
    parser.add_argument("--log",action="store_true",help="-hf -> hidden files")
    args = parser.parse_args()
    return args
def reconSystem():
    args = argParser()
    
    try:
        info = [
    f"System: {platform.system()}",
    f"Computer/Node Name: {platform.node()}",
    f"Release: {platform.release()}",
    f"Version: {platform.version()}",
    f"Machine: {platform.machine()}",
    f"Processor: {platform.processor()}",
    f"Architecture: {platform.architecture()[0]}",
    f"username: {os.getenv('username')or os.getenv('USER')}",
]
        permission_hai = True
    except PermissionError:print("PERMISSION ERROR")  
    if permission_hai : 
        lines = "-"*33
        print(lines)
        for line in info:
            print(f"{line}")
        print("-"*31)
        if args.log:
            try:
                with open("recon.txt","w") as file:
                    file.write(f"{lines}\n")
                    for line in info:file.write(f"{line}\n")
                    file.write(f"{lines}\n")
                    
                print("SAVED INFORMATION TO recon.txt")
            
            except PermissionError:print("PERMISSION ERROR")


if __name__=="__main__":
    reconSystem()