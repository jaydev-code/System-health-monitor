#!/bin/bash

BASE_DIR="/home/eljay/DevOps-Projects/02-system-health-monitor"

echo "setting up the System Health Monitor System...."

mkdir -p "$BASE_DIR/data"
mkdir -p "$BASE_DIR/logs"

chmod +x "$BASE_DIR/collect_metrics.sh"

(crontab -l 2>/dev/null; echo "0 * * * * $BASE_DIR/collect_metrics.sh && python3 $BASE_DIR/generate_report.py") | crontab -

echo "Setup complete!"
echo "Cron job added - runs every hour automatically"
