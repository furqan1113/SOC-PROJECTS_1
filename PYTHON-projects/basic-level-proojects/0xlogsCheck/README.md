# 🚀 Log Analyzer: IP Count & DoS Check

A **Python** script that reads log files, counts unique IP addresses, and detects potential **Denial-of-Service (DoS)** attempts based on IP request frequency.

## Features:
- Accepts log file paths via command-line arguments.
- Counts unique IPs from the log.
- Flags IPs that make too many requests (potential DoS).
- Displays the total number of unique IPs and the request count per IP.

---

## 🚀 Requirements:
- Python 3.x

---

## 🛠️ How to Use:
1. Clone or download the repository.
2. Install any dependencies (if required).
3. Run the script with the log file path as an argument:
   ```bash
   python3 log_analyzer.py -f /path/to/logfile.log
📝 Example Output:
markdown
Copy
Edit
Total Unique IPs: 10

IP: 192.168.0.1 — Requests: 15
----------
⚠️ WARNING: 192.168.0.1 may be performing a DoS attack!
----------
IP: 192.168.0.2 — Requests: 3
⚙️ How It Works:
Input: The script processes each line of the log file, extracting the IP from each line.

Processing: A dictionary is used to count the frequency of each IP address.

DoS Detection: If an IP exceeds the threshold (5 requests), it is flagged as potentially malicious.

🚀 Future Enhancements:
Improve DoS detection logic (e.g., rate-limiting).

Add more analysis features (e.g., geographical location of IPs).

Enhance error handling and logging.
