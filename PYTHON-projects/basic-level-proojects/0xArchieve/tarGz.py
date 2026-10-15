
import os
import tarfile
from colorama import Style,Fore,init
init(autoreset=True)
#tar function
excluded=[".log",".tmp"]
def tarGzArchive(f_path,name_to_keep,excluded,verbose):
    try:
        with tarfile.open(name_to_keep,"w:gz") as tar:
            for root,dir,files in os.walk(f_path):
                for eachFile in files:
                    full_path = os.path.join(root,eachFile)
                    if excluded:
                        if any(eachFile.endswith(eachExt) for eachExt in excluded):
                            if verbose:
                                print(Fore.RED + "[SKIPPED] -  ",eachFile)
                            continue
                    rel_path_of_files = os.path.relpath(full_path,f_path) #full path -> abs path , #f_path -> working dir/base of the files = > rel path
                    try:
                        if verbose:
                            print(Fore.YELLOW + f"[ARCHIVING....] - {eachFile}")
                            tar.add(full_path,rel_path_of_files) #eachfle #with name as its relative path
                            print(Fore.GREEN + f"[ARCHIVED] - {eachFile}")
                        else:
                            tar.add(full_path,rel_path_of_files) #FULL_FILE_PATH #rename  as its relative path
                    except PermissionError :
                        print(Fore.RED + "\t[NO PERMISSIONS]  - ",eachFile)
                    except Exception as fe :print(Fore.RED + "ERROR - ",fe)
    except FileNotFoundError:print("FILE/FOLDER NOT FOUND...")
    except PermissionError:print("NO PERMISSION FOR READING - ",f_path)

folder_path = os.path.join(os.getcwd(),"Folder1")
