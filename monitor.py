import psutil # This would get the system resource data
import time # This would get the time to pause between updates
import sqlite3


# Connect/create to databse
conn = sqlite3.connect('resources.db')
cursor = conn.cursor()

# Create table to store resource usage
cursor.execute(''' CREATE TABLE IF NOT EXISTS usage  (
               timestamp TEXT,
               cpu REAL,
               memory REAL,
               disk REAL)''')

def log_resources():
    cpu = psutil.cpu_percent()
    memory= psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    timestamp = time.strftime("%Y-%m-%d %H:%S:%S")
    cursor.execute("INSERT INTO usage VALUES (?, ?, ?, ?)", (timestamp, cpu, memory, disk))
    conn.commit()



# Driver Code

if __name__ == "__main__":
    try:
        while True:
            log_resources()
            print("Logged resource usage.")
            time.sleep(5)
    except KeyboardInterrupt:
        print("Stopping resource logger.")
        conn.close()