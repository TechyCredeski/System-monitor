import os
from datetime import datetime

def log_data(data):
    # Define logs folder and ensure it exists
    log_dir = "/mnt/c/Users/Chukwu Solomon/OneDrive/Documents/System monitor/logs"
    os.makedirs(log_dir, exist_ok=True)

    # Define log file path inside the logs folder
    log_file_path = os.path.join(log_dir, "log.txt")

    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - {data}\n"

    # Write log entry
    with open(log_file_path, "a") as log_file:
        log_file.write(log_entry)
