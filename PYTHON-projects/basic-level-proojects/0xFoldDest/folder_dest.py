#folder / file destroyer with --force flag

import argparse
import os
import shutil
import sys
import time
from colorama import Fore,init,Style
init(autoreset=True)
def argParsingFunc():
    parser = argparse.ArgumentParser(description="FOLDER DESTROYER",epilog="syntax - folder_dest.py -p path")
    parser.add_argument("--overwrite",action="store_true",help="Overwrites every File - Danger!")
    parser.add_argument("--force",action="store_true",help="deletes forcefully everything Danger!")
    parser.add_argument("-p","--path",help="PATH OF THE FOLDER ",required=True)
    return parser.parse_args()

def main():
    args = argParsingFunc()
    path=args.path
    if not args.path:
        sys.exit(Fore.RED + "path not specified Error !")
    if not os.path.exists(path):
        sys.exit(Fore.RED +"Folder/Path DOENS'T EXIST")
    if not os.path.isdir(path):
        sys.exit(Fore.RED + "PATH IS A FILE not dir...")
    if args.path and os.path.isdir(path) :
        isForce=False
        isoverwriten = False
        if args.force:
            isForce = True
        if args.overwrite:
            isoverwriten=True
        folderEmpytDelete(path,isForce,isoverwriten)
        
        
def folderEmpytDelete(path,forceDel,overwrite_flag):
        try:
            if forceDel:
                if overwrite_flag:
                    while True:
                        input1 = input(Fore.RED +"ARE YOU USING AT YOUR OWN RESPOSNSIBILITY... - ").lower()
                        if input1 in ["yes", "y", "ye"]:
                            isOverwritted = True
                            for root, dirs, files in os.walk(path):
                                for eachFile in files:
                                    new_path = os.path.join(root, eachFile)
                                    overwrite(new_path, eachFile)
                            break
                        elif input1 in ["no", "n", ""]:
                            print(Fore.GREEN +"STOPPED THE OVERWRITING FUNCTION!")
                            break
                        else:
                            print(Fore.RED +"INVALID INPUT...")
                while True:
                    confirmInput = input("Are you sure you want to delete?  y/n - ").lower()
                    if confirmInput in ["y", "ye", "yes"]:
                        print(Fore.GREEN +"DELETING.....")
                        time.sleep(0.5)
                        shutil.rmtree(path)  # all
                        if isOverwritted:
                            print(Fore.CYAN + "1)changed content \n2)deleted the folder !! (hope used in your own env) .....")
                        break
                    elif confirmInput in ["n", "no", ""]:
                        print(Fore.RED + "STOPPED THE PROCESS....! \n Bye")
                        break
                    else:
                        print(Fore.RED + "INVALID INPUT! TRY AGAIN")
            else:
                print("DELETING THE EMPTY DIRECTORY....")
                time.sleep(0.5)
                os.rmdir(path)  # only for blank ones
        except PermissionError:
            print(Fore.RED +"PERMISSION NOT ALLOWED!")
        except FileNotFoundError:
            print("file not found...")
        except Exception as fe:
            print(Fore.RED + "ERROR - ", fe)
        
        
def overwrite(file_path,eachFile):
    try:
        with open(file_path,"wb") as file:
            file.write(os.urandom(1022333)) #customize it 
    except PermissionError:print(Fore.RED + "NO PERMISSION FOR THIS FILE ",eachFile)
    except FileNotFoundError :print(Fore.RED + "file not found...")
    except Exception as fe:print("ERROR -",fe)

if __name__=="__main__":
    main()