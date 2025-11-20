# 💠 **Kerberos TimeSync Toolkit**

### *Auto-sync your Linux host clock with an Active Directory Domain Controller for Kerberos attacks*

![banner](https://via.placeholder.com/1200x250?text=Kerberos+TimeSync+Toolkit)

---

## ⚡ Overview

Kerberos authentication **requires** your machine’s system time to be within **5 minutes** of the Domain Controller (DC).
When attacking Active Directory from Kali/Linux, this often causes:

```
Kerberos SessionError: KRB_AP_ERR_SKEW (Clock skew too great)
```

This toolkit fixes that automatically.

### ✔ Auto-detect DC time

### ✔ Auto-set Linux time & timezone

### ✔ Ready for Kerberoasting, AS-REP roast, RBCD, constrained delegation

### ✔ Includes safe revert script to restore your local clock

---

# 📁 **Included Scripts**

| File              | Description                                                             |
| ----------------- | ----------------------------------------------------------------------- |
| `sync_dc_time.sh` | Bash script to fetch DC time via `nmap` and auto-sync local system time |
| `sync_dc_time.py` | Python version of the time sync script                                  |
| `revert_time.sh`  | Restore your normal timezone + re-enable NTP                            |

---

# 🚀 Setup

```bash
git clone https://github.com/<yourname>/kerberos-timesync-toolkit
cd kerberos-timesync-toolkit
chmod +x *.sh *.py
```

---

# 🟢 **1. sync_dc_time.sh (Bash Script)**

A fast, reliable script to auto-sync your Linux clock to an AD DC.

### **Usage**

```bash
./sync_dc_time.sh <dc-ip>
```

### **Example**

```bash
./sync_dc_time.sh 10.129.8.127
```

### **What it does**

* Runs `nmap --script smb2-time`
* Parses DC timestamp
* Disables NTP
* Switches to **UTC** (required for HTB environments)
* Sets exact DC time
* Prints new time

---

# 🔵 **2. sync_dc_time.py (Python Script)**

A Python implementation with cleaner parsing and cross-CLI compatibility.

### **Usage**

```bash
python3 sync_dc_time.py <dc-ip>
```

### **Example**

```bash
python3 sync_dc_time.py 10.129.8.127
```

This script:

* Fetches DC time
* Converts it from ISO8601 → Linux format
* Adjusts timezone
* Sets clock

Perfect for automating Kerberos-based attack chains.

---

# 🟣 **3. revert_time.sh**

Resets everything after your AD attack is complete.

### **Usage**

```bash
./revert_time.sh
```

This restores:

* **NTP enabled**
* **Timezone: Asia/Kolkata** *(customize if needed)*
* **Current regional date/time**

---

# 🎯 Why This Toolkit?

When performing:

* Kerberoasting
* AS-REP Roasting
* TargetedKerberoast
* RBCD / Shadow Credentials
* S4U2Self/S4U2Proxy attacks
* `GetUserSPNs.py -request`
* `Rubeus.exe asktgt /asrep /tgtdeleg /opsec`

Kerberos **will fail every time** unless your host time matches the DC.

These scripts automate that process with a single command.

---

# 🛡 Disclaimer

This toolkit is intended for:

* Security researchers
* Ethical hacking
* CTFs / HackTheBox / ProLabs
* Lab environments
* Authorized penetration testing

Do **not** use this on networks without explicit permission.

---

# ⭐ Contribute

PRs, improvements, and feature suggestions are welcome.
Feel free to add:

* Auto-detection for domain
* Multiple domain controller support
* Dry-run mode

---

# 📬 Contact

For issues, feature requests, or enhancements:

---
