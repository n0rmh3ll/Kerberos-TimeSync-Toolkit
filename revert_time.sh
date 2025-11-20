#!/bin/bash
echo "[*] Restoring system clock..."
sudo timedatectl set-ntp yes
sudo timedatectl set-timezone Asia/Kolkata
echo "[+] Clock restored to normal."
date
