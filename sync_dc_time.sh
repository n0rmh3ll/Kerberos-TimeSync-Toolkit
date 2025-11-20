#!/bin/bash

DC_IP="$1"

if [ -z "$DC_IP" ]; then
    echo "Usage: $0 <dc-ip>"
    exit 1
fi

echo "[*] Getting DC time from $DC_IP..."

DC_TIME=$(nmap --script smb2-time -p445 "$DC_IP" | grep "date:" | awk '{print $2}' | sed 's/T/ /')

if [ -z "$DC_TIME" ]; then
    echo "[-] Failed to fetch DC time."
    exit 1
fi

echo "[+] DC time: $DC_TIME"

echo "[*] Disabling NTP..."
sudo timedatectl set-ntp no

echo "[*] Setting timezone to UTC..."
sudo timedatectl set-timezone UTC

echo "[*] Setting system time to DC time..."
sudo date -s "$DC_TIME"

echo "[+] Time sync complete. Current local time:"
date
