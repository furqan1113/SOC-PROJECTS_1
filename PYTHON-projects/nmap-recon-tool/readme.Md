# 🛡️ Recon Tool v0.1

A small Python CLI that automates a first-pass recon workflow: **ping a target, scan it with Nmap if it responds, and pull WHOIS details when a web port is open.**

> ⚠️ **Use only on systems you own or have explicit written permission to test.** Port scanning third-party hosts without authorization may be illegal. The sample target lists in this repo use public hosts purely as format examples.

---

## ⚙️ How It Works

```
targets (single / file)
        │
        ▼
   ping (2 packets, 4s timeout)
        │ host up?
        ├── no  → reported DOWN, skipped
        ▼ yes
   nmap -sS <target>   (20s timeout)
        │
        ▼
   parse output → print PORT / STATE / SERVICE
        │
        ├── port 80 or 443 open → whois lookup (key fields printed)
        ▼
   raw Nmap output appended to cmd_<target>.log
```

## ✨ Features

- 🔍 ICMP ping check before scanning (cross-platform flag: `-c` on Linux/macOS, `-n` on Windows)
- ⚡ Nmap TCP SYN scan (`-sS`)
- 🌐 WHOIS summary for hosts with port 80/443 open (domain name, registrar, creation/expiry/updated dates, name servers)
- 📁 Per-target log files containing the raw Nmap output
- 📦 Input as a single target, a newline-separated file, or a comma-separated file
- 🗣️ `--verbose` mode for step-by-step output
- 🎨 Colour-coded terminal output via `colorama`

---

## 📂 Project Structure

```
recon-tool/
├── recon.py            # entry point: argument parsing and target loading
├── main1.py            # core logic: ping, Nmap, port parsing, WHOIS, logging
├── requirements.txt    # Python dependency (colorama)
├── ipList.txt          # sample input, one target per line
└── ipList.csv          # sample input, comma-separated targets
```

`recon.py` imports `pingingTool` from `main1.py`, so keep both files in the same folder.

---

## 📦 Installation

```bash
git clone https://github.com/<yourusername>/recon-tool.git
cd recon-tool
pip install -r requirements.txt
```

**System tools required** (must be in your `PATH`):

| Tool | Notes |
|------|-------|
| `ping` | Built into most systems |
| [`nmap`](https://nmap.org/download.html) | On Windows, also needs Npcap |
| `whois` | Not installed by default on Windows or some minimal Linux images |

---

## 🚀 Usage

```bash
# Single target
sudo python3 recon.py -i scanme.nmap.org -t single --verbose

# File with one target per line
sudo python3 recon.py -l ipList.txt -t lines

# File with comma-separated targets
sudo python3 recon.py -l ipList.csv -t csv --verbose
```

> 🔑 **Run with `sudo` (Linux/macOS) or an Administrator terminal (Windows).** Nmap's `-sS` SYN scan needs raw-socket privileges; without them the scan fails and the tool reports "Nmap scan failed".

> 🎯 `scanme.nmap.org` is a host the Nmap project provides for testing scans.

### Options

| Flag | Description |
|------|-------------|
| `-i`, `--ip` | A single IP or domain to scan |
| `-l`, `--iplist` | Path to a file of targets |
| `-t`, `--filetype` | `single`, `lines`, or `csv` (**required**, even for a single target) |
| `--verbose` | Show detailed progress |

Use `-t single` with `-i`, and `-t lines` or `-t csv` with `-l`. A file with `-t single` is rejected.

### Input Formats

`ipList.txt` (`-t lines`):
```
8.8.8.8
github.com
```

`ipList.csv` (`-t csv`): one line, comma-separated:
```
example.com,example.org,192.168.1.10
```

---

## 📁 Output

**Terminal:** each port is printed as `PROTO PORT <n> is <state> - SERVICE: <name>`, followed by a WHOIS summary if a web port is open.

**Log file:** `cmd_<target>.log` is created in the working directory. It contains the **raw Nmap output only** (WHOIS is printed to the terminal, not saved). Results are appended, so repeated scans of the same target accumulate in one file.

```text
==================================================
[SCAN RESULT] 192.168.1.10
--------------------------------------------------
PORT    STATE SERVICE
22/tcp  open  ssh
80/tcp  open  http
```

---

## ⚠️ Known Limitations (v0.1)

- **ICMP-dependent:** hosts that block ping are reported as DOWN and never scanned.
- **Timeouts:** Nmap is cut off after 20 seconds, so slow or large scans may be incomplete.
- **Top 1000 ports only:** the scan uses Nmap's default port selection.
- **Port reporting:** closed and filtered ports are printed alongside open ones, and a log is written whenever any port line is parsed.
- **WHOIS on IPs:** the lookup runs against the target string as given, so IP targets return registry (network) records rather than domain records.
- **CSV parsing:** the file is split on commas only, so keep all targets on one line with no stray whitespace.
- **Sequential:** targets are processed one at a time.

## 🛠️ Roadmap

- [ ] Banner grabbing
- [ ] Service fingerprinting
- [ ] JSON export
- [ ] Save WHOIS output to the log file
- [ ] Trim whitespace and skip blank lines in input files
- [ ] Configurable timeouts and port ranges

---

## 👤 Author

**Furqan Ayoub**
🔗 [GitHub](https://github.com/furqan1ayoub)
💼 [LinkedIn](https://www.linkedin.com/in/furqan-ayoub-39a6a935b/)

## 📄 License

MIT License. Free to use, modify, and distribute with attribution.

## 🤝 Contributions

Issues and pull requests are welcome.