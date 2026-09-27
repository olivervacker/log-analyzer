# Log Analyzer - SIEM-light

An automated tool for detecting Brute Force attacks through log analysis.

## Description

This project combines **Python** and **Bash** to create a lightweight SIEM (Security Information and Event Management) tool. It collects authentication logs from Linux systems, analyzes failed login attempts, and identifies potential Brute Force attacks.

### What it does

1. **Collects** authentication logs from `/var/log/auth.log` using a Bash script
2. **Extracts** IP addresses from failed login attempts using Python regex
3. **Counts** failed attempts per IP address
4. **Detects** potential Brute Force attacks (default threshold: 5 attempts)
5. **Generates** a clear report of suspicious activity

## Technical Stack

| Technology | Purpose |
|------------|---------|
| **Python 3** | Main analysis and report generation |
| **Bash** | Log collection and automation |
| **Linux (Ubuntu)** | Testing environment |
| **Git & GitHub** | Version control |
| **VirtualBox** | Virtual machine for testing |

## Project Structure

log-analyzer/
├── scripts/
│ └── get_logs.sh # Bash script for log collection
├── src/
│ └── analyzer.py # Python script for log analysis
├── data/ # Log files and reports (gitignored)
│ └── auth_*.log
├── tests/ # Test files (coming soon)
├── docs/ # Documentation (coming soon)
├── README.md
└── .gitignore

## Installation

### Prerequisites

- Linux (Ubuntu 22.04 or similar)
- Python 3.10+
- Bash
- sudo access (for reading /var/log/auth.log)

### Setup

1. **Clone the repository:**

git clone git@github.com:olivervacker/log-analyser.git
cd log-analyser

2. **Make the Bash script executable:**

chmod +x scripts/get_logs.sh

3. **(Optional) Install Python dependencies:**

pip3 install --user regex

### Usage
**Step 1: Collect logs**

Run the Bash script to collect failed login attempts:

./scripts/get_logs.sh

### Output:

📁 Collecting logs from /var/log/auth.log...
✅ Found 11 failed login attempts
💾 Saved to: ./data/auth_20260926_230246.log

**Step 2: Analyze logs**

Run the Python script to analyze the collected logs:

python3 src/analyzer.py data/auth_20260926_230246.log

#### Output:

==================================================
🔒 LOG ANALYSIS REPORT 🔒
==================================================
📊 Total failed logins: 11
🚨 Threshold: 5 attempts
--------------------------------------------------

⚠️ POTENTIAL BRUTE FORCE ATTACK DETECTED!
   1 IP address(es) over threshold:

   🔴 192.168.1.100 → 11 failed attempts

==================================================

### How It Works

Bash Script (get_logs.sh)

Reads /var/log/auth.log

Filters out lines containing "Failed password"

Saves results to data/auth_YYYYMMDD_HHMMSS.log

Python Script (analyzer.py)

Reads the log file line by line

Extracts IP addresses using regex: from (\d+\.\d+\.\d+\.\d+)

Counts failed attempts per IP using defaultdict

Flags IPs exceeding the threshold (5 attempts)

Generates a report sorted by number of attempts

## Testing
All five test scenarios passed successfully:

**Test	Description	Status**
**Test 1**	Normal run (no attack)	✅ Passed
**Test 2**	Simulated attack (11 attempts from same IP)	✅ Passed
**Test 3**	Empty log file	✅ Passed
**Test 4**	Wrong format	✅ Passed
**Test 4B**	Non-existent file	✅ Passed

## Future Improvements
**□ Support for multiple log files**
**□ Email alerts on detected attacks**
**□ Graphical dashboard (matplotlib/Flask)**
**□ Database storage (SQLite)**
**□ Windows Event Log support (PowerShell)**
**□ GeoIP lookup for attacker IPs**

## License

**MIT License**

## Author

**Oliver Vacker**

- GitHub: @olivervacker
- LinkedIn: Oliver Vacker