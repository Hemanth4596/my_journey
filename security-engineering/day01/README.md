# 🐧 Day 1 - Linux Permissions, ACLs, SUID & Capabilities

**📅 Date:** July 19, 2026  
**🎯 Goal:** Understand Linux Discretionary Access Control (DAC), master ownership rules, extend permissions using ACLs, demonstrate the danger of SUID, and implement secure capability-based privileges.

---

# 📸 Screenshots Taken Today

- 📷 [Basic Permissions](screenshots/Basic-Permissions.png)
- 📷 [Ownership Rules](screenshots/Ownership-Rules.png)
- 📷 [ACL Implementation](screenshots/ACL-Implementation.png)
- 📷 [SUID Demonstration](screenshots/SUID-Demonstration.png)
- 📷 [Capabilities Practice](screenshots/Capabilities-Practice.png)

---

# 📖 What I Learned Today

## 1. Basic Permissions (rwx & Octal Values)

Every file has **three permission sets**:

- User (Owner)
- Group
- Others

Each permission consists of:

| Permission | Value |
|------------|------:|
| Read (r) | 4 |
| Write (w) | 2 |
| Execute (x) | 1 |

### Example

`640`

```
rw-r-----
```

- User = 6 (Read + Write)
- Group = 4 (Read)
- Others = 0 (No permissions)

### Commands

```bash
echo "My password is 45962525" > secret.txt
chmod 640 secret.txt
ls -l secret.txt
```

Output

```text
-rw-r----- 1 attacker attacker 24 Jul 19 04:51 secret.txt
```

---

# 2. Ownership (chown) – The Root Rule

Only the **root user** can change ownership of a file to another user.

### Without sudo

```bash
chown root:root secret.txt
```

Output

```text
chown: changing ownership of 'secret.txt': Operation not permitted
```

### With sudo

```bash
sudo chown root:root secret.txt
ls -l secret.txt
```

Output

```text
-rw-r----- 1 root root 24 Jul 19 04:51 secret.txt
```

Trying to take ownership back:

```bash
chown $USER:$USER secret.txt
```

Output

```text
Operation not permitted
```

---

# 3. ACLs (Access Control Lists)

ACLs allow permissions for **specific users** without changing owner or group.

### Grant read permission

```bash
sudo setfacl -m u:$USER:r secret.txt
```

### View ACL

```bash
getfacl secret.txt
```

Output

```text
# file: secret.txt
# owner: root
# group: root

user::rw-
user:attacker:r--
group::r--
mask::r--
other::---
```

Reading the file

```bash
cat secret.txt
```

Output

```text
My password is 45962525
```

---

# 4. SUID (Set User ID)

SUID makes a program execute with the **owner's privileges**, not the user's.

If the owner is **root**, the program runs as **root**.

### Source Code

```c
#include <stdio.h>
#include <unistd.h>

int main() {
    printf("Real User: %d\n", getuid());
    printf("Effective User: %d\n", geteuid());
    return 0;
}
```

### Compile

```bash
gcc whoami.c -o whoami
```

### Make Root Owned

```bash
sudo chown root:root whoami
```

### Enable SUID

```bash
sudo chmod u+s whoami
```

Check permissions

```bash
ls -l whoami
```

Output

```text
-rwsr-xr-x 1 root root ...
```

Run program

```bash
./whoami
```

Output

```text
Real User: 1000
Effective User: 0
```

⚠️ One vulnerability inside a SUID program can result in full root compromise.

---

# 5. Linux Capabilities

Instead of giving **full root access**, Linux Capabilities provide only the permissions required.

Example:

```
cap_net_raw
```

Allows sending raw network packets without full root privileges.

### Copy ping

```bash
cp /usr/bin/ping ./myping
```

### Remove SUID

```bash
sudo chmod u-s myping
```

### Test

```bash
./myping -c 1 google.com
```

Fails because there is no privilege.

### Add Capability

```bash
sudo setcap cap_net_raw+ep ./myping
```

Verify

```bash
getcap ./myping
```

Output

```text
./myping cap_net_raw+ep
```

Run again

```bash
./myping -c 1 google.com
```

Output

```text
PING works successfully.
```

Capabilities follow the **Principle of Least Privilege**, making them much safer than SUID.

---

# ❌ Mistakes I Made Today

| # | Mistake | Reason | Fix |
|---|---------|--------|-----|
| 1 | `echo"My password` | Missing space | `echo "My password"` |
| 2 | `sudo setfacl-m` | Missing space | `sudo setfacl -m` |
| 3 | VM had no Internet | VirtualBox Adapter was Internal Network | Switched Adapter to NAT |
| 4 | Broken Ubuntu clone | Corrupted repositories | Installed fresh Ubuntu |
| 5 | `setcap -r` error | Binary had SUID instead of capabilities | Removed SUID using `chmod u-s` |

---

# 🐛 Errors I Faced

| Error | Meaning | Solution |
|--------|---------|----------|
| `setfacl: command not found` | ACL package missing | `sudo apt install acl -y` |
| Temporary failure resolving archive.ubuntu.com | DNS/Network issue | Switched VM to NAT and added DNS |
| `Operation not permitted` | Ownership change without root | Used `sudo` |
| `File has no capability to remove` | Binary had no capabilities | Removed SUID and reapplied capability |

---

# 📝 Commands Practiced

## File Permissions

```bash
echo "My password is 45962525" > secret.txt

chmod 640 secret.txt

ls -l secret.txt
```

---

## Ownership

```bash
sudo chown root:root secret.txt

ls -l secret.txt
```

---

## ACL

```bash
sudo setfacl -m u:$USER:r secret.txt

getfacl secret.txt

cat secret.txt
```

---

## Compile SUID Program

```bash
gcc whoami.c -o whoami

sudo chown root:root whoami

sudo chmod u+s whoami

./whoami
```

---

## Linux Capabilities

```bash
cp /usr/bin/ping ./myping

sudo chmod u-s myping

./myping -c 1 google.com

sudo setcap cap_net_raw+ep ./myping

getcap ./myping

./myping -c 1 google.com
```

---

# 💡 Important Rules

- **r = 4**
- **w = 2**
- **x = 1**

Example:

```
640 = rw-r-----
```

Remember:

- Only **root** can reassign file ownership.
- ACLs provide **user-specific permissions**.
- SUID grants **all owner privileges**.
- Capabilities grant **only the required privilege**.
- Always verify your environment (network mode, DNS, Ubuntu version) before debugging.

---

# 🎯 Day 1 Summary

## ✅ What I Learned

- Linux file permissions (`chmod`)
- Ownership rules (`chown`)
- Access Control Lists (`setfacl`, `getfacl`)
- SUID and Effective User ID
- Linux Capabilities (`setcap`)
- Difference between SUID and Capabilities

---

## ❌ Mistakes

- Forgot spaces in commands
- Used a corrupted Ubuntu clone
- Confused SUID with Capabilities

---

# 🙏 Honest Reflection

Today was the first day of my Linux security deep dive.

I initially spent time troubleshooting a corrupted Ubuntu clone before deciding to start fresh. That decision saved significant time and reinforced an important lesson: **sometimes rebuilding is more efficient than endlessly debugging**.

Technically, I progressed from understanding standard Linux permissions (`rwx`) to more advanced access control mechanisms such as ACLs, SUID, and Linux Capabilities. Seeing a program execute with an **Effective UID of 0** clearly demonstrated why SUID binaries require careful auditing. Learning Linux Capabilities also showed how the Principle of Least Privilege provides a much safer alternative by granting only the permissions an application actually needs.

Every mistake—from simple command syntax errors to VM networking issues—became a learning opportunity rather than a setback.

> **Discipline is showing up every day.  
> Progress comes from understanding every mistake, fixing it correctly, and moving forward. 🚀**
