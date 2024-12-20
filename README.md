
<img width="500" alt="image" src="https://github.com/user-attachments/assets/de146ffb-d2a9-4d08-b80d-8d37a27e7be6" />


# System Resource Monitor

## Overview
The **System Resource Monitor** is a Python-based tool that tracks real-time CPU, memory, and disk usage. It logs resource usage into an SQLite database and displays the data in a web-based dashboard built with Flask. This project is ideal for learning Python, Flask, SQLite, and basic web development concepts.

---

## Features
- Logs system resource usage (CPU, memory, disk) at regular intervals using the **System Logger**.
- Displays logged data in a **Flask Web Dashboard** for easy visualization.
- Stores resource usage data in an **SQLite database** for simplicity.
- Lightweight and easy to set up with a Python virtual environment.

---

## Requirements
- **Python 3.x** (tested with Python 3.8+)
- **Flask** (web framework)
- **psutil** (for system monitoring)
- **SQLite** (comes pre-installed with Python)

---

## Setup Instructions

### **1. Clone the Repository**
Clone the repository to your local machine:
```bash
git clone https://github.com/<your-username>/system-resource-monitor.git
cd system-resource-monitor


## 2. Set Up a Virtual Environment

Create and activate a Python virtual environment to isolate dependencies:

```bash
# Create a virtual environment
python3 -m venv venv

# Install Dependencies
pip install -r requirements.txt

# The System Logger (monitor.py) logs CPU, memory, and disk usage to an SQLite database at regular intervals:
python3 monitor.py

# - This script creates or updates the resources.db SQLite database.
# - Data is logged every few seconds with timestamps.

# The Flask Web Server (app.py) serves the web dashboard:
python3 app.py

# Activate the virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

```
# License
This project is open-source and licensed under the MIT License.

