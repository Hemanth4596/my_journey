# 🔐 Day 2 — CSE: Inspect and Compare File Permissions

**🎯 Role/Track:** Cloud Security Engineering (CSE)  
**🎯 Goal:** Understand Linux file permissions and compare modes `600` and `640`.

---

# 📸 Screenshots Taken Today

**Screenshot status:** Pending — capture the real lab evidence.

- `screenshots/new.png` — Show `chmod 640`, `ls -l`, and `stat` verifying the final permission mode.

**Evidence required:**
- The permission change applied to `report.txt`.
- The symbolic permission string `-rw-r-----`.
- The numeric permission mode `640`.
- File owner and group information.

---

# 📖 What I Learned Today

## 1. Understanding Linux File Permissions

Linux file permissions control who can read, modify, or execute a file. The three permission classes are:

| Class | Description |
|---|---|
| Owner | The user who owns the file |
| Group | Users associated with the file's group |
| Others | All other users |

Linux represents basic permissions using these values:

| Permission | Symbol | Numeric Value |
|---|---|---:|
| Read | `r` | 4 |
| Write | `w` | 2 |
| Execute | `x` | 1 |
| No permission | `-` | 0 |

## 2. Understanding Permission Mode `640`

Linux combines permission values for each class.

- Owner: `6` = read + write (`4 + 2`)
- Group: `4` = read only
- Others: `0` = no permissions

The symbolic permission string for a regular file with mode `640` is:

```text
-rw-r-----
```

The initial `-` indicates a regular file. The remaining nine characters represent permissions for the owner, group, and others.

## 3. Difference Between `600` and `640`

| Permission Mode | Owner | Group | Others |
|---|---|---|---|
| `600` | Read, write | None | None |
| `640` | Read, write | Read only | None |

Both modes allow the owner to read and modify the file. Mode `640` additionally allows members of the file's group to read it.

Therefore, `600` is more restrictive than `640` because it does not grant group read access.

## 4. Understanding Permission Commands

| Command | Purpose |
|---|---|
| `chmod` | Changes file permissions |
| `ls -l` | Displays permissions and file details |
| `stat` | Displays file metadata, including permissions and ownership |
| `pwd` | Displays the current working directory |

The numeric permission reported by `stat` helps verify the actual mode rather than relying only on visual inspection.

## 5. Why File Permissions Matter in Cloud Security

Configuration files and credential-related files may contain sensitive information. Unnecessarily broad permissions can expose information to other local users.

Restricting file permissions helps reduce this risk. However, file permissions alone do not guarantee that credentials are secure.

Directory permissions behave differently from regular-file permissions. Execute permission on a directory generally allows traversal when other required access conditions are satisfied.

---

# 💻 Commands Practiced / Code Used

**Status:** Commands assigned for the lab; execution has not yet been confirmed.

## 1. Create the Lab Directory

```bash
mkdir -p ~/day-002-lab/cse
cd ~/day-002-lab/cse
```

- `mkdir -p` creates the required directory structure.
- `cd` moves into the lab directory.
- `~` represents the current user's home directory.

## 2. Create the Test File

```bash
printf 'Safe permission test\n' > report.txt
```

This writes test content to `report.txt`. The redirection operator `>` replaces existing contents if the file already exists, so this should be run only in the dedicated lab directory.

## 3. Inspect Initial Permissions

```bash
pwd
ls -l report.txt
stat -c 'mode=%A (%a) owner=%U group=%G' report.txt
```

- `pwd` verifies the working directory.
- `ls -l` displays the symbolic permission string and file details.
- `%A` displays symbolic permissions.
- `%a` displays numeric permissions.
- `%U` displays the owner username.
- `%G` displays the group name.

The initial permission mode depends on the system's defaults and `umask`.

## 4. Apply Permission Mode `640`

```bash
chmod 640 report.txt
```

This grants read/write permissions to the owner, read permission to the group, and no ordinary permissions to others.

## 5. Verify the Final Mode

```bash
ls -l report.txt
stat -c 'mode=%A (%a) owner=%U group=%G' report.txt
```

Expected permission information:

```text
-rw-r-----
mode=-rw-r----- (640) owner=your_username group=your_group
```

**Note:** The output above is illustrative, not captured terminal output. The owner and group values depend on the actual environment.

---

# 🧪 Hands-On Lab / Verification

## Objective

Create a separate test file, apply permission mode `640`, and compare it with mode `600`.

## Environment

- Ubuntu Bash in Windows Subsystem for Linux (WSL).

## Actions Performed

**Pending verification:** No terminal execution has been confirmed in this session.

Planned actions:

1. Create `~/day-002-lab/cse`.
2. Create the test file `report.txt`.
3. Inspect its initial permissions.
4. Apply permission mode `640`.
5. Verify the symbolic and numeric permission modes.
6. Confirm that the current user can still read the file.

## Verification Criteria

| Check | Expected Result | Status |
|---|---|---|
| Test file exists | `report.txt` | Pending |
| Numeric permission mode | `640` | Pending |
| Symbolic permission string | `-rw-r-----` | Pending |
| Owner can read the file | Reading succeeds | Pending |
| Screenshot evidence | Saved in `screenshots/` | Pending |

## Safety and Cleanup

- Work only with the dedicated test file.
- Do not modify permissions on files under `/etc`, `/proc`, `/sys`, or `/dev`.
- Check the working directory and file ownership before troubleshooting permission errors.
- Leave the test file in the lab directory unless cleanup is required.

---

# ☁️ Relevant Engineering / Cloud Context

Linux permission management is relevant to cloud virtual machines and Linux-based infrastructure.

Cloud engineers may use file permissions to restrict access to application configuration, deployment files, logs, and other local resources.

For credential-related files, restrictive permissions can reduce exposure to other local users. The appropriate mode depends on the file's purpose and which users or processes need access.

---

# ❌ Mistakes I Made Today

No mistakes have been reported yet.

# 🐛 Errors I Encountered

No errors have been reported yet.

---

# 💡 Key Takeaways

1. Linux permissions use three classes: owner, group, and others.
2. Read, write, and execute have numeric values `4`, `2`, and `1`.
3. Mode `600` gives read/write access to the owner only.
4. Mode `640` additionally gives read access to the group.
5. `chmod` changes permissions, while `ls -l` and `stat` help verify them.
6. Verify the actual result instead of assuming a command succeeded.

---

# 🎯 Skills Learned / Practised

**Learned**
- The structure of Linux file permissions.
- The numeric permission system.
- The distinction between modes `600` and `640`.

**Practised**
- Not yet confirmed; terminal execution is pending.

**Implemented**
- The permission change on `report.txt` has not yet been confirmed.

**Verified**
- Final permission mode and screenshot evidence are pending.

---

# 🚀 Next Steps

1. Execute the lab in Ubuntu Bash in WSL.
2. Confirm mode `640` using `ls -l` and `stat`.
3. Verify that the owner can read `report.txt`.
4. Capture the real terminal screenshot and save it at the specified path.
5. Update this README with verified results and actual evidence.

---

# 🙏 Honest Reflection

This session focuses on understanding how Linux permissions control access to files and why the difference between `600` and `640` matters. The practical outcome remains unverified until the commands are executed and the results are inspected.
