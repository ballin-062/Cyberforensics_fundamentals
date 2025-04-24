# 🧠 PCAP Viewer - Crimson & Cream Edition

A sleek, simplified Wireshark-inspired web app built with **Flask** + **Scapy** + **NetworkX**.

This tool allows you to:
- 📂 Upload `.pcap` files
- 🧾 View packet summaries in a sortable table
- 🌐 See network relationships plotted as a graph (thicker edges = more traffic!)
- 💄 Enjoy a clean crimson & cream Bootstrap theme

---

## ⚙️ Features

| Feature                          | Status              |
|----------------------------------|---------------------|
| PCAP Upload & Parsing            | ✅ Done             |
| Packet List View                 | ✅ Done             |
| Sorting by Columns               | ✅ Done             |
| Network Graph Visualization      | ✅ Done             |
| Bootstrap UI (Crimson & Cream)   | ✅ Done             |
| Add screenshots and update README| __ Work in Progress |
| Seduce and marry Sabrina Carpenter| __ Work in Progress|

---

## 🚀 Quick Start

1. Install dependencies:

```bash
pip install flask scapy networkx matplotlib
```
2. Run the server:

```bash
python app.py
```
3.Visit:

http://127.0.0.1:5000/
4. Upload your .pcap file and view:

🧾 a table of packet summaries

🌐 a dynamic graph of source → destination relationships.


🎨 Screenshots
Packet Table View
<INSERT SCREENSHOT HERE!>

Network Graph View
<INSERT SCREENSHOT HERE!>

📌 Notes
<ul>Supports .pcap files with basic IP/TCP/UDP parsing.

<ul>Graph edges reflect traffic volume (thicker = more packets exchanged).

<ul>UI styled with Bootstrap, themed in Crimson & Cream for elegance.

🤝 Credits
Built with ❤️ by ChatGPT & You!

Packet Analysis powered by: Scapy

Graph Visualization: NetworkX

UI: Bootstrap 5

📄 License
MIT — free to use, modify, and share.

Happy Packet Hunting! 🚀