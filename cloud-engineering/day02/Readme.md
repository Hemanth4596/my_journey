# ☁️ Day 2 - Cloud Engineering Toolkit

**📅 Date:** July 20, 2026  
**🎯 Goal:** Learn essential Linux log analysis tools, Git fundamentals, and Python automation used in Cloud Infrastructure Engineering.

---

# 📸 Screenshots Taken Today

- 📷 [OS & Disk Information](screenshots/File-Inspection&OS-Info.png)
- 📷 [Log Hunting](screenshots/File-Inspection&OS-Info.png)
- 📷 [Pipes & Sorting](screenshots/Pipes&Sorting.png)
- 📷 [Python System Information Script](screenshots/Python-Automation-(sysinfo.py).png)

---

# 📖 What I Learned Today

## 1. Linux Investigation Commands

Practiced the core commands used by Linux administrators and SREs.

| Command | Purpose |
|----------|---------|
| `cat` | Display file contents |
| `less` | Read large files page by page |
| `grep` | Search text patterns |
| `find` | Locate files and directories |
| `wc` | Count lines, words, and characters |
| `df -h` | Display disk usage |
| `sort` | Sort output alphabetically or numerically |
| `|` | Pass the output of one command to another |

---

## 2. Log Analysis

System logs are the first place to investigate when diagnosing problems.

Example:

```bash
sudo grep -c "FAILED" /var/log/auth.log
```

This counts failed login attempts recorded by the operating system.

---

## 3. Pipes

Pipes (`|`) allow multiple commands to work together.

Example:

```bash
grep "FAILED" /var/log/auth.log | wc -l
```

Instead of manually counting matching lines, Linux passes the output of `grep` directly to `wc`.

---

## 4. Disk Usage

```bash
df -h
```

This command displays storage usage in a human-readable format and helps identify disks that are running out of space.

---

## 5. User Enumeration

```bash
wc -l /etc/passwd
```

Counts the total number of user entries stored on the system.

---

## 6. Git Configuration

Configured Git identity for version control.

```bash
git config --global user.name "Your Name"

git config --global user.email "your@email.com"
```

Git is the foundation of Infrastructure-as-Code and collaborative engineering.

---

## 7. Python Automation

Created my first infrastructure automation script.

```python
import os
import subprocess

print("===== CLOUD VM SYSTEM INFO =====")

print(f"Hostname: {os.uname().nodename}")

print(f"System: {os.uname().sysname} {os.uname().release}")

print(f"Uptime: {subprocess.check_output('uptime', text=True).strip()}")

print("Disk Usage:")

print(subprocess.check_output('df -h /', text=True).strip())
```

This script retrieves:

- Hostname
- Operating System
- Kernel Version
- System Uptime
- Root Disk Usage

using both Python libraries and Linux commands.

---

# 📝 Lab Results

- ✅ Verified Ubuntu installation
- ✅ Checked available disk space
- ✅ Counted failed login attempts
- ✅ Counted local users
- ✅ Configured Git successfully
- ✅ Built and executed the first infrastructure automation script

---

# 💡 Key Takeaways

- `grep` is one of the most powerful troubleshooting tools available in Linux.
- Pipes allow commands to be combined into efficient workflows.
- Git tracks every infrastructure change and enables collaboration.
- Python's `subprocess` module bridges Python with Linux commands, making automation possible.

---

# ❌ Mistakes I Made Today

| Mistake | Why It Happened | How I Fixed It |
|----------|-----------------|----------------|
| Typed the wrong path while counting users (`/etc/passwd`) | Small typing mistake while entering the command | Rechecked the command and corrected the path. |
| Forgot to finish the `EOF` block while creating `sysinfo.py` | I was unfamiliar with here-documents (`cat << EOF`) | Typed `EOF` on a new line to save the file correctly. |
| Tried running the Python script before confirming it was created | Didn't verify the file after writing it | Used `ls` and `cat sysinfo.py` before execution. |
| Initially forgot to use `python3` | Ubuntu uses Python 3 by default | Executed the script with `python3 sysinfo.py`. |
| Git configuration wasn't reflected immediately | Forgot to verify the configuration | Checked it using `git config --list`. |

---

# 🐛 Errors I Encountered

| Error | Cause | Resolution |
|--------|-------|-----------|
| `No such file or directory` | Incorrect file path | Corrected the path and reran the command. |
| Shell waiting for `EOF` | Here-document wasn't closed | Typed `EOF` on a separate line. |
| `python3: can't open file` | Script wasn't created yet | Completed the file creation before execution. |

---

# 🎯 Day Summary

## ✅ Skills Learned

- Linux log investigation
- Text searching with `grep`
- Pipes and command chaining
- Disk usage analysis
- User enumeration
- Git configuration
- Python automation
- Executing Linux commands from Python

---

# 🚀 Next Steps

Continue building Python automation by learning:

- Functions
- Loops
- Lists
- Dictionaries
- Modules
- File parsing
- Infrastructure automation scripts

---

# 🙏 Honest Reflection

Today reinforced an important lesson: **small mistakes slow you down more than difficult concepts.**

Most of my issues weren't caused by Linux or Python—they were caused by typing mistakes, missing `EOF`, or running commands before verifying that files had been created.

Instead of guessing, I learned to verify each step:

- Check that the file exists.
- Confirm the command syntax.
- Read the error message carefully.
- Fix the root cause before moving on.

I also saw how Cloud Engineers spend a significant amount of time reading logs, verifying system state, and automating repetitive tasks rather than manually repeating commands.

Every mistake today became part of my learning process, and documenting those mistakes ensures I won't repeat them as I progress.

> **"Automation isn't about writing more code—it's about reducing repeated human mistakes."** ☁️🐧