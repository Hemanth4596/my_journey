# 🔒 Day 4 - SUID, SGID, Sticky Bit & Linux Capabilities

**📅 Date:** July 29, 2026  
**🎯 Role:** Cloud Security Engineering  
**🎯 Goal:** Understand Linux special permission bits (SUID, SGID, Sticky Bit), audit privilege escalation risks, and explore Linux Capabilities as a safer alternative to full root privileges.

---

# 📸 Screenshots Taken Today

- 📷 [SUID Binary Scan](screenshots/1.png)
- 📷 [SGID Binary Scan](screenshots/2.png)
- 📷 [Capability Inspection](screenshots/3.png)
- 📷 [Capability Drop Test](screenshots/4.png)

---

# 📖 What I Learned Today

## 1. Special Permission Bits

Linux provides three special permission bits in addition to the standard `rwx` permissions.

### SUID (Set User ID)

```bash
find / -perm /4000 -ls 2>/dev/null
```

When a SUID binary executes, it runs with the permissions of the file owner rather than the user launching it.

Common example:

```
/usr/bin/passwd
```

This allows ordinary users to update password information that only root can modify.

---

### SGID (Set Group ID)

```bash
find / -perm /2000 -ls 2>/dev/null
```

Files execute using the file's group privileges.

Directories automatically assign newly created files to the directory's group.

Useful for shared project directories.

---

### Sticky Bit

```bash
chmod +t shared_dir
```

Verified using:

```bash
ls -ld shared_dir
```

Example output:

```
drwxrwxrwt
```

With the Sticky Bit enabled:

- Users may create files.
- Users cannot delete files owned by others.
- Common example:

```
/tmp
```

---

# 2. Auditing Privileged Files

Searched for SUID binaries:

```bash
find / -perm /4000 -ls 2>/dev/null
```

Searched for SGID binaries:

```bash
find / -perm /2000 -ls 2>/dev/null
```

Searched for either:

```bash
find / -perm /6000 -ls 2>/dev/null
```

These commands are frequently used during security audits and penetration testing.

---

# 3. Linux Capabilities

Rather than granting complete root privileges, Linux can grant only the capability required.

Examined file capabilities:

```bash
getcap /usr/bin/ping
```

Observed process capabilities:

```bash
cat /proc/self/status | grep Cap
```

Decoded capability masks:

```bash
capsh --decode=<hex-mask>
```

This converted hexadecimal capability values into human-readable capability names.

---

# 4. Dropping Capabilities

Executed:

```bash
capsh --drop=cap_net_raw -- -c "ping -c1 localhost"
```

Removing `CAP_NET_RAW` prevented `ping` from creating raw sockets.

This demonstrated that capabilities can be removed individually without affecting unrelated privileges.

---

# 5. Understanding the Capability Pipeline

Linux maintains multiple capability sets for every process:

- Inheritable
- Permitted
- Effective
- Bounding
- Ambient

Each `exec()` calculates the new capability state according to kernel rules.

The Bounding Set defines the maximum capabilities a process may ever obtain.

---

# 📝 Commands Practiced

## Permission Auditing

```bash
find / -perm /4000 -ls

find / -perm /2000 -ls

find / -perm /6000 -ls
```

---

## Sticky Bit

```bash
chmod +t directory

ls -ld directory
```

---

## Capability Inspection

```bash
getcap

capsh --print

capsh --decode=<mask>

cat /proc/self/status | grep Cap
```

---

## Capability Testing

```bash
capsh --drop=cap_net_raw -- -c "ping -c1 localhost"
```

---

# 🌐 Cloud Security Engineering Relevance

Modern cloud platforms rely heavily on Linux capabilities to reduce attack surface.

Examples include:

- Kubernetes `securityContext.capabilities`
- Docker capability drops
- Container runtime hardening
- Least Privilege enforcement
- Image security scanning for unexpected SUID binaries

Many security benchmarks recommend removing unnecessary capabilities before deploying workloads.

---

# ⚙️ ECE → Linux Bridge

| Linux Concept | Electronics Analogy |
|---------------|---------------------|
| SUID | Master Override Switch |
| SGID | Shared Bus Controller |
| Sticky Bit | Write-Protect Logic |
| Capability Register | CPU Status Register |
| Bounding Set | Hardware Permission Mask |
| Capability Drop | Clearing Control Register Bits |

Just as processors expose privileged control bits through status registers, Linux exposes privileges through capability bitmasks that the kernel evaluates during program execution.

---

# ❌ Mistakes I Made Today

| Mistake | Why It Happened | How I Fixed It |
|----------|-----------------|----------------|
| Initially thought SUID and capabilities served the same purpose | Both elevate privileges | Learned that capabilities provide much finer control. |
| Forgot to suppress permission errors during `find` | System directories denied access | Redirected errors using `2>/dev/null`. |
| Expected dropping one capability to break every privileged program | Capabilities are independent | Learned each capability controls specific kernel operations. |
| Confused Sticky Bit with SGID | Both affect directory behavior | Understood that Sticky Bit protects deletion, while SGID controls group inheritance. |

---

# 🐛 Errors I Encountered

| Error | Cause | Resolution |
|--------|-------|-----------|
| Large number of "Permission denied" messages | Searching the entire filesystem | Used `2>/dev/null` to suppress expected errors. |
| `ping` failed after dropping `CAP_NET_RAW` | Raw socket capability removed | Confirmed this was the expected security behavior. |

---

# 💡 Key Takeaways

- SUID grants full owner privileges and should be used sparingly.
- SGID simplifies collaboration through shared group ownership.
- Sticky Bit protects shared directories from accidental deletion.
- Linux Capabilities implement the Principle of Least Privilege.
- The Bounding Set defines the maximum privileges a process can obtain.
- Security audits should regularly inspect SUID binaries and assigned capabilities.

---

# 🎯 Skills Learned

- SUID Auditing
- SGID Auditing
- Sticky Bit Management
- Linux Capabilities
- Capability Inspection
- Capability Bounding Set
- Least Privilege
- Security Hardening

---

# 🚀 Next Steps

Continue exploring Linux security by studying:

- Securebits
- Ambient Capabilities
- User Namespaces
- SELinux
- AppArmor
- seccomp
- Container Security Profiles

---

# 🙏 Honest Reflection

Today's session helped me understand that Linux privilege management is far more granular than simply being "root" or "not root."

By experimenting with SUID, SGID, Sticky Bit, and Linux Capabilities, I saw how the operating system provides multiple mechanisms to control access at different levels. The most valuable lesson was learning that capabilities allow individual privileges to be granted or removed without giving a process unrestricted administrative access.

I also learned how to audit privileged binaries and inspect capability masks—skills that are directly applicable when reviewing Linux hosts and container images for unnecessary privilege escalation risks.

The biggest takeaway was that effective security comes from minimizing privilege rather than maximizing it.

> **"Good security isn't about giving root access—it is about granting only the capabilities that are genuinely required."** 🔒