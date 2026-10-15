import argparse
import time #for cool animation


# Function to handle argument parsing
def parseArgs():
    parser = argparse.ArgumentParser(
            description="Password Validator Tool",
            epilog="Example: python tool.py -p My$ecur3P@ss -v")  # Start the parser & description for -help
    
    
    # Define the arguments
    parser.add_argument("-p", "--password", help="Enter the Password to check after -p")
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose mode")
        # Parse and return the arguments
    return parser.parse_args()

def main():
    try:
            # Get the parsed arguments
        args = parseArgs() #this calls the above function to take inputs and args in a dict
        

        # Handle verbose mode
        if args.verbose:
            print("PRINT VERBOSE MODE ENABLED")

        # Check if password is provided , if not raise error
        if not args.password:
            raise ValueError("Password is required. Use -p or --password to provide a password.")

        # Validate the password
        user_password = args.password
        passwordChecker(user_password)

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def passwordChecker(user_password):
    # Define the validation
    print('CHECKING....',user_password)
    time.sleep(1)
    if (
        len(user_password) > 8
        and any(eachSymbol in user_password for eachSymbol in "~!@#$&*()-=_+:;")  # At least one special character
        and user_password.lower() != user_password  # At least one uppercase letter
        and user_password.upper() != user_password  # At least one lowercase letter
        and any(eachChar.isalpha() for eachChar in user_password)  # At least one alphabetic character / not required can cancel/delte
        and any(eachChar.isdigit() for eachChar in user_password)  # At least one digit
        
    ):
        
        print("Password length - STRONG")
        print("CHECKING IN leaked 100million-password Wait.......")
        time.sleep(1)
        #db-leaks checker
        leaked_db_check=leaked_db_checker(user_password)
        if not leaked_db_check:
            print("\nPASSWORD NOT FOUND IN DATABASE LEAK\n but WE AREN'T SURE !!\n \n CROSS VERIFY FROM OTHER SOURCE")
    else:
        print("PASSWORD WEAK")

def leaked_db_checker(user_password):
    try:
        with open("10-million-password-list-top-10000.txt","r") as leaksFile:
            #load into set for more fast 
            leaked_passwords = set(line.strip() for line in leaksFile)
            for eachLine in leaked_passwords:
                if user_password == eachLine.strip():
                    print("ALERT !!! \n LEAKED PASSWORD !!! \n TRY DIFFERENT !")
                    return True
            return False
    except FileNotFoundError:print('FILE NOT FOUND BRO (10-million-passowrd-list-top-1000.txt) !')
    except Exception as fe :print('ERROR - ',fe)
if __name__ == "__main__":
    main()