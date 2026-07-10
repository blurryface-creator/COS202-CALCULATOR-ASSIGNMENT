# Multi-Purpose Functional Calculators in Python

This repository contains two production-ready, interactive Python software solutions designed to fulfill academic and numerical operations requirements.

## 🛠️ Project Descriptions

### 1. Interactive Mathematical Calculator (MC)
A lightweight desktop calculator built using Python's native `tkinter` GUI package. It provides an intuitive dark-themed panel interface handling baseline calculations and explicit floor operations.
* **Key Components:** `+`, `-`, `/`, `*`, `%`, `^` (Exponentiation), `\` (Floor Division), `C` (Clear Screen), and `OFF` (Safe Shutdown).
* **Defensive Error Handling:** Built-in catch-blocks preventing raw application crashes on common computation faults like `ZeroDivisionError` or invalid text sequences.

### 2. Personal Pocket CGPA Calculator (PPC)
A terminal-based command-line interface application managing multiple academic semesters' GPA and cumulative graduation data.
* **Core Logic:** Implements layered selection control structures (`if-elif-else`) to dynamically convert numeric input scores into 5-point standard grade metrics (A to F).
* **Dynamic Intelligence:** Instantly renders your cumulative classification standings (e.g., First Class, Second Class Upper) along with automated academic progression advice text based on your running performance.

---

## 📸 System Outputs & Execution Logs

To verify execution profiles locally, run the script modules using your standard interpreter console:
`python calculator.py` or `python pocket_cgpa.py`

### Visual Architecture & Sample Terminal Interfaces:

#### Mathematical Calculator Screen Preview:
* High-Contrast Interface: Background matrix initialized at grid hex `#1e1e24`.
* Status Update: Successfully transforms `^` parsing into internal power evaluations (`**`).

#### Pocket CGPA Terminal Report Sample:
=============================================
         CURRENT CGPA POCKET STATUS
=============================================
 Total Registered Units : 15
 Total Quality Points   : 68.00
 Current Standing CGPA  : 4.53
---------------------------------------------
 Class: First Class Honours 🌟
 Advice: Maintain the momentum, you are flying high!
=============================================
