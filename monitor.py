import psutil # This would get the system resource data
import time # This would get the time to pause between updates

# Function to display system stats
def display_resources():
    while True: 
        # Get CPU, memory, and disk usage 
        cpu = psutil.cpu_percent(interval=1) # Get CPU percentage
        memory = psutil.virtual_memory() # Get memory info
        disk = psutil.disk_usage('/') # Get disk usage info

        # Output the stats for each component
        print("CPU Usage:", cpu, "%")
        print("Memory Usage:", memory.percent, "%")
        print("Disk Usage:", disk.percent, "%")
        print("--------------------------------")

        time.sleep(2) # Wait for 2 seconds before updating


# Driver Code

if __name__ == "__main__":
    print("=== System Resource Monitor ===")
    print(" Press CTRL + C to stop the program")
    print("--------------------------------")
    display_resources()