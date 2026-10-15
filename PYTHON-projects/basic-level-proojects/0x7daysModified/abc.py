import time
import os

def modifierChecker(folder_name):
    current_time = time.time() #in seconds 
    seven_days_in_sec = 7*24*60*60
    if os.path.exists(folder_name) and os.path.isdir(folder_name):
        for content in os.scandir(folder_name):
            last_modified = content.stat().st_mtime # modified contends in seconds 
            if current_time - last_modified < seven_days_in_sec: #compare with above 7 days not direct 7 as it is taken as 7 sec
                
                print(f"{content.name} - MODIFIED LAST ON {time.ctime(last_modified)}") #changes modified time in seconds to - readabel time


if __name__ == "__main__":
    path = input("ENTER THE PATH - ")
    modifierChecker("C:\\Users\\furqa\\Desktop\\DESKTOP STUFF\\x0projects\\0xSystemOrgProjects\\0x7daysModified")