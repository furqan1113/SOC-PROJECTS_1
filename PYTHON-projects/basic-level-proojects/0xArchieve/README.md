# 📦 Archive Tool

***A powerful Python command-line utility for creating ZIP and TAR.GZ archives with advanced filtering options.***

---

## 🚀 Features

- ✅ **Dual Format Support**: Create both ZIP and TAR.GZ archives
- 🔍 **File Filtering**: Exclude specific file extensions
- 📊 **Verbose Mode**: Detailed progress tracking with color output
- 🔐 **Permission Handling**: Graceful handling of permission-denied files
- 📁 **Relative Path Preservation**: Maintains directory structure in archives

---

## 📋 Requirements

```bash
pip install colorama
```

---

## 🔧 Installation

**1. Clone this repository:**
```bash
git clone [your-repo-url]
cd archive-tool
```

**2. Install dependencies:**
```bash
pip install -r requirements.txt
```

---

## 💻 Usage

### 🎯 Basic Usage

```bash
# Create a ZIP archive
python archieve.py -p /path/to/folder --name backup.zip --method zip

# Create a TAR.GZ archive  
python archieve.py -p /path/to/folder --name backup.tar.gz --method tar.gz
```

### ⚡ Advanced Usage

```bash
# Exclude specific file types
python archieve.py -p /path/to/folder --name backup.zip --method zip --exclude .log .tmp .cache

# Enable verbose mode
python archieve.py -p /path/to/folder --name backup.tar.gz --method tar.gz --verbose

# Complete example with all options
python archieve.py -p ./documents --name docs_backup.zip --method zip --exclude .log .tmp --verbose
```

---

## 📝 Command Line Arguments

| **Argument** | **Description** | **Required** | **Example** |
|--------------|-----------------|--------------|-------------|
| `-p, --path` | Path to folder to archive | ✅ **Yes** | `-p /home/user/docs` |
| `--name` | Output archive filename | ✅ **Yes** | `--name backup.zip` |
| `--method` | Archive method | ✅ **Yes** | `--method zip` or `--method tar.gz` |
| `--exclude` | File extensions to skip | ❌ No | `--exclude .log .tmp .cache` |
| `--verbose` | Enable detailed output | ❌ No | `--verbose` |

---

## 📁 Project Structure

```
archive-tool/
├── 📄 archieve.py      # Main script with argument parsing
├── 📦 zipPing.py       # ZIP archive functionality  
├── 🗜️  tarGz.py         # TAR.GZ archive functionality
├── 📚 README.md        # Documentation (this file)
└── 📋 requirements.txt # Python dependencies
```

---

## 🎯 Example Output

### **Normal Mode:**
```
DONE...!
```

### **Verbose Mode:**
```bash
[ARCHIVING....] - document.pdf
[ARCHIVED] - document.pdf
[SKIPPED] - temp.log  
[ARCHIVING....] - image.jpg
[ARCHIVED] - image.jpg
[NO PERMISSIONS] - system.file
DONE...!
```

---

## ⚠️ Important Notes

> **🔴 File Permissions**: Files without read permissions are automatically skipped  
> **🟡 Directory Structure**: Original folder hierarchy is preserved in archives  
> **🟢 Default Exclusions**: `.log` and `.tmp` files are excluded by default  
> **🔵 Extension Matching**: Archive names ***must*** include proper extensions

---

## 🐛 Error Handling

The tool gracefully handles:

- ❌ **Invalid folder paths**
- 🚫 **Permission denied errors** 
- 📂 **File not found errors**
- 🏷️ **Invalid archive extensions**
- 💥 **General exceptions with descriptive messages**

---

## 📚 **Learning Purpose**

*This project demonstrates:*

- ✨ Command-line argument parsing with `argparse`
- 🗂️ File system operations with `os` module
- 🛡️ Comprehensive error handling
- 📦 Archive creation (`zipfile` & `tarfile`)
- 🎨 Terminal color output with `colorama`
- 🔄 Cross-platform compatibility

---

## 🔄 Future Improvements

- [ ] 🗜️ Add compression level options
- [ ] 🔒 Support for password-protected archives  
- [ ] 📊 Progress bar for large archives
- [ ] ⚙️ Configuration file support
- [ ] ⚡ Multi-threading for faster processing
- [ ] 📈 Archive size statistics
- [ ] 🔍 Duplicate file detection

---

## 🏷️ **Tags**

`#Python` `#CLI-Tool` `#Archive` `#Scripting` `#File-Management` `#Learning-Project`

---

## 📄 License

> **Educational Use**: This project is created for learning purposes.  
> **Disclaimer**: Always test on sample data before using on production files.

---

***⭐ If you find this project helpful, please give it a star!***

---

**Made with ❤️ while learning Python scripting**