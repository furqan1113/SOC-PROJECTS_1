import argparse
import os
import sys
import time
import requests
#step 1) parse the arguments

def argAccepter():
    parser = argparse.ArgumentParser(description="DIRECTORY ENUMERATOR",epilog="MADE BY @FURQAN")
    parser.add_argument("-u","--url",help="ENTER THE URL",metavar="URL",required=True)
    parser.add_argument("-w","--wordlist",help="ENTER THE WORDLIST OR DEFAULT IS wordlist.txt")
    parser.add_argument("--verbose",help="MORE DETAILED",action="store_true")
    return parser.parse_args()


#step 2) logic of arguments

def argValidtor():
    args  = argAccepter()
    verbose = args.verbose
    url = args.url
    #conditions
    wl=args.wordlist if args.wordlist else "dirFile.txt"
    if os.path.exists(wl) and os.path.isfile(wl):
        print(f"USING {wl}....")
        time.sleep(1)
        dirEnumerator(url,verbose,wl)
            
    else :
        sys.exit("THE WORDLIST FILE DOESN'T EXIST")
    

#MAIN TOOL - DIRECTORY ENUMERATOR

def dirEnumerator(url,verbose,wl):
    try:
        with open(wl,"r",encoding="utf-8") as f1:
            full_content = f1.readlines() 
            if full_content :
                for eachWord in full_content:
                    eachWord = eachWord.strip()
                    full_url = url.rstrip("/") + "/" + eachWord.lstrip("/")
                    if verbose:print('TRYING - ',full_url)
                    start_tool(full_url,verbose)
    except PermissionError:print("PERMISSIONE ERROR")
    except Exception as fe :print('WORD LIST FILE ERROR - ',fe)           
                    
#Requesting 

def start_tool(full_url,verbose):
    try:
        response = requests.get(full_url,timeout=4)
        if response.status_code == 200 :
            if verbose:
                print("DIR FOUND [200] - ", full_url)
                save_to_file(full_url)
            else:
                print(f"FOUND saving....")
                save_to_file(full_url)
        elif response.status_code in [301, 302]:
            if verbose:print(f"DIR REDIRECTION [{response.status_code}] - ", full_url)
        else:
            print(f"NOT FOUND -  [{response.status_code}]")
    except requests.RequestException as e :
        print("REQUEST ERROR	 - ",e)
        
def save_to_file( full_url):
    try:
        with open("results_dirEnum", "a") as newFile:
            newFile.write(f"{full_url}\n")
    except ValueError:
        print(f'[ERROR] Please enter a valid output file name.')
    except Exception as e:
        print(f'[ERROR] {e}')
        
if __name__ == "__main__":
    argValidtor()