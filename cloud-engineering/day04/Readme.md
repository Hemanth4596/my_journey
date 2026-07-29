# ☁️ Day 4 - Text Processing, Job Control & Python Automation

**📅 Date:** July 29, 2026  
**🎯 Role:** Cloud Engineering  
**🎯 Goal:** Learn Linux text-processing utilities, process/job control, web utilities, and improve Python automation with exception handling and persistent CSV logging.

---

# 📸 Screenshots Taken Today

- 📷 [Text Processing (`cut`, `awk`, `sed`)](screenshots/1.png)
- 📷 [Sort, Uniq & Tee](screenshots/2.png)
- 📷 [Watch & Curl](screenshots/3.png)
- 📷 [Job Control](screenshots/4.png)

---

# 📖 What I Learned Today

## 1. Text Processing

Linux treats text as structured data that can be transformed using command-line tools.

### `cut`

Extracts specific fields from delimited data.

```bash
cut -d: -f1 /etc/passwd
```

Used to extract usernames from `/etc/passwd`.

---

### `awk`

Processes structured text using pattern-action rules.

```bash
awk -F: '{print $1, $3}' /etc/passwd
```

Displayed:

- Username
- UID

without modifying the original file.

---

### `sed`

Performs stream editing.

```bash
sed 's/root/ROOT/g'
```

Replaces every occurrence of `root` with `ROOT`.

Unlike a text editor, `sed` processes data as it flows through a pipeline.

---

## 2. Sorting & Data Pipelines

Sorted shell entries:

```bash
cut -d: -f7 /etc/passwd | sort | uniq -c
```

This demonstrated how multiple small utilities can solve larger problems when combined.

---

### `tee`

```bash
df -h | tee disk_snapshot.txt
```

Displayed the output on the terminal while simultaneously writing it to a file.

Useful when collecting diagnostics during troubleshooting.

---

### `xargs`

```bash
ls dummy*.txt | xargs -I {} echo "Found: {}"
```

Converted standard input into command-line arguments.

A common tool for bulk file operations.

---

## 3. Monitoring & Web Utilities

### `watch`

```bash
watch -n 2 df -h
```

Repeatedly executes a command at fixed intervals.

Useful for observing changing system metrics.

---

### `curl`

```bash
curl -I https://google.com
```

Retrieved HTTP response headers.

Frequently used for:

- Health checks
- API testing
- Debugging web services

---

### `wget`

```bash
wget https://example.com
```

Downloads files directly from remote servers.

---

## 4. Job Control

Linux shells support managing multiple running processes.

Started a background task:

```bash
ping 8.8.8.8 > ping.log &
```

Inspected jobs:

```bash
jobs
```

Returned the process to the foreground:

```bash
fg
```

Detached long-running processes:

```bash
nohup ./script.sh &
```

and

```bash
disown
```

These commands are useful when working on remote servers over SSH.

---

## 5. Python Automation

Improved my health-check script.

The updated script now:

- Performs HTTP health checks
- Uses `try/except`
- Records timestamps
- Measures response status
- Stores every execution in a CSV file

Output:

```
health_log.csv
```

Each execution appends:

- Timestamp
- URL
- HTTP Status
- Response Time

This creates a simple historical record of service health.

---

# 📝 Commands Practiced

## Text Processing

```bash
cut -d: -f1 /etc/passwd

awk -F: '{print $1, $3}' /etc/passwd

sed 's/root/ROOT/g'

sort

uniq
```

---

## Data Pipelines

```bash
tee

xargs
```

---

## Monitoring

```bash
watch

curl

wget
```

---

## Job Control

```bash
jobs

bg

fg

nohup

disown
```

---

## Python

```bash
python3 health_check.py
```

---

# 🌐 Cloud Engineering Relevance

Cloud Engineers routinely use these utilities to:

- Parse configuration files
- Analyze logs
- Monitor systems
- Test web services
- Build automation
- Run long-lived background tasks

The Python health-check script demonstrates the foundation of service monitoring by collecting availability data in a structured format.

---

# ⚙️ ECE → Linux Bridge

| Linux Concept | Electronics Analogy |
|---------------|---------------------|
| `awk` | Finite State Machine (FSM) |
| Pipe (`|`) | Data Bus |
| `watch` | Timer Interrupt |
| `tee` | Signal Splitter |
| `sort` | Hardware Sorting Network |
| Background Jobs | Concurrent Hardware Processes |

Thinking in terms of data flow made these Linux tools easier to understand.

---

# ❌ Mistakes I Made Today

| Mistake | Why It Happened | How I Fixed It |
|----------|-----------------|----------------|
| Initially confused `cut` and `awk` | Both manipulate text | Learned that `cut` extracts fields while `awk` performs programmable processing. |
| Forgot the field separator (`-F:`) in `awk` | `/etc/passwd` is colon-separated | Added `-F:` to correctly parse the file. |
| Expected `tee` to replace redirection | Misunderstood its purpose | Learned that `tee` duplicates output instead of redirecting it. |
| Forgot to terminate a background job | Process continued running | Used `jobs` followed by `kill %1`. |
| Health-check script exited on connection failures | Missing exception handling | Added `try/except` blocks to handle network errors gracefully. |

---

# 🐛 Errors I Encountered

| Error | Cause | Resolution |
|--------|-------|-----------|
| Incorrect `awk` output | Wrong field separator | Used `-F:` |
| HTTP request failure | Network or server issue | Handled exceptions in Python |
| Background process left running | Forgot to stop the job | Used `kill` after verifying with `jobs` |

---

# 💡 Key Takeaways

- Linux pipelines allow small tools to solve complex problems together.
- `awk` is significantly more powerful than `cut`.
- `tee` is useful when diagnostics need to be both displayed and saved.
- Job control is essential when managing long-running processes.
- Python exception handling makes automation more resilient.
- Persistent logging provides historical data for troubleshooting.

---

# 🎯 Skills Learned

- Text Processing
- Data Pipelines
- Job Control
- HTTP Testing
- Background Processes
- Python Exception Handling
- CSV Logging
- Basic Monitoring Automation

---

# 🚀 Next Steps

Continue expanding the monitoring script by adding:

- CPU usage
- Memory usage
- Disk usage
- JSON logging
- Email alerts
- Multiple endpoint monitoring

---

# 🙏 Honest Reflection

Today's session changed how I think about the Linux terminal.

Instead of seeing commands as isolated utilities, I began treating them as building blocks that can be combined into reusable data-processing pipelines. Commands like `cut`, `awk`, `sort`, and `tee` each perform one task well, but together they become powerful tools for analyzing system data.

I also improved my Python automation by adding exception handling and persistent CSV logging. While the script is still simple, it is more reliable than my earlier versions because it continues running even when requests fail and records each execution for later analysis.

Crossing the 50-command milestone wasn't about memorizing commands—it was about understanding how they fit together to solve operational problems.

> **"The terminal becomes powerful when commands are connected into workflows rather than used in isolation."** ☁️🐧