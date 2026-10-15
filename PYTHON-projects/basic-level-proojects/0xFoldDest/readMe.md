# Folder Destroyer

Folder Destroyer is a Python-based tool to delete folders or files with options for forced deletion and overwriting file contents. Use this tool responsibly, as it can permanently delete data.

## Features

- Deletes folders and their contents.
- Supports forced deletion with the `--force` flag.
- Overwrites file contents before deletion with the `--overwrite` flag.
- Handles errors like missing paths, invalid directories, and permission issues.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Folder-Destroyer.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Folder-Destroyer
   ```

## Usage

Run the script with the following arguments:

```bash
python folder_dest.py -p <path_to_folder> [--force] [--overwrite]
```

### Arguments:
- `-p` or `--path`: Specify the path of the folder to delete.
- `--force`: Forcefully deletes the folder and its contents.
- `--overwrite`: Overwrites the contents of files before deletion (requires `--force`).

### Example:
1. Delete an empty folder:
   ```bash
   python folder_dest.py -p C:\path\to\empty\folder
   ```

2. Forcefully delete a folder and its contents:
   ```bash
   python folder_dest.py -p C:\path\to\folder --force
   ```

3. Overwrite file contents before deletion:
   ```bash
   python folder_dest.py -p C:\path\to\folder --force --overwrite
   ```

## Error Handling

- **Path not specified**: Displays an error if the `--path` argument is missing.
- **Invalid path**: Checks if the specified path exists and is a directory.
- **Permission issues**: Handles permission errors gracefully.
- **File not found**: Displays an error if a file or folder is missing.

## Warnings

- **Dangerous Flags**: The `--force` and `--overwrite` flags can cause irreversible data loss. Use them with caution.
- **Environment**: Ensure you are using this tool in a safe environment to avoid accidental data loss.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.