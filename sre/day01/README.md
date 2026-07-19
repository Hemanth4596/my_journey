# ⚙️ Day 1 - Linux Systems Deep Dive (`/proc`, `/sys`, `/dev`)

**📅 Date:** July 19, 2026  
**🎯 Goal:** Understand Linux virtual filesystems (`/proc`, `/sys`, `/dev`) and learn how SREs inspect a live Linux system without relying on graphical tools.

---

# 📸 Screenshots Taken Today

- 📷 [CPU Information](screenshots/Reading-the-CPU-&-Memory-Dashboard.png)
- 📷 [Kernel Version](screenshots/Checking-Kernel-Version-vs-Boot-Secrets.png)
- 📷 [Boot Parameters](screenshots/Checking-Kernel-Version-vs-Boot-Secrets.png)
- 📷 [MAC Address](screenshots/Finding-the-Hardware-ID-(MAC)-and-Disk-Driver.png)

---

# 📖 What I Learned Today

## 1. Everything is a File

One of Linux's core design principles is:

> **Everything is represented as a file.**

Instead of creating special APIs for hardware and kernel information, Linux exposes them through virtual files.

Examples:

| Path | Represents |
|------|------------|
| `/proc/cpuinfo` | CPU information |
| `/proc/meminfo` | Memory statistics |
| `/proc/version` | Kernel version |
| `/sys/class/net/` | Network devices |
| `/dev/sda` | Physical storage device |

Unlike regular files, these files are generated dynamically by the kernel and exist only while the system is running.

---

# 2. Understanding Linux Virtual Filesystems

Linux provides three important virtual filesystems.

| Directory | Purpose | Why It Matters |
|-----------|----------|----------------|
| **`/proc`** | Running processes and kernel information | Monitor system health |
| **`/sys`** | Hardware devices and kernel interfaces | Inspect hardware configuration |
| **`/dev`** | Device files | Communicate with physical hardware |

Together they provide a complete view of a running Linux system.

---

# 3. `/proc` – Inspecting the Running Kernel

The `/proc` filesystem provides live information generated directly by the kernel.

Useful files include:

- `/proc/cpuinfo`
- `/proc/meminfo`
- `/proc/version`
- `/proc/cmdline`

Unlike normal files, these are regenerated every time they are accessed.

---

# 4. `/sys` – Hardware Information

The `/sys` filesystem exposes hardware information through the Linux kernel.

Example:

```bash
cat /sys/class/net/eth0/address
```

Output:

```text
08:00:27:12:34:56
```

This displays the MAC address of the network interface.

---

# 5. `/dev` – Device Files

Every hardware device is represented as a file.

Example:

```bash
ls -l /dev/sda
```

Output:

```text
brw-rw---- 1 root disk 8,0
```

### Understanding Major & Minor Numbers

```
8,0
│ │
│ └── Minor Number → First disk
└──── Major Number → Disk driver
```

The kernel uses these numbers to route I/O requests to the correct device driver.

---

# 6. Process Inspection

Every running process has its own directory.

Example:

```bash
echo $$
```

Output:

```text
4823
```

This represents the current shell's Process ID (PID).

---

### Memory Usage

```bash
cat /proc/$$/status | grep VmRSS
```

Example:

```text
VmRSS:      5320 kB
```

`VmRSS` shows the amount of physical RAM currently used by the process.

This metric is commonly monitored while investigating memory leaks.

---

### Open File Descriptors

```bash
ls -la /proc/$$/fd
```

Output:

```text
0 -> stdin
1 -> stdout
2 -> stderr
```

This directory shows every file currently opened by the process.

---

# 7. Commands Practiced

## CPU Information

```bash
cat /proc/cpuinfo | head -20
```

---

## Memory Information

```bash
cat /proc/meminfo | head -10
```

---

## Kernel Version

```bash
cat /proc/version

uname -a
```

---

## Boot Parameters

```bash
cat /proc/cmdline
```

---

## Network Interface

```bash
cat /sys/class/net/eth0/address
```

---

## Device Information

```bash
ls -l /dev/sda
```

---

## Current Process

```bash
echo $$
```

---

## Process Memory

```bash
cat /proc/$$/status | grep VmRSS
```

---

## Open File Descriptors

```bash
ls -la /proc/$$/fd
```

---

## Install Essential SRE Tools

```bash
sudo apt install tmux vim -y
```

Installed:

- **tmux** → Terminal multiplexer
- **vim** → Text editor

---

# 🧠 ECE → Linux Bridge

My Electronics & Communication Engineering background helped me relate Linux internals to hardware concepts.

| Linux | ECE Concept |
|--------|-------------|
| `/proc/cpuinfo` | Reading CPU registers |
| `/proc/sys` | Memory-mapped configuration registers |
| `/sys` | Hardware bus inspection |
| `/dev` | Device interface |
| Major/Minor Numbers | Bus address + Device ID |

Viewing Linux through a hardware perspective made many concepts easier to understand.

---

# 🛠 Real-World SRE Use Cases

### Diagnosing Memory Leaks

Monitor:

```bash
cat /proc/<PID>/status
```

If `VmRSS` continuously increases without stabilizing, the process may be leaking memory.

---

### Debugging Boot Issues

Inspect:

```bash
cat /proc/cmdline
```

to verify kernel boot parameters.

---

### Hardware Verification

Check:

```bash
cat /sys/class/net/eth0/address
```

to verify the network interface and MAC address.

---

### Storage Troubleshooting

Inspect:

```bash
ls -l /dev/sda
```

to verify the correct storage device is present.

---

# 💡 Key Takeaways

- Linux exposes kernel data through virtual filesystems.
- `/proc` provides live kernel and process information.
- `/sys` exposes hardware managed by the kernel.
- `/dev` represents hardware devices as files.
- `VmRSS` is an important metric when investigating memory usage.
- Major and Minor numbers identify hardware drivers and devices.
- Reading from virtual filesystems is safe, while writing to them can change kernel behavior immediately.

---

# 🎯 Day Summary

## ✅ Skills Learned

- Linux virtual filesystems
- Process inspection
- Memory analysis
- Device management
- Hardware inspection
- Kernel information
- Boot parameter analysis
- File descriptor inspection

---

## 🚀 Tools Practiced

- `cat`
- `grep`
- `head`
- `ls`
- `uname`
- `tmux`
- `vim`

---

# 🙏 Reflection

Today's session helped me understand how Linux exposes its internal state without requiring specialized debugging tools.

Instead of treating the operating system as a black box, I learned how to inspect CPU details, memory usage, kernel configuration, hardware information, and process state directly from the terminal.

The most valuable lesson was realizing that Linux's virtual filesystems provide a live view of the running system. Knowing where to find this information is a foundational skill for system administration, infrastructure engineering, and Site Reliability Engineering.

Every command I practiced today is something that can be used during real-world production troubleshooting when there is no graphical interface available.

> **"Good SREs don't guess what the kernel is doing—they ask the kernel directly."** 🐧