import subprocess
import re
from logger import log_data
from config import CPU_THRESHOLD, MEMORY_THRESHOLD, send_alert


# Run the bash script and capture the output
def run_data_collector():
    try:
         result = subprocess.check_output(["bash", "/mnt/c/Users/Chukwu Solomon/OneDrive/Documents/System monitor/bash/datacollector.sh"])
         return result.decode("utf-8")
    except subprocess.CalledProcessError as e:
        print(f"Error executing bash script: {e}")
        return None
    
    
# Parse data from the bash script output
def parse_metrics(output):
    # Parse CPU usage (example: CPU Usage: 75%)
    cpu_usage = int(re.search(r"CPU Usage: (\d+)%", output).group(1))

    # Parse Memory usage (example: Used: 3.5Gi / Total: 8Gi)
    memory_usage = re.search(r"Used: ([\d\.]+)Gi / Total: (\d+)Gi", output)
    memory_used = float(memory_usage.group(1)) if memory_usage else 0.0
    memory_total = int(memory_usage.group(2)) if memory_usage else 0

    # Initialize disk_usage as an empty list
    disk_usage = []

    # Parse Disk usage (example: /dev/sda1: 25G used of 50G (50%))
    for line in output.splitlines():
        if "/dev/" in line:
            match = re.search(r"(/dev/\S+): (\S+) used of (\S+) \((\d+)%\)", line)
            if match:
                disk_usage.append({
                    "disk": match.group(1),
                    "used": match.group(2),
                    "total": match.group(3),
                    "percentage": match.group(4),
                })

    # Parse Uptime (example: up 10 days, 3 hours, 15 minutes)
    uptime_match = re.search(r"up (.+)", output)
    uptime = uptime_match.group(1) if uptime_match else "N/A"

    # Return all parsed data
    return cpu_usage, memory_used, memory_total, disk_usage, uptime


# Run the bash script and parse the metrics
bash_output = run_data_collector()
if bash_output:
    cpu, memory_used, memory_total, disk_usage, uptime = parse_metrics(bash_output)
    
    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory_used}Gi / {memory_total}Gi")
    print(f"Disk Usage:")
    for disk in disk_usage:
        print(f"  {disk['disk']}: {disk['used']} used of {disk['total']} ({disk['percentage']}%)")
    print(f"Uptime: {uptime}")
    


# Define log_system_health function
def log_system_health(cpu_usage, memory_used, disk_usage, uptime):
    log_data(f"CPU Usage: {cpu_usage}% | Memory Usage: {memory_used}Gi | Uptime: {uptime}")
    for disk in disk_usage:
        log_data(f"Disk: {disk['disk']} - {disk['used']} used of {disk['total']} ({disk['percentage']}%)")
        
# Alert logic
def check_and_alert(cpu, memory_used, memory_total, disk_usage):
    alert_messages = []

    if cpu > CPU_THRESHOLD:
        alert_messages.append(f"🚨 High CPU Usage: {cpu}% (Threshold: {CPU_THRESHOLD}%)")

    mem_percent = (memory_used / memory_total) * 100 if memory_total else 0
    if mem_percent > MEMORY_THRESHOLD:
        alert_messages.append(f"🚨 High Memory Usage: {memory_used}Gi / {memory_total}Gi ({mem_percent:.1f}%)")

    for disk in disk_usage:
        if disk['percentage'] > 80:  # Alert threshold for disk usage
            alert_messages.append(f"🚨 High Disk Usage on {disk['disk']}: {disk['percentage']}% used")

    if alert_messages:
        send_alert("\n".join(alert_messages))

log_system_health(cpu, memory_used, disk_usage, uptime)
check_and_alert(cpu, memory_used, memory_total, disk_usage)