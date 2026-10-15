# DirBuster

DirBuster is a Python-based directory enumeration tool. It checks for the existence of specified directories on a given web server and saves the found paths to a file. The tool now supports command-line arguments for enhanced usability.

## Features

- Accepts a target URL and wordlist file via command-line arguments.
- Verbose mode for detailed output.
- Saves valid paths to an output file.
- Handles connection errors gracefully.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/DirBuster.git
   ```
2. Navigate to the project directory:
   ```bash
   cd DirBuster
   ```

## Usage

1. Prepare a text file (e.g., `dirFile.txt`) with the directory paths you want to check.
2. Run the script with the following arguments:
   ```bash
   python dirBuster.py -u <target_url> -w <wordlist_file> -o <output_file>
   ```
   - `-u` or `--url`: Specify the target URL (e.g., `http://example.com`).
   - `-w` or `--wordlist`: Specify the wordlist file containing directory paths.
   - `-o` or `--output`: Specify the output file to save found paths.
   - `-v` or `--verbose`: Enable verbose mode for detailed output.

### Example
```bash
python dirBuster.py -u http://localhost:8080 -w dirFile.txt -o foundPaths.txt -v
```

## Error Handling

- Handles HTTP errors like `404 Not Found` and connection errors gracefully.
- Prints meaningful error messages for debugging.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.