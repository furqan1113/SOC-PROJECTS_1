import argparse
import os
import sys

def argumentAccepter():
    parser = argparse.ArgumentParser(description="EMAIL VALIDATOR TOOL")
    parser.add_argument("-f", "--file", help="File with emails to check")
    parser.add_argument("-e", "--email", help="Single email to check")
    parser.add_argument("-s", "--saveto", help="Filename to save valid emails")
    return parser.parse_args()

def main():
    args = argumentAccepter()
    
    if not args.file or  not args.email:
        sys.exit("❌ No arguments entered. Please provide -f or -e.")
    
    if args.file:
        if os.path.exists(args.file) and os.path.isfile(args.file):
            parseFile(args.file, args.saveto)
        else:
            sys.exit("❌ Invalid file path.")
    
    if args.email:
        email = args.email.strip()
        isValid = emailChecker(email)
        print(f"{'VALID ✅' if isValid else 'INVALID ❌'} - {email}")

def parseFile(filename, savetoFile=None):
    try:
        with open(filename, "r") as emFile:
            lines = emFile.readlines() #reads whole content line by line and save in array
            if not lines:
                print("📭 File is empty.")
                return
            
            for eachLine in lines: #loop through that array
                eachEmail = eachLine.strip()
                if not eachEmail:
                    continue

                isValid = emailChecker(eachEmail)
                print(f"{'VALID ✅' if isValid else 'INVALID ❌'} - {eachEmail}")
                
                if isValid and savetoFile:
                    create_save_to_file(savetoFile, eachEmail)
                    
    except PermissionError:
        print("🚫 Permission denied for file:", filename)
    except Exception as e:
        print("⚠️ Error:", e)

def emailChecker(email):
    if "@" not in email or email.count("@") != 1 or email.count(".") != 1:
        return False
    if any(c in email for c in '/!#$%^&*()-+=[]{}|~`"'):
        return False
    if " " in email:
        return False

    name, domain = email.split("@")
    if not name or not domain:
        return False
    if ".." in name or ".." in domain:
        return False
    if name.startswith(".") or name.endswith("."):
        return False
    if domain.startswith(".") or domain.endswith("."):
        return False
    if domain.count(".") != 1:
        return False

    tld = domain.split(".")[1]
    common_tlds = {
        "com", "net", "org", "info", "biz", "name", "pro", "xyz", "online", "site",
        "store", "tech", "io", "dev", "app", "in", "us", "uk", "ca", "au", "ru", "de",
        "fr", "cn", "jp", "br", "sa", "edu", "gov", "mil", "int", "aero", "museum",
        "jobs", "travel", "arpa", "blog", "pizza", "art", "design", "photography",
        "news", "finance", "health", "doctor", "law", "games", "music"
    }
    return tld in common_tlds #true/false
def create_save_to_file(filename, email):
    try:
        with open(filename, "a") as file:
            file.write(f"{email}\n")
    except PermissionError:
        print("🚫 Permission denied for saving file.")
    except Exception as e:
        print("⚠️ Error:", e)

if __name__ == "__main__":
    main()
