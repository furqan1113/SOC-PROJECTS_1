# Password Checker (CLI)

A Python-based **Password Checker** that validates the strength of a password provided via the command line. The tool checks the password against specific criteria to determine if it is **Strong** or **Weak**.

## Features
- Accepts a password as input via the command line.
- Provides a verbose mode for additional output.
- Validates the password based on the following criteria:
  - Must be longer than 8 characters.
  - Must contain at least one special character (`~!@#$&*()-=_+:;`).
  - Must contain both uppercase and lowercase letters.
  - Must contain at least one alphabetic character.
  - Must contain at least one digit.
- Outputs whether the password is **Strong** or **Weak**.

## Requirements
- Python 3.6 or higher.

## Installation

1. Clone this repository or download the script.
2. Ensure Python is installed on your system.
3. Run the script using the command line.

## Usage
Run the script with the following options:

### Arguments

- `-p` or `--password`: Provide the password to check.
- `-v` or `--verbose`: Enable verbose mode for additional output.

### Examples

#### Check a Strong Password
```bash
python main.py -p MyP@ssword123
```
Output:
```
Password STRONG
```

#### Check a Weak Password
```bash
python main.py -p weakpass
```
Output:
```
PASSWORD WEAK
```
#### Missing Password
```bash
python main.py -v
```
Output:
```
ValueError: Password is required. Use -p or --password to provide a password.
```

## How It Works

1. The script uses `argparse` to parse command-line arguments.
2. The `passwordChecker` function validates the password based on the defined criteria.
3. If the password meets all the criteria, it is deemed **Strong**; otherwise, it is **Weak**.
4. Verbose mode provides additional output for debugging or informational purposes.

## License

This project is licensed under the MIT License. You are free to use, modify, and distribute this project as long as the original license is included.

## Open to Contributions

This project is open to anyone. Feel free to contribute by submitting issues or pull requests to improve the functionality or add new features.

## Author

Created by Furqan Ayoub.