#!/usr/bin/env python3
import subprocess
import re
import sys

if len(sys.argv) != 2:
    print("Usage: python3 sync_dc_time.py <dc-ip>")
    sys.exit(1)

dc_ip = sys.argv[1]

print(f"[*] Fetching DC time from {dc_ip}...")

cmd = ["nmap", "--script", "smb2-time", "-p445", dc_ip]
output = subprocess.check_output(cmd).decode()

match = re.search(r"date:\s+([\d\-T:]+)", output)

if not match:
    print("[-] Failed to extract DC time.")
    sys.exit(1)

dc_time = match.group(1).replace("T", " ")
print(f"[+] DC Time: {dc_time}")

print("[*] Disabling NTP...")
subprocess.run(["sudo", "timedatectl", "set-ntp", "no"])

print("[*] Setting timezone to UTC...")
subprocess.run(["sudo", "timedatectl", "set-timezone", "UTC"])

print("[*] Setting system time...")
subprocess.run(["sudo", "date", "-s", dc_time])

print("[+] Time sync complete:")
subprocess.run(["date"])
