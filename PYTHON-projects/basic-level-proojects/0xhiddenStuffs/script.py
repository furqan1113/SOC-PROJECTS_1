# hidden files finder for linux with all files saving in a file
import argparse
import os
import sys
def argsAccepter():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p","--path",help="Enter path ")
    parser.add_argument("--recursive",action="store_true",help="Recursively-Check")
    parser.add_argument("--output",action="store_true",help="save to output file")
    return parser.parse_args()

def main():
    args = argsAccepter()
    
    if not args.path:
        sys.exit("NO PATH SPECIFIED..")
    if args.path:
        path=args.path
        if os.path.exists(path) and os.access(path,os.R_OK): #if path exist and
            if not args.recursive:
                findFilesinCwd(path,args)
            elif args.recursive:
                findRecurisve(path,args)
def findFilesinCwd(path,args):
    try:
        file_exists = False
        for eachFile in os.listdir(path): #goes only if file exists there...
            file_exists=True
            if "." ==eachFile[0]:
                print("FOUND - ",eachFile) #just for debugging
                if args.output:
                    save_to_file(eachFile,os.path.abspath(path))
        if not file_exists:print("NO FILES FOUND IN CWD ")
            
    except FileNotFoundError:print("file not found error")  
    except PermissionError:print("error permission")
    except Exception as fe:print("FILE ERROR - ",fe)
    
    
#recursive    
def findRecurisve(path,args):
    try:
        file_exists = False
        for root,dir,files in os.walk(path):
            file_exists=True
            for file in files:
                new_path = os.path.join(root,file)
                if file[0] == ".":
                    print(f"FOUND - {file} FullPath -{os.path.abspath(new_path)}") #Just for debugging
                    if args.output:save_to_file(file,new_path)
        if not file_exists:print("NO FILES FOUND IN -  ",root)
    except FileNotFoundError:print("file not found error")  
    except PermissionError:print("error permission")
    except Exception as fe:print("FILE ERROR - ",fe)
   

def save_to_file(file,path):
    try:
        with open("h_files.txt","a") as f:
            f.write(f"FOUND - {file}    FULLPATH - [{os.path.abspath(path)}]\n")
    except PermissionError:print("COULDN'T MAKE FILE DUE TO - NO PERMISSION ")
    except FileExistsError:print("FILE NAME EXISTS ")
    except Exception as fe:print("error in creating FILE - ",fe)
    
    
if __name__=="__main__":
    main()