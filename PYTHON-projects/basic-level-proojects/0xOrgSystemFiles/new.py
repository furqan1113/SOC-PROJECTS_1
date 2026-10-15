 #file organizer tool

import argparse
import os
import sys
import shutil
import time


#1)function for args
def argParsing():
    parser = argparse.ArgumentParser(add_help="This is File organizer tool",
                                     epilog=" \n Syntax-\nCopy in cwd -> python new.py -p path/of/folder --copy \nMove in cwd -> python new.py -p path/of/folder --move ")
    parser.add_argument("-p","--path",help=" add your path of unorganized folder after -p ")
    
    parser.add_argument("-d","--destination",help="destination folder after -d ",default=os.getcwd()) #not used in this just save in cwd
    parser.add_argument("--move",action="store_true")
    parser.add_argument("--copy",action="store_true")
    parser.add_argument("--log",action="store_true")
    
    return parser.parse_args()


#2)function to check the args & paths
def file_org_file():
    args = argParsing()
    if not args.path :
        sys.exit("\nError(syntax)\nCommand syntax- \n Copy in cwd -> python new.py -p path/of/folder --copy \n Move in cwd -> python new.py -p path/of/folder --move ")
    destination=args.destination
    path22= args.path
    copy=args.copy
    move=args.move
    log=args.log
    #for checking permissions / destination folder exists or not
    if not os.listdir(path22):sys.exit("NO CONTENTS IN THE PATH FOLDER TO ORGANIZE.....CHECK again & \n try again~")
    if not os.path.exists(destination) or not os.access(destination,os.W_OK):
        sys.exit("DESTINATION PATH ISN'T THERE OR NO PERMISSION TO WRITE THERE... ")
    if os.path.exists(path22) and os.path.isdir(path22) :
        if copy and move:
            sys.exit("YOU CAN EITHER COPY OR MOVE (BOTH NOT ALLOWED AT SAME TIME)")
        if copy or move or log:
            input_user(path22,copy,move,destination,log)
        else:
            sys.exit("PATH IS NOT DIRECTORY / invalid dir ! TRY AGAIN")
    else:
        print("PATH DOESN'T EXIST ! Error \n ENTER CORRECT PATH")
        
        

#3) take input and check files
def input_user(path22,copy,move,destination,log):
    inp1 = input("Are you sure to continue? (y/n) : ").lower()
    if inp1 in ["y","yes","ye",""] : #if in them or user press enter do it!
        
        print("STARTING...")
        time.sleep(0.2)
        ext_checker(path22,copy,move,destination,log)
    elif inp1 in ["no","n","ney"]:
        print("  \n THANK YOU FOR USING 	:) \n exited...")
    else:
        print("INAVLID INPUT !!! \n Try Again ")
        
#4) extension checking & organizing to further make folders in new function 
def ext_checker(path22,copy,move,destination,log):
    print('CHECKING FILES....')
    time.sleep(0.2)
    print("DONE !")
    extension_dict = {}
    try:
        
        for fileitems in os.listdir(path22):
            path_of_file = os.path.join(path22,fileitems)
            if "." in fileitems and fileitems.count(".") ==1:
                extension_name=fileitems.split(".")[1]
                if extension_name in extension_dict:
                    extension_dict[extension_name]+=1
                else:
                    extension_dict[extension_name] =1
            else:
                if copy:
                    print(f"TWO DOTTED FILE {fileitems} not COPIED (CHECK IN ERRORLOGS.TXT for more details)")
                    error_logs_files(fileitems,"copy")
                if move:
                    print(f"TWO DOTTED FILE {fileitems} not MOVED (CHECK IN ERRORLOGS.TXT for more details)")
                    error_logs_files(fileitems,"move")
        organize_folder(extension_dict,path22,copy,move,destination,log)
    except Exception as e:print("error (faced in - mainfunciton) ->",e)
    
#this one is for the two dotted files
def error_logs_files(fileitems,action_done):
    with open("errorLogFile.txt","a") as logFile:
        logFile.write(f"\t Error in {action_done}moving  - '{fileitems}' [not 1 dotted file] \n ")
        
#5) main function to -> organize all the files into respective folders 
def organize_folder(exten_dict,path22,copy,move,destination,log):
    try:
        for ext,count in exten_dict.items():
            if count:
                folder_name = f"{ext.upper()}s"
                os.chdir(destination)
                folder_path  = os.path.join(destination,folder_name)
                print(f"{"*"*21}MAKING FOLDER{"*"*21}")
                time.sleep(1)
                print(F"\tcreated {folder_path} in {folder_path}")
                os.makedirs(folder_path,exist_ok=True)
                for eachItem in os.listdir(path22):
                    if eachItem.endswith(f".{ext}"):
                        time.sleep(0.2)
                        if copy:
                            print("COPYING...... ")
                            shutil.copy2(os.path.join(path22, eachItem), folder_path)
                            if log:
                                action_done="COPIED"
                                write_to_log_file(eachItem,action_done,folder_path)
                        if move:
                            print("MOVING...... ")
                            shutil.move(os.path.join(path22,eachItem),folder_path)
                            action_done="COPIED"
                            write_to_log_file(eachItem,action_done,folder_path)
    except KeyError:print("extension error")
    except Exception as e :print("error in organize folder function ->",e) 

#6) log-file function to what actions done in real time f
def write_to_log_file(eachItem,action_done,folder_path):
    with open("log-file.txt","a") as logFile:
        logFile.write(f"\t* {action_done} - '{eachItem}' to \t {folder_path} * \n\n")


        
#THE MAIN CALL with effective exporting 
if __name__ =="__main__":
    if file_org_file():print("FINISHED... \n check log-file.txt to see summary ")