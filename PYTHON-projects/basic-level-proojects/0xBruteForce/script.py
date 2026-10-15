#BRUTE-FORCE ATTEMPT where each-Username is tested with 1000 passwords from password-list field

#1) importing modules
import os
import argparse
import sys
import time
#2) make an argument accepting function accepting -> username file and password-file

def argumentAccepter():
    parser=argparse.ArgumentParser(description="THIS IS A BRUTE FORCE SIMULATED SCRIPT",epilog="syntax\n python3 script.py -u usernameFile.txt -p passwordFile.txt")
    parser.add_argument("-u","--usernameF",help="ENTER USERNAME FILE ",required=True)
    parser.add_argument("-p","--passwordF",help="ENTER Password FILE ",required=True)
    parser.add_argument("-d","--delay",help="Enter DELAY OF Time b/w each-pattern")
    return parser.parse_args()


def main():
    args = argumentAccepter()
    
    if not args.usernameF or not args.passwordF:
        sys.exit("NO USERNAME FILE OR PASSWORD FILE PROVIDED")
    else:
        usernames,passwords = args.usernameF,args.passwordF 
        if os.path.exists(usernames) and os.path.exists(passwords):
            try:
                with open(usernames,"r") as u_file:
                    has_content_u=False   
                    for eachusername in u_file:
                        has_content_u = True
                        with open(passwords,"r") as p_file: # for each username file is openng again instead of file.seek(0)
                            for eachPwd in p_file:
                                if not args.delay:print(f"TRYING [{eachusername.strip()}] - [{eachPwd.strip()}]")
                                else:
                                    try:
                                        time_bw = int(args.delay)
                                        print(f"TRYING [{eachusername.strip()}] - [{eachPwd.strip()}]")
                                        time.sleep(time_bw)
                                    except ValueError:sys.exit("ENTER TIME VAlue errror")
                    if not has_content_u:sys.exit("NO CONTENT in Username file")
            except PermissionError:print("PERMISSION ERROR TO READ PWD AND USERNAME FILES")
            except Exception as fe:print("ERROR - ",fe)
        else:sys.exit("EITHER PASSWORD OR USERNAME FILE DOESN'T EXIST.")

if __name__ == "__main__":
    main()