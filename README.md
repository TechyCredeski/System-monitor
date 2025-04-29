# System Health Monitor & Alert Script

This project is a system monitoring tool that tracks and logs various system health metrics such as CPU usage, memory usage, disk usage, and system uptime. The collected data is saved in log files, and the system sends alerts if any monitored values exceed defined thresholds. The project is designed to run on Linux systems, including WSL (Windows Subsystem for Linux).

---

## Project Structure

```
system-health-monitor/
├── bash/
│   └── datacollector.sh          # Bash script to collect system health data
├── python/
│   ├── config.py                 # Configuration file for threshold values and alert function
│   ├── logger.py                 # Logger utility to write health data to log files
│   └── monitor.py                # Python script that runs the system monitor, parses data, and sends alerts
├── logs/
│   └── (auto-generated log files)
└── .gitignore                    # Git ignore file
```

---

## Prerequisites

Before using the System Health Monitor & Alert Script, make sure you have the following installed:

- **Python 3.x**: This is required to run the `monitor.py` script.
- **Bash**: Required for running the Bash script (`datacollector.sh`).
- **Linux or WSL**: The script is designed to run on Linux-based systems or Windows Subsystem for Linux (WSL).
- **cron (optional)**: For automating the monitoring script.

---

## Features

- **CPU Monitoring**: Tracks CPU usage and logs it.
- **Memory Monitoring**: Monitors the used and total memory.
- **Disk Monitoring**: Tracks disk usage for each partition.
- **Uptime Monitoring**: Logs system uptime.
- **Alerting**: Sends email alerts when system metrics exceed defined thresholds for CPU, memory, or disk usage.
- **Logging**: Logs all collected metrics with timestamps in a log file.
- **Automatic Execution**: Can be automated using `cron` or other task schedulers.

---

## How It Works

1. **Bash Script (datacollector.sh)**:
   - Gathers data on CPU, memory, disk usage, and system uptime using Linux system commands.
   - The script generates a log file with a timestamped name (e.g., `system_health_YYYY-MM-DD_HH-MM-SS.log`).

2. **Python Script (monitor.py)**:
   - Executes the Bash script to collect system health data.
   - Parses the output of the Bash script and extracts the relevant information.
   - Logs the data in a log file (`log.txt`) located in the `/logs` directory.
   - Compares the monitored metrics to defined thresholds (found in `config.py`).
   - Sends alerts if any thresholds are exceeded.

---

## Configuration

### Thresholds for Alerts

The `config.py` file contains the threshold values for CPU and memory usage. You can adjust these thresholds based on your system requirements:

```python
CPU_THRESHOLD = 80          # CPU usage threshold (in percentage)
MEMORY_THRESHOLD = 85       # Memory usage threshold (in percentage)

def send_alert(message):
    print(f"ALERT: {message}")  # Customize with your alert mechanism (e.g., email, Telegram)
```

---

## Running the Script

### Step 1: Make the Bash Script Executable

To make sure the Bash script is executable, run the following command:

```bash
chmod +x bash/datacollector.sh
```

### Step 2: Run the Python Script

To start the system monitoring and alerting process, run the Python script:

```bash
python3 python/monitor.py
```

This will execute the Bash script, collect system data, and log it while checking if any thresholds are exceeded.

---

## Automation

You can automate the script to run at regular intervals using `cron`. For example, to run the script every 15 minutes:

1. Open the crontab editor:

   ```bash
   crontab -e
   ```

2. Add the following line to run the script every 15 minutes:

   ```bash
   */15 * * * * /usr/bin/python3 /path/to/python/monitor.py
   ```

Make sure to replace `/path/to/python/monitor.py` with the actual path to your Python script.

---

## Log Files

The logs are stored in the `/logs` directory. Each log file is named with a timestamp (e.g., `system_health_2025-04-29_08-42-01.log`) and contains the system health data collected during that run.

---

## Example Output

### Console Output:

```
CPU Usage: 67%
Memory Usage: 3.1Gi / 8Gi
Disk Usage:
/dev/sda1: 15G used of 50G (30%)
Uptime: up 2 hours, 13 minutes
```

### Log File (`logs/log.txt`):

```
2025-04-29 08:42:01 - CPU Usage: 67% | Memory Usage: 3.1Gi | Uptime: up 2 hours, 13 minutes
2025-04-29 08:42:01 - Disk: /dev/sda1 - 15G used of 50G (30%)
```

---

## License

MIT License. You can freely use and modify this script for personal and commercial purposes.

---

## Author

Created by Solomon Chukwu(Credeski) (https://github.com/TechyCredeski).

