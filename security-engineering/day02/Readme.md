# 🔒 Day 2 - Linux Capabilities (Replacing SUID with Fine-Grained Privileges)

**📅 Date:** July 20, 2026  
**🎯 Role:** Cloud Security Engineering  
**🎯 Goal:** Understand Linux Capabilities, investigate unexpected system behavior, and learn why modern Linux systems often avoid SUID for networking utilities.

---

# 📸 Screenshots Taken Today

- 📷 [SUID Demonstration](screenshots/SUID-Works.png)
- 📷 [Restricted Environment](screenshots/Security-Audit-Check.png)
- 📷 [Capability Applied](screenshots/The-Baseline.png)
- 📷 [Security Audit](screenshots/2.2.3.png)

---

# 📖 Objective

Today's goal was to understand why Linux Capabilities are considered a safer alternative to SUID binaries.

Instead of blindly following a lab, I investigated how my Ubuntu system actually behaved and learned how kernel configuration can change security behavior.

---

# 🧠 Expected Lab Behaviour

The planned experiment was:

```
Normal Binary
      │
      ▼
❌ Permission Denied

      │
Add SUID
      ▼

✅ Works (Runs as root)

      │
Remove SUID
      ▼

❌ Permission Denied

      │
Grant CAP_NET_RAW
      ▼

✅ Works (Least Privilege)
```

The idea is simple:

- SUID grants **all root privileges**
- Capabilities grant **only the privilege required**

---

# 🤔 What Actually Happened

The lab did **not** behave as expected.

```
cp /usr/bin/ping ./myping

./myping -c 1 google.com
```

Output:

```
PING ...
0% packet loss
```

Even after removing SUID:

```bash
chmod u-s ./myping
```

the command still worked.

That immediately raised a question:

> **Why does the binary still work after removing all obvious privileges?**

---

# 🔍 Root Cause Investigation

Instead of assuming the lab was wrong, I investigated the operating system.

Checking the kernel configuration:

```bash
cat /proc/sys/net/ipv4/ping_group_range
```

Output:

```text
0 2147483647
```

This explained everything.

Ubuntu allows every user group to create ICMP echo sockets.

As a result:

- No SUID required
- No capability required
- Ping works normally

---

# ⚙️ Understanding the Security Layers

Today's biggest lesson was that Linux security is layered.

```
Application
      │
      ▼
File Permissions
(SUID / Capabilities)
      │
      ▼
Kernel Security Policies
(sysctl)
      │
      ▼
Linux Kernel
```

Changing file permissions does **not** always change system behavior if a kernel policy already allows the operation.

---

# 🛠 Reproducing the Intended Lab

To observe the expected behavior, I temporarily restricted the kernel policy.

```bash
sudo sysctl -w net.ipv4.ping_group_range="0 0"
```

Now the binary behaved exactly as expected.

Without SUID or capabilities:

```
Operation not permitted
```

After granting the capability:

```bash
sudo setcap cap_net_raw+ep ./myping
```

```
PING ...
```

The binary worked again without requiring root privileges.

Finally, I restored the default configuration:

```bash
sudo sysctl -w net.ipv4.ping_group_range="0 2147483647"
```

---

# 🔍 Security Audit

Audited existing privileged binaries.

```bash
ls -l /usr/bin/passwd
```

Observed:

```
-rwsr-xr-x
```

The `s` bit indicates that `passwd` executes with the owner's privileges.

Examined process capabilities:

```bash
capsh --print
```

Observed:

```
Current: =
Current IAB:
```

This indicates my current shell had **no special Linux capabilities**, which is expected for an unprivileged user session.

---

# 📝 Useful Commands

```bash
getcap /bin/ping

getcap -r /usr/bin /usr/sbin

capsh --print

setcap cap_net_raw+ep ./myping

chmod u-s ./myping

cat /proc/sys/net/ipv4/ping_group_range
```

---

# ❌ Mistakes I Made

| Mistake | What I Learned |
|----------|----------------|
| Assumed the lab would behave exactly as documented | Production systems often have different defaults. |
| Initially thought SUID removal had failed | The kernel policy (`ping_group_range`) was allowing the operation. |
| Focused only on file permissions | Linux security also depends on kernel configuration. |
| Expected `capsh --print` to display capabilities | My shell correctly had none because it was running as an ordinary user. |

---

# 💡 Key Takeaways

- Capabilities implement the Principle of Least Privilege.
- SUID grants complete privileges and should be used sparingly.
- Kernel configuration can override assumptions made during security labs.
- Always investigate unexpected behavior instead of assuming a command is wrong.
- Production environments should be audited rather than assumed.

---

# 🎯 Skills Learned

- Linux Capabilities
- SUID
- Security Auditing
- Kernel sysctl Configuration
- Principle of Least Privilege
- Capability Inspection
- Production Troubleshooting

---

# 🙏 Honest Reflection

Today reminded me that real systems rarely behave exactly like textbook examples.

When my experiment didn't produce the expected result, I could have simply captured screenshots and moved on. Instead, I investigated why it behaved differently.

That investigation led me to discover `ping_group_range`, a kernel configuration that fundamentally changed the behavior of the lab.

The biggest lesson wasn't how to run `setcap`.

It was learning that effective security engineering begins with understanding the system's current state before making assumptions.

Today's mindset was:

1. Observe the behavior.
2. Verify the configuration.
3. Understand the root cause.
4. Apply the appropriate security control.

> **"Security isn't about memorizing commands—it's about understanding why the system behaves the way it does."** 🔒