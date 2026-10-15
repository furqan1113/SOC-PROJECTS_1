#last 7 days files/folders check


import time
import os

current_date = time.time() #in seconds
seven_days = 7*24*60*60 

folder_path = input("ENTER THE NAME OF DIRECTORY IN CWD / ENTER THE PATH - ")
try:
    for entry in os.scandir(folder_path):
        if entry.is_file():
        #print(f"File Name - {entry.stat().st_mtime}") #in seconds time of last modified date
            modified_time = entry.stat().st_mtime
            if current_date - modified_time < seven_days: # this is just files modified in less than 7 days
                print(f"FileName {entry.name} \n",time.ctime(modified_time))
        
        if entry.is_dir():
            modified_time=entry.stat().st_mtime 
            if current_date - modified_time < seven_days :
                print(f"DIRECTORY {entry.name} \n {time.ctime(modified_time)} ")
except FileNotFoundError:print("FOLDER NOT FOUND")
except PermissionError:print("PERMISSSION ERROR ")
except Exception as fe:print("ERROR - ",fe)