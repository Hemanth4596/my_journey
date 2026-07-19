# 🐧 Day 1: Ubuntu & Shell Fundamentals (Cloud Engineer Bootstrapping)

**📅 Date:** July 19, 2026  
**🎯 Goal:** Install Ubuntu (baseline OS for cloud workloads), bootstrap an environment similar to a GCP Compute Engine instance, and master the first five essential Linux commands: `uname`, `whoami`, `pwd`, `ls`, and `cd`.

> **Note:** No screenshots were taken during this introductory session.

---

# 📖 What I Learned Today

## 1. Ubuntu as the Foundation for Cloud Computing

Linux is the operating system that powers the majority of cloud infrastructure.

The Linux kernel abstracts hardware resources such as:

- CPU
- Memory
- Storage
- Network interfaces

Instead of interacting with hardware directly, applications communicate with the kernel through **system calls (syscalls)**.

The shell (Bash) is my primary interface to the operating system.

Everything I practice locally is directly transferable to:

- Google Cloud Platform (GCP)
- AWS EC2
- Azure Virtual Machines
- Docker containers
- Kubernetes worker nodes

---

## 2. The Five Foundational Linux Commands

These commands answer three important questions:

- **Who am I?**
- **Where am I?**
- **What exists around me?**

| Command | Purpose | Cloud Relevance |
|----------|---------|----------------|
| `uname -a` | Displays kernel version, architecture, and hostname | Verify OS before installing software |
| `whoami` | Shows the current logged-in user | Confirm privileges (`root` vs normal user) |
| `pwd` | Prints the current working directory | Prevents executing commands in the wrong location |
| `ls -la` | Lists files with detailed metadata | Inspect permissions, ownership, timestamps, and hidden files |
| `cd / && ls` | Navigate to the root filesystem and list directories | Explore the Linux Filesystem Hierarchy (FHS) |

---

# 3. Understanding File Metadata

Running

```bash
ls -la
```

produced output similar to:

```text
drwxr-xr-x 2 root root 4096 Jul 19 05:00 home
-rw-r--r-- 1 root root  220 Jul 19 05:00 .bash_logout
```

### Breaking It Down

- `d` → Directory
- `-` → Regular file
- `rwx` → Owner permissions
- `r-x` → Group permissions
- `r-x` → Others permissions

Other important metadata includes:

- Link count
- Owner
- Group
- File size
- Timestamp

This metadata is stored inside the file's **inode**.

---

# 4. Linux Filesystem Hierarchy (FHS)

Running

```bash
cd / && ls
```

showed the standard Linux directory layout.

```text
bin
boot
dev
etc
home
lib
media
mnt
opt
proc
root
run
sbin
srv
sys
tmp
usr
var
```

### Important Directories

| Directory | Purpose |
|------------|---------|
| `/bin` | Essential user commands |
| `/sbin` | System administration commands |
| `/etc` | Configuration files |
| `/home` | User home directories |
| `/var` | Logs, cache, spool files |
| `/proc` | Virtual filesystem exposing kernel information |
| `/sys` | Hardware and kernel interfaces |
| `/usr` | User applications and libraries |
| `/tmp` | Temporary files |

### Cloud Relevance

This structure exists on almost every Linux server:

- Google Compute Engine
- AWS EC2
- Azure VM
- Docker containers

Knowing where configuration files and logs are stored is essential for troubleshooting production systems.

---

# 📝 Commands Practiced

## Verify Operating System

```bash
uname -a
```

Example Output

```text
Linux Ubuntu-Server 7.0.0-28-generic #1-Ubuntu SMP x86_64 GNU/Linux
```

---

## Check Current User

```bash
whoami
```

Output

```text
attacker
```

---

## Print Current Directory

```bash
pwd
```

Output

```text
/home/attacker
```

---

## View Directory Contents

```bash
ls -la
```

Example Output

```text
total 36

drwxr-x--- 4 attacker attacker 4096 Jul 19 05:00 .
drwxr-xr-x 3 root     root     4096 Jul 19 04:50 ..
-rw------- 1 attacker attacker  220 Jul 19 05:00 .bash_history
```

---

## Explore the Root Filesystem

```bash
cd /

ls
```

Output

```text
bin
boot
dev
etc
home
lib
...
```

---

## Create My Learning Workspace

```bash
mkdir -p ~/sre-foundation/day1

cd ~/sre-foundation/day1

pwd
```

Output

```text
/home/attacker/sre-foundation/day1
```

---

# ❌ Mistakes I Made Today

| # | Mistake | Reason | Solution |
|---|----------|---------|----------|
| 1 | Forgot `sudo apt update` | Fresh Ubuntu installation | Updated package lists before installing software |
| 2 | Ran `cd /` without `&& ls` | Forgot command chaining | Used `cd / && ls` |
| 3 | Tried entering a directory before creating it | Missing `mkdir -p` | Created the directory first |

---

# 🐛 Errors I Faced

| Error | Meaning | Solution |
|--------|---------|----------|
| `cd: sre-foundation: No such file or directory` | Directory did not exist | Created it using `mkdir -p` |
| `bash: cd: too many arguments` | Incorrect command syntax | Corrected command chaining and quoting |

---

# 💡 Important Rules to Remember

- Always run **`uname -a`** on a new machine to verify the operating system.
- Always check **`pwd`** before running destructive commands.
- The Linux root filesystem (`/`) is standardized across cloud providers.
- Use **`ls -la`** to inspect permissions, ownership, timestamps, and hidden files.
- Learn the Filesystem Hierarchy Standard (FHS); you'll use it daily in cloud environments.

---

# 🎯 Day 1 Summary

## ✅ What I Learned

- Ubuntu is the standard operating system for most cloud environments.
- The shell is the primary interface for interacting with Linux.
- Mastered five foundational Linux commands:
  - `uname`
  - `whoami`
  - `pwd`
  - `ls`
  - `cd`
- Learned the Linux Filesystem Hierarchy.
- Understood the metadata displayed by `ls -la`.
- Created my local learning workspace (`~/sre-foundation/day1`).

---

## ❌ Mistakes

- Forgot to update package lists before installing software.
- Tried changing into a directory before creating it.
- Forgot command chaining while exploring the filesystem.

---

# 🚀 Next Steps

**Day 2: Shell Navigation, File Operations & Permissions**

Topics to cover:

- `mkdir`
- `touch`
- `cp`
- `mv`
- `rm`
- `find`
- `locate`
- File permissions (`chmod`)
- Ownership (`chown`)

---

# 🙏 Honest Reflection

Today was the foundation of my Linux and Cloud journey.

Setting up Ubuntu and becoming comfortable with the terminal reminded me that cloud engineering starts with mastering the operating system before moving to higher-level services.

The terminal is my primary interface with the system. Every command gives direct insight into how Linux works, without relying on graphical tools.

Today's session wasn't about doing many things—it was about understanding the environment I'll be working in throughout my cloud engineering journey.

> **Discipline means verifying every environment before working on it.**  
> **Progress comes from mastering the fundamentals before chasing advanced topics. 🚀**