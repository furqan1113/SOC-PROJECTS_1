# 🛡️ RECON TOOL - v0.1  
> A Python-based CLI tool to ping targets, scan with Nmap, and gather WHOIS info.

---

## ⚙️ Features

- 🔍 Ping detection (ICMP)
- ⚡ Nmap SYN scan (`-sS`)
- 🌐 WHOIS info for web ports (80/443)
- 📁 Log results per target in `.log` files
- 📦 Support single IP, line-separated, or CSV list input
- 💬 Verbose mode for detailed terminal output

---

## 📦 Installation

```bash
git clone https://github.com/<yourusername>/recon-tool.git
cd recon-tool
pip install -r requirements.txt
```

> ✅ Make sure `nmap`, `ping`, and `whois` are installed and accessible in your system’s PATH.

---

## 🚀 Usage

```bash
python3 recon.py -i 192.168.1.1 -t single --verbose
python3 recon.py -l ipList.txt -t lines
python3 recon.py -l ipList.csv -t csv --verbose
```

---

## 🧠 Command Reference

| Flag               | Description                                           |
|--------------------|-------------------------------------------------------|
| `-i`, `--ip`       | Scan a **single** IP/domain                           |
| `-l`, `--iplist`   | Provide a **file** with targets                       |
| `-t`, `--filetype` | File format: `single`, `lines`, or `csv` *(required)* |
| `--verbose`        | Enable detailed scanning output                       |

---

## 📂 Input File Examples

### `ipList.txt` (for `--filetype lines`)
```
8.8.8.8
1.1.1.1
github.com
```

### `ipList.csv` (for `--filetype csv`)
```
openai.com,cloudflare.com,stackoverflow.com
```

---

## 📁 Output Example

For each scanned host, results are saved in:

```
cmd_<IP>.log
```

Each log includes:
- Nmap open ports
- Service names
- WHOIS summary (for ports 80/443)

---

## 📌 Requirements

Only one Python dependency:
```
colorama>=0.4.6
```

Install via:
```bash
pip install -r requirements.txt
```

System tools required:
- `ping` (default in all OSes)
- [`nmap`](https://nmap.org/download.html)
- [`whois`](https://linux.die.net/man/1/whois)

---

## 🧪 Sample Log Output

```text
[SCAN RESULT] 8.8.8.8
-------------------------------
PORT     STATE SERVICE
53/tcp   open  domain
443/tcp  open  https
...
WHOIS INFO for 8.8.8.8
Domain Name: GOOGLE.COM
Registrar: MarkMonitor Inc.
Creation Date: 1997-09-15T04:00:00Z
...
```

---

## 🛠️ Roadmap

- [ ] Banner grabbing
- [ ] Service fingerprinting
- [ ] Export results as JSON

---

## 👤 Author

**Furqan Ayoub**  
🔗 [GitHub](https://github.com/furqan1ayoub)  
💼 [LinkedIn](https://www.linkedin.com/in/furqan-ayoub-39a6a935b/)

---

## 📄 License

MIT License. You can use, modify, and distribute this tool freely with attribution.

---

## 🤝 Contributions

PRs welcome. If you have improvements or bug fixes, feel free to open an issue or pull request!
