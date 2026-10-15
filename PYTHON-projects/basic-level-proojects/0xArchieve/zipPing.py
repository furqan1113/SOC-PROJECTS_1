#put all files and folders from a file into a zip file FILTERING:-
#1) exclude files with extension user gives
#2) exclude not permitted but print there names
#3) name -> relative paths for the files

import os
from zipfile import ZipFile
from colorama import Style,Fore,init
init(autoreset=True)
#zip function
excluded=[".log",".tmp"]
def zipArchive(f_path,name_to_keep,excluded,verbose):
    try:
        with ZipFile(name_to_keep,"w") as zipf:
            for root,dir,files in os.walk(f_path):
                for eachFile in files:
                    full_path = os.path.join(root,eachFile)
                    if any(eachFile.endswith(eachExt) for eachExt in excluded):
                        if verbose:
                            print(Fore.RED + "[SKIPPED] -  ",eachFile)
                        continue
                    #for windows we gonna use try except for PERMISSIONS
                    rel_path_of_files = os.path.relpath(full_path,f_path) #full path -> abs path , #f_path -> working dir/base of the files = > rel path
                    try:
                        if verbose:
                            print(Fore.YELLOW + f"[ARCHIVING....] - {eachFile}")
                            zipf.write(full_path,rel_path_of_files) #eachfle #with name as its relative path
                            print(Fore.GREEN + f"[ARCHIVED] - {eachFile}")
                        else:
                            zipf.write(full_path,rel_path_of_files) #eachfle #with name as its relative path
                    except PermissionError :
                        print(Fore.RED + "\t[NO PERMISSIONS]  - ",eachFile)
                    except Exception as fe :print(Fore.RED + "ERROR - ",fe)
    except FileNotFoundError:print("FILE/FOLDER NOT FOUND...")
    except PermissionError:print("NO PERMISSION FOR READING - ",f_path)

folder_path = os.path.join(os.getcwd(),"Folder1")
