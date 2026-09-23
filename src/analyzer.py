#!/usr/bin/env python3
# ============================================================
# === analyzer.py - Analyze logs for Brute Force attacks ====
# ============================================================

import sys
import re
from collections import defaultdict

# Threshold for brute force detection
THRESHOLD = 5


def parse_log_file(filepath):
    """
    Reads the log file and extracts IP addresses from failed logins.

    Args:
        filepath (str): Path to the log file

    Returns:
        dict: IP addresses with number of failed attempts
    """
    ip_counts = defaultdict(int)

    try:
        with open(filepath, 'r') as file:
            for line in file:
                # match for IP-address in log line
                match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
                if match:
                    ip = match.group(1)
                    ip_counts[ip] += 1
    except FileNotFoundError:
        print(f"[ERROR] File {filepath} not found!")
        return None

    return ip_counts


def detect_brute_force(ip_counts, threshold):
    """
    Identifies IP addresses that exceeded the threshold.

    Args:
        ip_counts (dict): IP addresses with number of attempts
        threshold (int): Threshold for warning

    Returns:
        dict: Suspicious IP addresses with number of attempts
    """
    suspicious = {}
    for ip, count in ip_counts.items():
        if count >= threshold:
            suspicious[ip] = count
    return suspicious

def generate_report(suspicious, total_attempts, threshold):
    """
    Creates a report of suspicious activity.

    Args:
        suspicious (dict): Suspicious IP addresses
        total_attempts (int): Total number of failed logins
        threshold (int): Threshold used
    """
    print("\n" + "=" * 50)
    print("🔒 LOG ANALYSIS REPORT 🔒")
    print("=" * 50)
    print(f"📊 Total failed logins: {total_attempts}")
    print(f"🚨 Threshold: {threshold} attempts")
    print("-" * 50)

    if suspicious:
        print(f"\n⚠️ POTENTIAL BRUTE FORCE ATTACK DETECTED!")
        print(f"   {len(suspicious)} IP address(es) over threshold:\n")
        for ip, count in sorted(suspicious.items(),
                                key=lambda x: x[1], reverse=True):
            print(f"   🔴 {ip} → {count} failed attempts")
    else:
        print("\n✅ No suspicious activity detected.")

    print("\n" + "=" * 50)

def main():
    """Main function that controls program flow."""
    if len(sys.argv) < 2:
        print("Usage: python3 analyzer.py <logfile>")
        sys.exit(1)

    log_file = sys.argv[1]
    ip_counts = parse_log_file(log_file)
    if ip_counts is None:
        sys.exit(1)

    total_attempts = sum(ip_counts.values())
    suspicious = detect_brute_force(ip_counts, THRESHOLD)
    generate_report(suspicious, total_attempts, THRESHOLD)

if __name__ == "__main__":
    main()
