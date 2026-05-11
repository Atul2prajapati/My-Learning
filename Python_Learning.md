# 🚀 Learning Python for Data Engineering (DE)

Welcome to your Python learning notes for **Data Engineering**.  
This guide covers the basics of **File Handling in Python** with simple explanations and examples.

---

# 📂 File Handling in Python

File handling allows Python to:

- 📖 Read files
- ✍️ Write data
- ➕ Append content
- 🆕 Create files

---

# 🧠 RAWX Concept

| Mode | Meaning |
|------|----------|
| `R` | Read |
| `A` | Append |
| `W` | Write |
| `X` | Create |

---

# 1️⃣ READ Mode (`r`)

Used to read the contents of a file.

---

## 📖 A) Read Command

```python
f = open("Practice.txt")

print(f.read())
```

### 🔍 Explanation

- `open()` opens the file
- `read()` reads the complete content

---

## 🔒 B) Closing a File

```python
f.close()
```

### ⚠️ Why Close a File?

Closing a file is important because:

- It saves resources
- Prevents memory leaks
- Ensures changes are saved properly

---

## 🛑 C) Handling Error if File Does Not Exist

```python
try:
    f = open("atul.txt")
    print(f.read())

except:
    print("This file is not present")

finally:
    f.close()
```

### 💡 Explanation

- `try` → Runs risky code
- `except` → Handles errors
- `finally` → Always executes

---

# 2️⃣ APPEND Mode (`a`)

Append mode adds new content to the file **without deleting old data**.

✅ Also creates the file if it does not exist.

---

## ➕ A) Append Example

```python
f = open("Practice.txt", "a")

f.write("Please also check the brand netting")

f.close()

f = open("Practice.txt")

print(f.read())

f.close()
```

### 🧠 Important

Every time this code runs:

- New text gets added at the end of the file

---

# 3️⃣ WRITE Mode (`w`)

Write mode replaces the **entire content** of the file.

⚠️ Be careful while using it.

---

## ✍️ A) Write Example

```python
# Reading old content
f = open("NamingSheet.txt", "r")

print(f.read())

f.close()

# Replacing content
f = open("NamingSheet.txt", "w")

f.write("We are deleting all content in this file")

f.close()

# Reading updated content
f = open("NamingSheet.txt", "r")

print(f.read())

f.close()
```

### ⚠️ Important Note

Whenever you use:

```python
open("file.txt", "w")
```

Python will:

- Remove existing content
- Replace it with new data

---

# 4️⃣ Creating Files in Python

There are two ways to create files.

---

## 🆕 A) Create File Using `w`

Creates the file if it does not exist.

```python
f = open("FileCreated.txt", "w")

f.close()
```

### ✅ Behavior

- Creates file if missing
- Does NOT throw error if file already exists

---

## 🚫 B) Create File Using `x`

Creates a file only if it does not already exist.

```python
import os

if os.path.exists("FileCreated.txt"):
    print("File already exists")

else:
    f = open("FileCreated.txt", "x")
    f.close()
```

### 💡 Why Use `x`?

- Prevents accidental overwriting
- Safer for important files

---

# 5️⃣ Deleting a File 🗑️

Python allows us to delete files using the `os` module.

---

## 🧹 Delete File Example

```python
import os

if os.path.exists("FileCreated.txt"):
    os.remove("FileCreated.txt")

else:
    print("File does not exist")
```

### 💡 Explanation

| Function | Purpose |
|----------|----------|
| `os.path.exists()` | Checks whether the file exists |
| `os.remove()` | Deletes the file |

---

### ⚠️ Important

Always check if the file exists before deleting it.  
Otherwise Python will throw an error.

---

# 6️⃣ Copying Content from One File to Another 📄➡️📄

We can read data from one file and write it into another file.

---

## 🔁 Copy File Content Example

```python
# Reading content from Practice.txt
with open("Practice.txt") as f:
    content = f.read()

# Writing content into NamingSheet.txt
with open("NamingSheet.txt", "w") as f:
    f.write(content)
```

---

### 💡 Why Use `with open()`?

Using `with open()` is considered best practice because:

✅ Automatically closes the file  
✅ Cleaner and shorter code  
✅ Better memory management

---

## 🧠 Flow of the Program

```text
Practice.txt  ──(Read Content)──▶  content variable
                                      │
                                      ▼
                          NamingSheet.txt
                           (Write Content)
```

---

# 🎯 What We Learned

✅ How to delete files safely  
✅ How to check file existence  
✅ How to copy content between files  
✅ Why `with open()` is better

---

# 🎯 Quick Summary

| Mode | Purpose | Creates File? | Deletes Old Content? |
|------|----------|----------------|----------------------|
| `r` | Read file | ❌ No | ❌ No |
| `a` | Append data | ✅ Yes | ❌ No |
| `w` | Write data | ✅ Yes | ✅ Yes |
| `x` | Create file only | ✅ Yes | ❌ No |

---

# 🏁 Final Notes

✅ Always close files after use  
✅ Use `try-except` for safer programs  
✅ Prefer `a` when you don't want to lose old data  
✅ Use `x` for secure file creation

---

# 📚 Next Topics to Learn

- File Paths
- CSV Handling
- JSON Handling
- Pandas File Operations
- Exception Handling
- OS Module
- Logging

---