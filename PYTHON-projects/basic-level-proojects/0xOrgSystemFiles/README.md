# 📂 File Organizer v1

## 📝 Overview
**File Organizer v1** is a Python-based utility that organizes files in a specified folder by their extensions. It supports copying or moving files to categorized subfolders (e.g., `PDFs`, `TXTs`) and allows users to specify a custom destination for the organized files.

---

## ✨ Features
- 📁 Organizes files by their extensions into categorized subfolders.
- 🔄 Supports both **copying** and **moving** files.
- 📍 Allows specifying a custom destination for organized files.
- 🛠️ Automatically creates destination folders if they don't exist.
- 📝 Logs actions (optional).

---

## ⚙️ Requirements
- **Python 3.x**
- Modules:
  - `os`
  - `shutil`
  - `argparse`
  - `time`

---

## 🚀 Usage

### 🔧 Command Syntax
```bash
python new.py -p <source_folder> [--copy | --move] [-d <destination_folder>] [--log]
```

### 📜 Arguments
| Argument             | Description                                                                                  | Required | Default Value          |
|----------------------|----------------------------------------------------------------------------------------------|----------|------------------------|
| `-p`, `--path`       | Path to the folder containing files to organize.                                             | ✅ Yes   | N/A                    |
| `--copy`             | Copy files to the destination folder.                                                        | ❌ Optional | N/A                    |
| `--move`             | Move files to the destination folder.                                                        | ❌ Optional | N/A                    |
| `-d`, `--destination`| Path to the destination folder where files will be organized.                                | ❌ Optional | Current working directory (`os.getcwd()`) |
| `--log`              | Enable logging of actions (e.g., copied/moved files).                                        | ❌ Optional | Disabled               |

---

### 📂 Examples

#### 1️⃣ Organize Files by Copying to the Current Directory
```bash
python new.py -p c:/Users/furqa/Desktop/myPROJECTS/file-organizer/sampleFolder --copy
```

#### 2️⃣ Organize Files by Moving to a Custom Destination
```bash
python new.py -p c:/Users/furqa/Desktop/myPROJECTS/file-organizer/sampleFolder -d c:/Users/furqa/Desktop/myPROJECTS/file-organizer/organizedFolder --move
```

#### 3️⃣ Enable Logging While Copying Files
```bash
python new.py -p c:/Users/furqa/Desktop/myPROJECTS/file-organizer/sampleFolder --copy --log
```

---

## 🛠️ How It Works

1. **Input Validation**:
   - ✅ Checks if the source folder (`--path`) exists and is a valid directory.
   - ✅ Validates the destination folder (`--destination`) and creates it if it doesn’t exist.

2. **File Organization**:
   - 📂 Iterates through the files in the source folder.
   - 🗂️ Categorizes files based on their extensions (e.g., `.pdf`, `.txt`).
   - 📁 Creates subfolders for each file type in the destination folder.
   - 🔄 Copies or moves files to the appropriate subfolders.

3. **Logging (Optional)**:
   - 📝 Logs actions (e.g., copied/moved files) to a `log-file.txt` in the current working directory.

---

## 📁 Folder Structure

```
file-organizer/
│
├── sampleFolder/                # Example folder with unorganized files
├── organizedFolder/             # Destination folder for organized files (created dynamically)
├── new.py                       # Main script
├── log-file.txt                 # Log file (optional, created if logging is enabled)
└── README.md                    # Project documentation
```

---

## ⚠️ Error Handling

- **Invalid Source Path**:
  - ❌ If the source folder does not exist or is not a directory, the program exits with an error message.
- **Invalid Destination Path**:
  - ❌ If the destination folder is not writable, the program exits with an error message.
- **File Name Conflicts**:
  - 🛠️ Handles files with the same name by overwriting them in the destination folder.

---

## 🚀 Future Enhancements

- 📅 Add support for organizing files by creation or modification date.
- 🖋️ Allow users to specify custom folder names for file types.
- 🧪 Add a dry-run mode to preview changes without making modifications.

---

## 📜 License

This project is licensed under the **MIT License**. Feel free to use, modify, and distribute it.

---

## Made by
***0xfurqan***
