

# 🐼 Pandas Basics — Complete Notes

> **Practice Session Notes** · Covers missing values, filtering, query method & core DataFrame operations.

---

## 📚 Table of Contents

| # | Topic |
|---|-------|
| 1 | [Loading Data](#1-loading-data) |
| 2 | [Viewing Data](#2-viewing-data) |
| 3 | [Missing Values](#3-missing-values) |
| 4 | [Handling Missing Values](#4-handling-missing-values) |
| 5 | [Filtering Data — Boolean Indexing](#5-filtering-data--boolean-indexing) |
| 6 | [Query Method](#6-query-method) |
| 7 | [Boolean Indexing vs Query](#7-boolean-indexing-vs-query) |
| 8 | [Key Rules Summary](#8-key-rules-summary) |
| 9 | [Important Takeaways](#9-important-takeaways) |

---

## 1. Loading Data

```python
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv")
```

> 📦 This loads the classic **MPG dataset** — a great dataset for practicing pandas with real-world data.

---

## 2. Viewing Data

### 🔼 First Rows

```python
df.head()      # Shows first 5 rows (default)
df.head(10)    # Shows first 10 rows
```

### 🔽 Last Rows

```python
df.tail()      # Shows last 5 rows (default)
df.tail(10)    # Shows last 10 rows
```

---

## 3. Missing Values

### Check for Missing Values

```python
df.isnull()    # Returns a DataFrame of True/False
df.isna()      # Alias — same as isnull()
```

| Value | Meaning |
|-------|---------|
| `True` | Missing value (NaN) |
| `False` | Value exists |

### Count Missing Values

```python
df.isnull().sum()        # Missing count per column
df.isnull().sum().sum()  # Total missing values across entire DataFrame
```

---

## 4. Handling Missing Values

### Fill Missing Values with `fillna()`

```python
df.fillna(0)   # ⚠️ Does NOT modify the original DataFrame!
```

> ⚠️ **Important:** `fillna()` returns a new DataFrame. You must explicitly save the result.

### ✅ Correct Ways to Apply Changes

**Option 1 — Assign back:**
```python
df = df.fillna(0)
```

**Option 2 — Use `inplace=True`:**
```python
df.fillna(0, inplace=True)
```

### Verify No Missing Values Remain

```python
df.isnull().sum()   # All columns should now show 0
```

---

## 5. Filtering Data — Boolean Indexing

### Single Condition

```python
df[df['weight'] > 3433]
```

### Multiple Conditions

```python
# AND condition
df[(df['weight'] > 3433) & (df['origin'] == 'usa')]

# OR condition
df[(df['weight'] > 3433) | (df['mpg'] > 30)]
```

### 📌 Rules

- Use `&` for **AND**
- Use `|` for **OR**
- Each condition **must** be wrapped in its own parentheses `()`

### ❌ Common Mistake

```python
# WRONG — missing parentheses around individual conditions
df[df['weight'] > 3433 & df['origin'] == 'usa']
```

### ✅ Correct Usage

```python
# RIGHT — each condition in its own parentheses
df[(df['weight'] > 3433) & (df['origin'] == 'usa')]
```

---

## 6. Query Method

A cleaner, SQL-like alternative to boolean indexing.

### Single Condition

```python
df.query("weight > 3433")
```

### AND Condition

```python
df.query("weight > 3433 and origin == 'usa'")
```

### OR Condition

```python
df.query("weight > 3433 or mpg > 30")
```

### ❌ Wrong Usage

```python
df.query(model_year > 75)    # Missing quotes — will throw an error!
```

### ✅ Correct Usage

```python
df.query("model_year > 75")  # Condition must be a string
```

---

## 7. Boolean Indexing vs Query

| Feature | Boolean Indexing | `.query()` |
|---------|:----------------:|:----------:|
| **Syntax** | `df[df['col'] > x]` | `df.query("col > x")` |
| **Readability** | Medium | High ⭐ |
| **AND / OR** | `&` / `\|` | `and` / `or` |
| **Parentheses** | Required | Not required |
| **Best for** | Flexibility & computed columns | Clean, SQL-like logic |

---

## 8. Key Rules Summary

### Boolean Indexing

```python
# AND
df[(condition1) & (condition2)]

# OR
df[(condition1) | (condition2)]
```

### Query Method

```python
# AND
df.query("condition1 and condition2")

# OR
df.query("condition1 or condition2")
```

---

## 9. Important Takeaways

| Method | Purpose |
|--------|---------|
| `df.head()` | View **first** N rows |
| `df.tail()` | View **last** N rows |
| `df.isnull()` | Detect missing values |
| `df.isnull().sum()` | Count missing values per column |
| `df.fillna(value)` | Replace missing values |
| `df[condition]` | Filter with boolean indexing |
| `df.query("...")` | Filter with SQL-like string syntax |

---

> 💡 **Pro Tip:** Use `.query()` for readability in exploratory analysis and boolean indexing when you need to reference computed variables or complex expressions.

---

*🐼 Happy Pandas-ing!*
