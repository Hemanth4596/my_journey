# ⚙️ Day 2 - Linux Systems Deep Dive (`/sys`, `/dev`, `/etc`)

**📅 Date:** July 27, 2026  
**🎯 Goal:** Understand Linux device nodes, the `/sys` hardware model, critical `/etc` configuration files, and build a persistent incident-response dashboard using `tmux`.

---

# 📸 Screenshots Taken Today

- 📷 [Hardware Tree-1 (`lsblk` & `stat`)](screenshots/1.1.png)
- 📷 [Hardware Tree-2 (`lsblk` & `stat`)](screenshots/1.2.png)
- 📷 [/sys Hardware Blueprint](screenshots/2.png)
- 📷 [Critical Configuration Files](screenshots/3.png)
- 📷 [Tmux Incident Dashboard](screenshots/4.png)
- 📷 [Linux Manual Pages](screenshots/5.png)

---

# 📖 What I Learned Today

# 1. Device Nodes & Major/Minor Numbers

Linux represents hardware devices using **device nodes** located inside `/dev`.

There are two main types of device files.

| Device Type | Purpose | Example |
|-------------|---------|---------|
| **Block Device (`b`)** | Reads and writes data in blocks | `/dev/sda` |
| **Character Device (`c`)** | Reads and writes one byte at a time | `/dev/tty` |

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
│ └── Minor Number → Specific storage device
└──── Major Number → Storage driver
```

The kernel uses these numbers to route every I/O request to the correct device driver.

---

# 2. Exploring the `/sys` Filesystem

The `/sys` filesystem exposes the Linux kernel's live hardware model.

Useful locations include:

| Path | Purpose |
|------|---------|
| `/sys/class/net/` | Network interfaces |
| `/sys/bus/pci/devices/` | PCI hardware tree |
| `/sys/block/sda/queue/` | Disk scheduling and queue information |

Unlike ordinary files, the contents of `/sys` are generated dynamically by the kernel.

---

# 3. Inspecting Network Hardware

Display the MAC address of a network interface.

```bash
cat /sys/class/net/eth0/address
```

Example Output:

```text
08:00:27:12:34:56
```

This information is commonly used to verify network hardware during server deployment and troubleshooting.

---

# 4. Storage Queue Information

Linux exposes storage tuning parameters through `/sys`.

Example:

```bash
ls /sys/block/sda/queue/
```

Useful settings include:

- Scheduler
- Read-ahead
- Queue depth
- Request merging

These parameters are often inspected when diagnosing storage performance issues.

---

# 5. The `/etc` Configuration Lifelines

Critical Linux configuration files are stored inside `/etc`.

| File | Purpose |
|------|---------|
| `/etc/hostname` | Stores the system hostname |
| `/etc/fstab` | Filesystem mount configuration |
| `/etc/passwd` | User account database |

A broken `/etc/fstab` configuration can prevent Linux from booting successfully and may drop the system into **Emergency Mode**.

---

# 6. Building an SRE Dashboard with `tmux`

Create a persistent session.

```bash
tmux new -s sre_dashboard
```

Split the window vertically.

```text
Ctrl-b %
```

### Left Pane

```bash
dmesg -w
```

Continuously displays live kernel messages.

---

### Right Pane

```bash
watch -n 1 'cat /proc/loadavg'
```

Displays the system load average every second.

This setup creates a simple but effective incident-response dashboard for monitoring a Linux server.

---

# 7. Understanding Linux Manual Sections

Linux manuals are divided into sections.

Configuration file documentation:

```bash
man 5 passwd
```

Command documentation:

```bash
man 1 passwd
```

| Manual Section | Purpose |
|---------------|---------|
| **man 1** | User commands |
| **man 5** | Configuration files |

Knowing the correct manual section helps quickly locate accurate documentation during troubleshooting.

---

# 8. Commands Practiced

## Device Information

```bash
ls -l /dev/sda
```

---

## Network Interface

```bash
cat /sys/class/net/eth0/address
```

---

## PCI Hardware

```bash
ls /sys/bus/pci/devices
```

---

## Storage Queue

```bash
ls /sys/block/sda/queue
```

---

## Hostname

```bash
cat /etc/hostname
```

---

## Filesystem Table

```bash
cat /etc/fstab
```

---

## User Database

```bash
cat /etc/passwd
```

---

## Create tmux Session

```bash
tmux new -s sre_dashboard
```

---

## Live Kernel Logs

```bash
dmesg -w
```

---

## Monitor System Load

```bash
watch -n 1 'cat /proc/loadavg'
```

---

## Linux Manual Pages

```bash
man 5 passwd

man 1 passwd
```

---

# 🧠 ECE → Linux Bridge

My Electronics & Communication Engineering background helped me understand Linux device management through familiar hardware concepts.

| Linux | ECE Concept |
|--------|-------------|
| Major Number | Chip Select Line |
| Minor Number | Device Sub-address |
| Device Driver | Peripheral Controller |
| `/dev/sda` | Memory-Mapped Device |
| Driver Lookup | Interrupt Vector Table |

Viewing Linux through an embedded systems perspective made device management much easier to understand.

---

# 🛠 Real-World SRE Use Cases

### Storage Troubleshooting

Inspect:

```bash
ls /sys/block/sda/queue
```

to investigate disk scheduling and queue configuration.

---

### Hardware Verification

Check:

```bash
cat /sys/class/net/eth0/address
```

to verify the correct network interface and MAC address.

---

### Boot Recovery

Inspect:

```bash
cat /etc/fstab
```

to verify filesystem mount configuration before rebooting.

---

### Incident Monitoring

Use:

```bash
tmux
```

to keep kernel logs and system load visible simultaneously during production incidents.

---

# 💡 Key Takeaways

- Linux represents hardware through device nodes inside `/dev`.
- Major and Minor numbers identify drivers and device instances.
- `/sys` provides a live view of hardware managed by the kernel.
- `/etc` stores critical system configuration files.
- `tmux` allows persistent monitoring sessions during incident response.
- `man 5` documents configuration files, while `man 1` documents commands.

---

# 🎯 Day Summary

## ✅ Skills Learned

- Linux device nodes
- Major & Minor numbers
- Hardware inspection with `/sys`
- Critical system configuration
- Storage queue inspection
- Terminal multiplexing
- Incident dashboard creation
- Linux manual sections

---

## 🚀 Tools Practiced

- `ls`
- `cat`
- `watch`
- `dmesg`
- `tmux`
- `man`
- `stat`

---

# 🙏 Reflection

Today's session changed the way I think about Linux hardware management.

Instead of seeing `/dev/sda` as just another file, I learned that it is an interface to a kernel device driver. I also explored how `/sys` exposes the kernel's live hardware model and how `/etc` stores the configuration that keeps a Linux system running.

Building my first `tmux` dashboard showed me how SREs monitor systems during real production incidents. Watching kernel logs in one pane while tracking system load in another demonstrated how powerful simple command-line tools can be.

Understanding these core Linux components has strengthened my foundation for System Reliability Engineering and prepared me to troubleshoot production systems with greater confidence.

> **"Good SREs don't just execute commands—they understand what the operating system is telling them."** 🐧