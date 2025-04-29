#!/bin/bash

#Log file with timestamp
LOG_DIR="/mnt/c/Users/Chukwu Solomon/OneDrive/Documents/System monitor/logs"
LOG_FILE="$LOG_DIR/system_health_$(date '+%Y-%m-%d_%H-%M-%S').log"

{
    echo "System Health Report - $(date)"
echo "=============================="

#CPU
echo
echo "----- CPU Usage -----"
CPU=$(grep 'cpu ' /proc/stat)
IDLE=$(echo $CPU | awk '{print $5}')
TOTAL=$(echo $CPU | awk '{sum=0; for(i=2;i<=8;i++) sum+=$i; print sum}')
USAGE=$((100 - (IDLE * 100 / TOTAL)))
echo "CPU Usage: $USAGE%"


#Memory
echo
echo "----- Memory Usage -----"
free -h | awk '/^Mem/ {print "Used: " $3 " / Total: " $2}'

#Disk
echo
echo "----- Disk Usage -----"
df -h | grep '^/dev/' | awk '{print $1 ": " $3 " used of " $2 " (" $5 " used)"}'

# Uptime./system_health.sh
echo
echo "----- Uptime -----"
uptime -p
} | tee "$LOG_FILE"