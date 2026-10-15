#Email Validator
import argparse
import os
import sys

#arg parsing

def argumentAccepter():
    parser = argparse.ArgumentParser(
        description= """
        Email validator Tool V2""",
        epilog="Made By Furqan",
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-s","--single",metavar="singleEmail",help="ENTER SINGLE EMAIL TO CHECK ")
    parser.add_argument("-f","--file",metavar="emailFile",help="ENTER FILE CONTAINING EMAILS")
    parser.add_argument("-d","--saveTo",help="GIVE FILE NAME WHERE CORRECT EMAILS WILL BE STORED")
    parser.add_argument("--verbose",action="store_true",help="MORE DETAILED ON TERMINAL")
    return parser.parse_args()

def argsValidator():
    args = argumentAccepter()
    #args validations
    
    if not args.single and not  args.file:
        sys.exit("NO EMAIL / FILE CONTAINING EMAILS GIVEN \n USE --help for correct usage ")
    #single-email
    if args.single:
        SingleEmail = args.single.strip()
        isValid = emailValidator(SingleEmail)
        print(f"{'EMAIL IS VALID' if isValid else 'EMAIL IS INVALID'} - ",SingleEmail)
    #files-emails
    if args.file:
        file1 = args.file
        destFile = args.saveTo
        if os.path.exists(file1) and os.path.isfile(file1):
            parseEmails(file1,args.verbose,destFile)
        else:print("NO FILE EXISTS ")  

def parseEmails(file1,verbose, destFile=None):
    try:
        with open(file1,"r") as f1:
            allContent = f1.readlines()
            if not allContent:
                print(f"{file1} FILE IS EMPTY ")
            else:
                for eachLines in allContent:
                    eachEmail = eachLines.strip()
                    isValid = emailValidator(eachEmail)
                    if isValid and verbose:print("EMAIL IS VALID - ",eachEmail)
                    elif not isValid and verbose:print("INVALID - ",eachEmail)
                    if isValid and destFile:
                        newEmailSaver(eachEmail,destFile)
    except PermissionError:print("PERMISSION ERROR ")
    except Exception as fe :print("ERROR - ",fe)

def newEmailSaver(eachEmail,filename):
    i = 0
    with open(filename,"a") as f1:
        if i == 0:f1.write("VALID EMAILS \n")
        else : f1.write(f"{eachEmail} \n")


def emailValidator(eachEmail):
    if " " in eachEmail:
        return False
    if eachEmail.count("@") != 1:
        return False
    if any(c in eachEmail for c in '/!#$%^&*()-+=[]{ }|~`"'):
        return False
    name, domain = eachEmail.split("@")
    if name.startswith(".") or name.endswith("."):
        return False
    if domain.startswith(".") or domain.endswith("."):
        return False
    if "." not in domain:
        return False

    tld = domain.rsplit(".", 1)[-1]
    
    
    common_tlds = {
        "com", "net", "org", "info", "biz", "name", "pro", "xyz", "online", "site",
        "store", "tech", "io", "dev", "app", "in", "us", "uk", "ca", "au", "ru", "de",
        "fr", "cn", "jp", "br", "sa", "edu", "gov", "mil", "int", "aero", "museum",
        "jobs", "travel", "arpa", "blog", "pizza", "art", "design", "photography",
        "news", "finance", "health", "doctor", "law", "games", "music"
    }
    return tld in common_tlds # true / false hogaa as in will see hai kya ? and returns false / true


if __name__ == "__main__":
    argsValidator()