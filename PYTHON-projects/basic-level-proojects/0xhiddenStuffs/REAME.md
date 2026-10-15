# Hidden Files Finder

A Python script to find hidden files in a specified directory. It supports both non-recursive and recursive searches and can save the results to an output file.

## Features

- Find hidden files in a specified directory.
- Recursive search through subdirectories.
- Save results to an output file (`h_files.txt`).

## Usage

### Prerequisites

- Python 3.x installed on your system.

### Running the Script

1. Clone the repository or download the script.
2. Open a terminal and navigate to the directory containing the script.
3. Run the script with the following options:

```bash
python script.py -p <path> [--recursive] [--output]
```

### Arguments

- `-p`, `--path`: Specify the directory path to search for hidden files.
- `--recursive`: Enable recursive search through subdirectories.
- `--output`: Save the results to an output file (`h_files.txt`).

### Example

```bash
python script.py -p /path/to/directory --recursive --output
```

## Error Handling

The script handles the following errors gracefully:
- File not found.
- Permission errors.
- General exceptions.

## Author

Furqan Ayoub

## License

This project is licensed under the MIT License.