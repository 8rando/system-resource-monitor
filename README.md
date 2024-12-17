# **System Resource Monitor**

## **Project Overview**  
This is a Python-based system resource monitor that displays real-time information about CPU usage, memory usage, and disk space. It is a lightweight command-line tool designed for learning system monitoring concepts and scripting with Python.  

---

## **Features**  
- Displays real-time CPU, memory, and disk usage.  
- Simple command-line interface for ease of use.  
- Updates resource statistics every few seconds for continuous monitoring.  

---

## **Requirements**  
- Python 3.11.9 installed on the system.  
- The `psutil` library for retrieving system resource information.  

---

## **Setup Instructions**  

1. **Clone the Repository**  
   Clone the project to your local machine:  
   ```bash
   git clone https://github.com/<your-username>/system-resource-monitor.git
   cd system-resource-monitor
   ```

2. **Install Dependencies**  
   Use `pip` to install the required library:  
   ```bash
   pip install psutil
   ```

3. **Run the Script**  
   Execute the script to start monitoring system resources:  
   ```bash
   python monitor.py
   ```

---

## **Example Usage**  

### **Sample Output**  
```
=== System Resource Monitor ===
Press CTRL+C to stop the program.
-----------------------------
CPU Usage: 23%
Memory Usage: 45%
Disk Usage: 61%
-----------------------------
CPU Usage: 25%
Memory Usage: 47%
Disk Usage: 62%
-----------------------------
```

---

## **How It Works**  
1. The script uses the `psutil` library to collect system resource data.  
2. It retrieves the following metrics:  
   - **CPU Usage**: Percentage of CPU currently being used.  
   - **Memory Usage**: Percentage of RAM in use.  
   - **Disk Usage**: Percentage of storage space used on the root directory.  
3. The information is printed to the terminal and refreshed every 2 seconds.

---

## **Project Structure**  
```
system-resource-monitor/
│-- monitor.py        # Main script to monitor system resources
```

---

## **Potential Improvements**  
- Add logging to save resource data to a file.  
- Build a web-based dashboard using Flask to visualize the data.  
- Add alerting for when CPU, memory, or disk usage crosses a set threshold.  
- Include graphing for historical trends using libraries like Matplotlib or Plotly.  

---

## **Technologies Used**  
- **Python**  
- **psutil**: To retrieve CPU, memory, and disk information.  

---

## **License**  
This project is open-source and licensed under the MIT License.  

---

