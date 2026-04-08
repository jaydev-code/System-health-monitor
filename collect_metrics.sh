#!/bin/bash

BASE_DIR="/home/eljay/DevOps-Projects/02-system-health-monitor"
DATA_FILE="$BASE_DIR/data/metrics.json"
LOG_FILE="$BASE_DIR/logs/monitor.log"


CPU_USAGE=$(cat /proc/stat | awk '/cpu / {printf("%.2f",100 - (100 * ( $5 / ($2+$3+$4+$5+$6+$7+$8))))}')
MEMORY_USED=$(free | awk '/Mem/ {printf("%.2f", 100 * ( $3 / $2 ))}')
WINDOWS_DRIVER_USED=$(df | awk '/drivers/ {printf("%.2f",$5)}')
WSL_DISK_USED=$(df | awk '/\/dev\/sdd/   {printf("%.2f",$5)}')
user=$(whoami)

cat <<EOF > "$DATA_FILE"
{

  "cpu_usage": $CPU_USAGE,
  "memory_used": $MEMORY_USED,
  "Windows_drivers_disk_used": $WINDOWS_DRIVER_USED,
  "wsl_disk_used": $WSL_DISK_USED,
  "timestamp": "$(date '+%Y-%m-%d %H:%M:%S')",
  "User": "$user"
}
EOF


echo "$(date) - Metrics collected" >> "$LOG_FILE"
