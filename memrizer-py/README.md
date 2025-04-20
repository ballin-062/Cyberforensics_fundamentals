# 🧠 memrizer

_A simple automation wrapper for [Volatility 3](https://github.com/volatilityfoundation/volatility3) — designed to make Windows memory analysis easier and more structured._

---

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-Active-brightgreen.svg)
![Swag](https://img.shields.io/badge/Swag%20-%20ON-red)

---

## 💡 Overview

**memrizer** is a lightweight Python tool that automates the use of common **Volatility 3** plugins on Windows memory dumps.  
It simplifies the process of running multiple plugins, organizes output into structured log files, and serves as a customizable template for expanding or modifying your own memory analysis workflows.

---

## ⚙️ Features

- 🔍 Automates multiple `volatility3` plugin executions.
- 📁 Generates a `log_directory/` with separate output files for each plugin.
- 🧩 Designed as a clean template for further modification.
- 💻 Simple command-line interface (CLI).

---

## 🚀 Usage

> ⚠️ **Before running:**  
Paths to `volatility.py`, the output directory, and your memory dump (`*.mem`) file are **hardcoded** in `memrizer.py`.  
Make sure to edit these variables before executing!

```bash
$ python3 memrizer.py
```
## 🔧 Requirements
Python 3.x

Volatility 3

A Windows memory dump (.mem file)

## 📌 Notes
memrizer does not create or modify volatility plugins. It simply automates their execution.

Perfect as a starting point for scripting your own memory analysis workflows.

You can extend the script to include additional plugins or refine the output structure.

## 🤝 Contributing
Pull requests, suggestions, and custom plugin templates are welcome!
Feel free to fork the repo and build your own memory forensics automation toolkit.

## 🧾 License
This project is licensed under the MIT License.