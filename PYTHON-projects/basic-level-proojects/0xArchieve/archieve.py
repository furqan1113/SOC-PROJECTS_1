#MENU AND VALIDATIONS FOR THE USE OF 1) ZIP OR 2) TAR.GZ
from zipPing import zipArchive
from tarGz import tarGzArchive
import os
import argparse
import sys
from colorama import Fore,Style,init
init(autoreset=True)

def argParsing():
    parser = argparse.ArgumentParser(description="ARCHIEVING TOOL..")
    parser.add_argument("-p","--path",help="ENTER THE FOLDER PATH",required=True)
    parser.add_argument("--exclude",nargs="+",help="OPTIONAL  ENTER EXTENSIONS TO SKIP..")
    parser.add_argument("--name",help="NAME TO KEEP of .zip/.tar.gz file",required=True)
    parser.add_argument("--method",
                        help="choose method 1).zip(EASY) 2).tar.gz(BEST for TECHiis)",required=True)
    parser.add_argument("--verbose",help="VERBOSE MODE",action="store_true")
    return parser.parse_args()

def main():
    args = argParsing()
    path_folder = args.path
    ext_exclude_list = args.exclude if args.exclude else []
    new_zip_name = args.name
    method = args.method.lower()
    verbose = args.verbose
    try:
        if os.path.exists(path_folder) and os.path.isdir(path_folder):
            if (method in ["tar.gz", ".tar.gz", "tar"] and new_zip_name.endswith(".tar.gz")):
                tarGzArchive(path_folder, new_zip_name, ext_exclude_list, verbose)
                print("DONE...!")
            elif (method in ["zip", ".zip"] and new_zip_name.endswith(".zip")):
                zipArchive(path_folder, new_zip_name, ext_exclude_list, verbose)
                print("DONE...!")
            else:
                sys.exit(Fore.RED + "BAD ARCHIEVE PATH...ENTER .zip or .tar.gz at end of paths...")
    except PermissionError:
        print(Fore.RED + "FOLDER DOESNT HAVE ENOUGH PERMISSIONS")
    except Exception as folErr:
        print(Fore.RED + "FOLDER ERROR - ", folErr)
main()

