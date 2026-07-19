# 🐍 Day 1 - Python Fundamentals for Infrastructure Automation

**📅 Date:** July 19, 2026  
**🎯 Goal:** Learn Python fundamentals and build the programming foundation required for Infrastructure Automation, Cloud Engineering, and Site Reliability Engineering.

---

# 📖 What I Learned Today

## 1. Variables

Variables store values that can be reused throughout a program.

```python
project = "my-app"
region = "us-central1"
count = 5
```

Variables improve readability and make scripts easier to maintain.

---

# 2. Output with `print()`

The `print()` function displays information to the terminal.

```python
print("Hello World")
print(f"Project: {project}")
```

This is commonly used for logging script execution and debugging.

---

# 3. User Input with `input()`

The `input()` function waits for the user to enter data.

```python
name = input("Enter your name: ")
```

### Important

`input()` always returns a **string**.

---

## ❌ Mistake

```python
project = ("Enter project name: ")
```

This only creates a string.

## ✅ Correct

```python
project = input("Enter project name: ")
```

---

# 4. Type Conversion

Since `input()` returns strings, conversion is often required.

```python
count_str = input("Enter number of VMs: ")

count = int(count_str)

price = float(input("Enter price: "))
```

Without conversion, mathematical operations cannot be performed correctly.

---

# 5. f-Strings

f-Strings provide a clean way to embed variables inside text.

```python
username = "alice"

print(f"Welcome {username}")
```

---

## ❌ Mistake

```python
print("Welcome {username}")
```

Output

```text
Welcome {username}
```

---

## ✅ Correct

```python
print(f"Welcome {username}")
```

Output

```text
Welcome alice
```

---

# 6. Conditional Statements

Python uses `if`, `elif`, and `else` for decision making.

```python
if len(password) >= 8:
    print("Strong password")
else:
    print("Weak password")
```

Remember:

- Conditions end with `:`
- Use consistent indentation (4 spaces)

---

# 7. Finding Length with `len()`

```python
password = "secret123"

length = len(password)
```

Useful for:

- Password validation
- String processing
- Input verification

---

# 8. Splitting Strings

The `.split()` method separates text into a list.

```python
data = "12345.67 9876.54"

fields = data.split()
```

Result

```python
["12345.67", "9876.54"]
```

Individual values can then be accessed using indexes.

```python
fields[0]

fields[1]
```

---

# 9. Reading Files

The recommended approach is using `with`.

```python
with open("/proc/uptime") as f:
    first_line = f.readline()
```

Benefits:

- Automatically closes the file
- Cleaner code
- Prevents resource leaks

---

# 10. Exception Handling

Instead of crashing, programs can recover gracefully.

```python
try:
    count = int(input("Enter number: "))

except ValueError:
    print("Please enter a valid number.")
```

---

## ❌ Mistake

```python
except filenotfounderror:
```

---

## ✅ Correct

```python
except FileNotFoundError:
```

Exception names are case-sensitive.

---

# 11. Input Validation

Validate input before processing it.

```python
count_str = input("How many VMs? ")

if not count_str.isdigit():
    print("Please enter a valid number.")
    exit(1)
```

This prevents runtime errors.

---

# 📝 Programs Built

## 1. VM Deployment Planner

```python
project = input("Enter project name: ")

region = input("Target region: ")

count = int(input("Number of VMs: "))

print(f"Deploying {count} VMs in {region} for project {project}")
```

### Sample Output

```text
Enter project name: my-project
Target region: europe-west4
Number of VMs: 5

Deploying 5 VMs in europe-west4 for project my-project
```

---

## 2. IAM Password Validator

```python
username = input("Username: ")

password = input("Password: ")

if len(password) >= 8:
    print(f"[IAM] Password accepted for {username}")
else:
    print("[IAM] Password too short")
```

---

## 3. Linux Uptime Reader

```python
try:

    with open("/proc/uptime") as f:

        first_line = f.readline()

        fields = first_line.split()

        uptime = float(fields[0])

        print(f"System uptime: {uptime:.0f} seconds")

except FileNotFoundError:

    print("File not found")

except ValueError:

    print("Invalid data")
```

---

## 4. Numeric Input Validator

```python
count = input("How many VMs? ")

if not count.isdigit():

    print("Invalid input.")

    exit(1)

count = int(count)
```

---

# ❌ Mistakes I Made

| Mistake | Cause | Solution |
|----------|-------|----------|
| Forgot `input()` | Treated text as user input | Used `input()` correctly |
| Misspelled `fields` | Typing mistake | Corrected variable name |
| Forgot `f` in f-strings | Variables printed literally | Added `f` |
| Used incorrect exception name | Wrong capitalization | Used `FileNotFoundError` |
| Incorrect indentation | Mixed spaces | Used consistent 4-space indentation |

---

# 🐛 Errors Encountered

| Error | Meaning | Solution |
|--------|---------|----------|
| `FileNotFoundError` | File doesn't exist | Used `try-except` |
| `ValueError` | Invalid conversion | Validated input |
| `IndentationError` | Incorrect indentation | Used 4 spaces |
| `NameError` | Variable not defined | Checked spelling |

---

# 💡 Key Takeaways

- `input()` always returns a string.
- Convert values using `int()` or `float()`.
- Always use `f` before f-strings.
- Python depends on indentation.
- Validate user input before processing.
- Handle exceptions instead of letting programs crash.
- Use `with open()` for file handling.

---

# 🌐 Infrastructure Engineering Relevance

These Python fundamentals directly support infrastructure automation.

| Python Concept | Infrastructure Use Case |
|---------------|--------------------------|
| Variables | Store project IDs, regions, VM names |
| Input | Build interactive deployment scripts |
| Conditions | Validate infrastructure configuration |
| File Handling | Read configuration files and logs |
| Exception Handling | Prevent deployment failures |
| String Processing | Parse command output |
| Input Validation | Validate user-provided infrastructure values |

Python is one of the primary languages used for cloud automation, DevOps tooling, and Site Reliability Engineering.

---

# 🎯 Day Summary

## ✅ Skills Learned

- Variables
- Input & Output
- Type Conversion
- f-Strings
- Conditional Logic
- String Operations
- File Handling
- Exception Handling
- Input Validation

---

## 🚀 Tools Practiced

- Python 3
- VS Code
- Linux Terminal

---

# 🙏 Reflection

Today's session established the programming foundation needed for infrastructure engineering.

Rather than memorizing syntax, I focused on understanding how Python can automate repetitive operational tasks such as deployments, configuration validation, and system monitoring.

Every concept I learned today—from variables to exception handling—will be reused in future cloud automation, DevOps workflows, and SRE tooling.

This is the first step toward writing reliable automation that interacts with Linux systems and cloud platforms.

> **"Automation begins with understanding the language before scaling the infrastructure."** 🐍🚀