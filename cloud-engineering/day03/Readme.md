# ☁️ Day 3 - Process & Resource Monitoring

**📅 Date:** July 28, 2026  
**🎯 Role:** Cloud Engineering  
**🎯 Goal:** Learn how to inspect processes, monitor system resources, troubleshoot networking, analyze logs, and automate system telemetry using Python.

---

# 📸 Screenshots Taken Today

- 📷 [Process Monitoring-1](screenshots/1.1.png)
- 📷 [Process Monitoring-2](screenshots/1.2.png)
- 📷 [Memory & Disk Usage](screenshots/3.png)
- 📷 [Networking & Listening Ports](screenshots/4.png)
- 📷 [Kernel & System Logs](screenshots/5.png)
---

# 📖 What I Learned Today

## 1. Process Monitoring

Linux keeps information about every running process inside the kernel's process table.

### Snapshot of Running Processes

```bash
ps aux
```

Useful for:

- Checking running processes
- Finding high CPU usage
- Finding high memory usage
- Viewing process owners

---

### Real-Time Monitoring

```bash
top
```

Unlike `ps`, `top` continuously refreshes.

This allows me to observe:

- CPU utilization
- Memory usage
- Running processes
- Load average

---

## 2. Memory Monitoring

```bash
free -h
```

Displays:

- Total RAM
- Used RAM
- Free RAM
- Swap Memory

Using `-h` makes the output human-readable.

---

## 3. Disk Monitoring

Filesystem usage:

```bash
df -hT
```

Shows:

- Filesystem
- Disk Size
- Used Space
- Available Space
- Filesystem Type

---

Directory usage:

```bash
du -sh
```

Useful when locating directories consuming excessive storage.

---

## 4. Network Troubleshooting

Display network interfaces:

```bash
ip addr show
```

List listening ports:

```bash
ss -tlnp
```

Test connectivity:

```bash
ping -c 3 8.8.8.8
```

These commands are commonly used when troubleshooting unreachable services.

---

## 5. System Logs

Kernel messages:

```bash
dmesg | tail -15
```

Recent system logs:

```bash
journalctl --since "10 min ago"
```

Logs are often the first place to investigate when diagnosing production failures.

---

## 6. Python Automation

Created a telemetry collection script.

```bash
python3 sys_snapshot.py
```

The script collected:

- Hostname
- Uptime
- Load Average
- Memory Usage
- Disk Usage

and stored the information inside:

```
system_snapshot.json
```

This demonstrates how Python can automate routine system inspection tasks.

---

# 📝 Commands Practiced

## Process Monitoring

```bash
ps aux | head -10

top
```

---

## Memory & Storage

```bash
free -h

df -hT

du -sh
```

---

## Networking

```bash
ip addr show

ss -tlnp

ping -c 3 8.8.8.8
```

---

## Logs

```bash
dmesg | tail -15

journalctl --since "10 min ago"
```

---

## Automation

```bash
python3 sys_snapshot.py
```

---

# 🌐 Cloud Engineering Relevance

Every cloud virtual machine eventually needs troubleshooting.

The same commands practiced today are used by Cloud Engineers to answer questions like:

- Why is the VM slow?
- Which process is consuming CPU?
- Is memory exhausted?
- Is disk space full?
- Is the service listening on the expected port?
- Did the kernel report any hardware or driver issues?
- What changed in the last few minutes?

Cloud monitoring platforms such as Google Cloud Monitoring and Prometheus collect these same metrics automatically.

Today's Python script is a simplified version of a monitoring agent.

---

# ⚙️ ECE → Linux Bridge

| Linux Concept | Electronics Analogy |
|---------------|---------------------|
| Process Table | Scheduler Queue |
| CPU Scheduler | Round-Robin Arbiter |
| `top` | Logic Analyzer |
| Memory Usage | RAM Occupancy |
| Network Interface | Communication Bus |
| System Logs | Event Recorder |
| Telemetry JSON | Sensor Data Packet |

My ECE background helped me relate operating system scheduling and monitoring to hardware arbitration and embedded diagnostics.

---

# ❌ Mistakes I Made Today

| Mistake | Why It Happened | How I Fixed It |
|----------|-----------------|----------------|
| Initially confused `ps` and `top` | Both display running processes but behave differently | Learned that `ps` is a snapshot while `top` updates continuously. |
| Forgot the `-h` option with `free` and `df` | Output was difficult to read in bytes | Used `-h` for human-readable units. |
| Tried reading the complete `dmesg` output | Produced too much information | Used `tail` to inspect only recent messages. |
| Forgot to save the Python telemetry output | Script executed but no file was generated | Corrected the script to write `system_snapshot.json`. |
| Expected `journalctl` to show only recent logs | It displayed a large number of entries | Used `--since "10 min ago"` to narrow the search. |

---

# 🐛 Errors I Encountered

| Error | Cause | Resolution |
|--------|-------|-----------|
| Large command output | Too much information displayed | Filtered output using `head`, `tail`, and command options. |
| Difficulty locating processes | Many processes running simultaneously | Sorted and monitored using `top`. |
| JSON output not generated | File writing logic missing | Updated Python script to save telemetry correctly. |

---

# 💡 Key Takeaways

- `ps` provides a snapshot of running processes.
- `top` provides live system monitoring.
- `free` is the quickest way to inspect memory pressure.
- `df` and `du` identify storage issues.
- `ss` replaces many older networking tools for socket inspection.
- `journalctl` is essential on systemd-based Linux systems.
- Python can automate repetitive operational tasks.

---

# 🎯 Skills Learned

- Process Monitoring
- Resource Monitoring
- Linux Networking
- Kernel Log Analysis
- System Log Investigation
- Python Automation
- JSON Telemetry
- Basic Operational Troubleshooting

---

# 🚀 Next Steps

Continue building automation by collecting:

- CPU utilization
- Disk I/O
- Network throughput
- Running services
- Process statistics

and exporting them into structured JSON suitable for dashboards.

---

# 🙏 Honest Reflection

Today felt much closer to real infrastructure engineering than previous labs.

Instead of learning isolated Linux commands, I learned how to answer operational questions systematically:

- Is the CPU overloaded?
- Is memory exhausted?
- Is disk space available?
- Is the network functioning?
- Are services listening?
- Do the logs explain the problem?

I also took the first step toward automation by writing a Python script that collects telemetry instead of manually checking each command.

The biggest lesson wasn't memorizing commands—it was developing a repeatable troubleshooting workflow.

> **"Good Cloud Engineers don't memorize every command. They know where to look, what to verify, and how to automate the process."** ☁️🐧