# 🔒 Day 3 - Access Control Lists (ACLs) & Linux Capability Bounding Set

**📅 Date:** July 28, 2026  
**🎯 Role:** Cloud Security Engineering  
**🎯 Goal:** Learn how Linux Access Control Lists (ACLs) extend traditional file permissions, understand the ACL Mask, explore Default ACL inheritance, and investigate the Linux Capability Bounding Set.

---

# 📸 Screenshots Taken Today

- 📷 [Granting ACL Permissions-1](screenshots/1.1.png)
- 📷 [Granting ACL Permissions-2](screenshots/1.0.png)
- 📷 [Verifying ACL Access](screenshots/3.0.3.png)
- 📷 [ACL Mask Demonstration](screenshots/3.00.png)
- 📷 [Default ACL Inheritance](screenshots/4.00.png)
- 📷 [Capability Bounding Set](screenshots/5.00.png)

---

# 📖 What I Learned Today

## 1. Why ACLs Exist

Traditional Linux permissions only support:

- Owner
- Group
- Others

This works well for simple access control but becomes limiting when multiple individual users require different permissions.

Access Control Lists (ACLs) solve this problem by allowing permissions to be assigned directly to specific users or groups without changing ownership.

---

## 2. Granting User-Specific Permissions

Granted read/write access to a specific user.

```bash
setfacl -m u:testuser:rw plan.txt
```

Verified using:

```bash
getfacl plan.txt
```

Result:

```
user:testuser:rw-
```

Unlike `chmod`, ACLs provide fine-grained access without modifying file ownership.

---

## 3. Understanding the ACL Mask

The **Mask** represents the maximum effective permissions granted to named users and groups.

Example:

```bash
setfacl -m m::r plan.txt
```

Although the ACL entry granted:

```
user:testuser:rw-
```

the effective permission became:

```
user:testuser:r--
```

because the Mask removed write permission.

Think of the Mask as the final permission filter before access is granted.

---

## 4. Default ACLs

ACLs can also be inherited automatically by newly created files.

Applied a Default ACL:

```bash
setfacl -m d:u:testuser:rwx acldemo/
```

Every new file created inside the directory inherited the configured permissions automatically.

Verified using:

```bash
getfacl acldemo/
```

This is particularly useful for shared project directories where permissions should remain consistent.

---

## 5. Linux Capability Bounding Set

Investigated Linux capabilities using:

```bash
capsh --print
```

and

```bash
cat /proc/self/status | grep Cap
```

Observed:

```
Current: =
Current IAB:
```

This indicates the current shell was running without any additional Linux capabilities.

The Bounding Set defines the maximum capabilities that a process can ever acquire, even after executing another program.

It acts as an upper security boundary enforced by the kernel.

---

# 📝 Commands Practiced

## ACL Management

```bash
setfacl -m u:testuser:rw plan.txt

getfacl plan.txt

setfacl -m m::r plan.txt

setfacl -m d:u:testuser:rwx acldemo/
```

---

## Capability Inspection

```bash
capsh --print

cat /proc/self/status | grep Cap
```

---

# 🌐 Cloud Security Engineering Relevance

ACLs are commonly used when:

- Multiple administrators require different access levels
- Shared application directories exist
- Service accounts require controlled file access
- Traditional owner/group permissions become insufficient

Linux Capabilities reduce the need for SUID binaries by granting only the privileges required by a process.

Both mechanisms follow the Principle of Least Privilege.

---

# ⚙️ ECE → Linux Bridge

| Linux Concept | Electronics Analogy |
|---------------|---------------------|
| ACL Entry | Programmable Logic Array (PLA) |
| ACL Mask | AND Gate / Output Enable |
| Default ACL | Configuration EEPROM |
| Capability Bounding Set | Hardware Permission Register |
| Capability Mask | Register Bitmask |

Instead of hardwired permission bits, ACLs behave like programmable logic where access rules can be configured dynamically.

---

# ❌ Mistakes I Made Today

| Mistake | Why It Happened | How I Fixed It |
|----------|-----------------|----------------|
| Expected ACL permissions to override everything | Didn't understand the ACL Mask | Learned that the Mask limits effective permissions. |
| Forgot to verify permissions after modification | Assumed the command worked | Used `getfacl` after every ACL change. |
| Initially confused Default ACLs with normal ACLs | Both use similar syntax | Learned that entries beginning with `d:` apply only to newly created files. |
| Expected `capsh --print` to list capabilities | My shell had none assigned | Understood that an empty Current set is normal for an unprivileged shell. |

---

# 🐛 Errors I Encountered

| Error | Cause | Resolution |
|--------|-------|-----------|
| Permission denied despite ACL entry | ACL Mask restricted permissions | Adjusted the Mask appropriately. |
| Default ACL not applied to existing files | Default ACLs affect only newly created files | Created new files to verify inheritance. |

---

# 💡 Key Takeaways

- ACLs provide fine-grained access control beyond `chmod`.
- The ACL Mask limits effective permissions.
- Default ACLs automatically propagate permissions to newly created files.
- Linux Capabilities reduce reliance on SUID binaries.
- The Capability Bounding Set acts as a security ceiling for every process.
- Always verify permissions using `getfacl` instead of assuming they were applied.

---

# 🎯 Skills Learned

- Access Control Lists (ACLs)
- ACL Masks
- Default ACL Inheritance
- Capability Inspection
- Capability Bounding Set
- Principle of Least Privilege
- Linux Permission Auditing

---

# 🚀 Next Steps

Continue exploring Linux security by learning:

- POSIX Capabilities in depth
- SELinux / AppArmor
- PAM (Pluggable Authentication Modules)
- User Namespaces
- Container Security

---

# 🙏 Honest Reflection

Today's lab showed that Linux permissions extend far beyond the familiar `rwx` model.

Initially, I assumed that granting an ACL entry was enough to provide access. After experimenting with the ACL Mask, I realized that effective permissions are determined by multiple layers working together.

I also explored the Capability Bounding Set and learned that Linux not only grants privileges—it also defines an upper limit on what a process can ever obtain.

The biggest lesson today was that security is layered. Ownership, ACLs, Masks, Capabilities, and kernel policies all interact to determine the final access decision.

> **"Good security isn't achieved by adding more permissions—it's achieved by granting only what is necessary."** 🔒