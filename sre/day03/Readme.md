# ⚙️ Day 3 - Linux System Configuration (`/etc`)

**📅 Date:** July 28, 2026  
**🎯 Role:** Site Reliability Engineering (SRE)  
**🎯 Goal:** Explore the Linux `/etc` directory, understand how user identities, authentication, groups, hostname resolution, and the Name Service Switch (NSS) work together.

---

# 📸 Screenshots Taken Today

- 📷 [User Database (`/etc/passwd`)](screenshots/1.png)
- 📷 [Shadow Password File](screenshots/2.png)
- 📷 [Group Database](screenshots/3.png)
- 📷 [Hosts File](screenshots/4.png)
- 📷 [User & Group Lookup](screenshots/5.png)

---

# 📖 What I Learned Today

## 1. Understanding the `/etc` Directory

The `/etc` directory stores system-wide configuration files used by Linux services, authentication, networking, and user management.

Unlike `/proc` or `/sys`, these files exist on disk and persist across reboots.

Many critical Linux services depend on the configuration stored here.

---

# 2. Five Critical Configuration Files

| File | Purpose | Why It Matters |
|------|---------|----------------|
| `/etc/passwd` | User account database | Maps usernames to UIDs and login shells |
| `/etc/shadow` | Password hashes and account policies | Stores authentication information securely |
| `/etc/group` | Group database | Controls shared permissions |
| `/etc/nsswitch.conf` | Name Service Switch configuration | Determines how Linux resolves users, groups, and hosts |
| `/etc/hosts` | Static hostname mappings | Local hostname resolution without DNS |

---

# 3. Understanding `/etc/passwd`

Each line follows this format:

```text
username:x:UID:GID:GECOS:home:shell
```

Example:

```text
hemanth:x:1000:1000:Hemanth:/home/hemanth:/bin/bash
```

Field breakdown:

| Field | Description |
|--------|-------------|
| Username | Login name |
| x | Password stored inside `/etc/shadow` |
| UID | User ID |
| GID | Primary Group ID |
| GECOS | User information |
| Home Directory | User's home |
| Login Shell | Default shell |

The Linux kernel identifies users using **UIDs**, not usernames.

---

# 4. Understanding `/etc/shadow`

The shadow file stores password hashes and password policies.

Example format:

```text
username:$y$...:last:min:max:warn:inactive:expire:reserved
```

Important fields:

- Password hash
- Last password change
- Minimum password age
- Maximum password age
- Warning period
- Account expiration

Special values:

```
!
*
```

indicate that the account is locked.

Only the **root** user can read this file.

---

# 5. Understanding `/etc/group`

Groups simplify permission management.

Example:

```text
sudo:x:27:hemanth
```

This indicates:

- Group name
- Group password placeholder
- Group ID
- Members

Rather than assigning permissions individually, Linux commonly assigns permissions to groups.

---

# 6. Name Service Switch (`/etc/nsswitch.conf`)

Linux doesn't automatically know where to search for users.

That decision is configured in:

```text
/etc/nsswitch.conf
```

Example:

```text
passwd: files systemd

group: files systemd

shadow: files
```

Meaning:

```
Application

      │

      ▼

glibc

      │

      ▼

nsswitch.conf

      │

      ▼

files → LDAP → NIS → systemd
```

The order determines where Linux searches first.

---

# 7. Hostname Resolution

The local hostname database lives inside:

```text
/etc/hosts
```

Example:

```text
127.0.0.1 localhost

192.168.1.20 webserver
```

Entries here override DNS.

This is commonly used during troubleshooting and testing.

---

# 📝 Commands Practiced

## View User Database

```bash
cat /etc/passwd
```

---

## View Group Database

```bash
cat /etc/group
```

---

## View Shadow File

```bash
sudo cat /etc/shadow
```

---

## Display NSS Configuration

```bash
cat /etc/nsswitch.conf
```

---

## View Hosts File

```bash
cat /etc/hosts
```

---

## Display Current User Information

```bash
id
```

---

## Lookup User Information

```bash
getent passwd hemanth
```

---

## Lookup Group Information

```bash
getent group sudo
```

---

# 🌐 SRE Relevance

Understanding `/etc` is essential for troubleshooting production systems.

Common operational tasks include:

- Why can't a user log in?
- Why isn't group membership applied?
- Why does hostname resolution fail?
- Why is authentication using LDAP instead of local files?
- Why is a service running under the wrong user?

Most of these questions begin with inspecting configuration inside `/etc`.

---

# ⚙️ ECE → Linux Bridge

| Linux Component | Electronics Analogy |
|----------------|---------------------|
| `/etc/passwd` | Device Address Table |
| UID | Hardware Address |
| Username | Human-readable Label |
| `/etc/shadow` | Secure Key Storage |
| `/etc/group` | Shared Bus |
| `/etc/nsswitch.conf` | Address Decoder |
| `/etc/hosts` | Local Routing Table |

The kernel works primarily with numeric IDs, just as hardware uses addresses rather than symbolic names.

The C library (`glibc`) performs the translation from human-readable names to numeric identifiers.

---

# ❌ Mistakes I Made Today

| Mistake | Why It Happened | How I Fixed It |
|----------|-----------------|----------------|
| Initially assumed usernames are stored inside the kernel | Linux internally uses UIDs | Learned that usernames are resolved through `glibc` and NSS. |
| Tried reading `/etc/shadow` without root privileges | The file is protected | Used `sudo` to inspect it. |
| Confused `/etc/passwd` with `/etc/shadow` | Both relate to users | Learned that passwords are stored separately for security. |
| Assumed `/etc/hosts` replaces DNS | It only overrides DNS locally | Understood how local name resolution works. |

---

# 🐛 Errors I Encountered

| Error | Cause | Resolution |
|--------|-------|-----------|
| Permission denied | Accessing `/etc/shadow` as a normal user | Used `sudo`. |
| User lookup confusion | Mixed up UID and username | Verified using `id` and `getent`. |

---

# 💡 Key Takeaways

- `/etc/passwd` stores user account information.
- `/etc/shadow` stores password hashes securely.
- `/etc/group` manages group memberships.
- `/etc/nsswitch.conf` controls identity lookup order.
- `/etc/hosts` provides local hostname resolution.
- Linux internally works with UIDs and GIDs rather than usernames.
- `glibc` translates numeric IDs into human-readable names.

---

# 🎯 Skills Learned

- Linux User Management
- Authentication Files
- Group Management
- Name Service Switch (NSS)
- Hostname Resolution
- UID & GID Concepts
- Identity Lookup

---

# 🚀 Next Steps

Continue exploring Linux identity management by learning:

- PAM (Pluggable Authentication Modules)
- LDAP
- Active Directory Integration
- SSSD
- SSH Authentication
- sudo Configuration

---

# 🙏 Honest Reflection

Today's lab helped me understand that Linux separates **identity**, **authentication**, and **authorization** into different configuration files.

Initially, I thought usernames were what the kernel used internally. After exploring `/etc/passwd`, `id`, and `getent`, I realized the kernel only understands numeric UIDs and GIDs. Human-readable usernames are translated by the C library (`glibc`) according to the lookup rules defined in `nsswitch.conf`.

This separation makes Linux flexible enough to authenticate users locally, through LDAP, or through other identity services without changing applications.

The biggest lesson today was that system reliability starts with understanding how Linux resolves identities before any authentication or authorization decisions are made.

> **"The kernel knows numbers. Users know names. Linux bridges the two."** ⚙️🐧