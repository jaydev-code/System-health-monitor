# 02 - System Health Monitor

## Overview
A system health monitoring tool that automatically collects metrics,
checks system status, and generates an HTML report.

## Features
- Collects CPU, Memory, and Disk usage metrics
- Generates color-coded status reports
- Automatic HTML report generation
- Runs automatically every hour via cron

## Technologies
- Bash
- Python 3
- Cron
- JSON
- HTML

## Project Structure
02-system-health-monitor/
├── collect_metrics.sh      # collects system metrics
├── generate_report.py      # checks status + generates HTML
├── setup.sh                # automates everything with cron
├── data/
│   └── metrics.json        # stores collected metrics
├── logs/
│   └── monitor.log         # tracks when script runs
└── reports_system_health_monitor.html  # visual report

#This project is built specifically for a 
Windows WSL2 environment.

Metrics collected:
- CPU usage
- Memory usage  
- Windows C: drive disk usage (WSL specific)
- Windows drivers disk usage (WSL specific)

## Requirements
- Windows 11/10 with WSL2
- Python 3
- Bash

## How to Use
1. Clone the repository
2. Update BASE_DIR in collect_metrics.sh 
   to match your folder path
3. Run setup:
\```bash
chmod +x setup.sh
./setup.sh


## Sample Report
- CPU: 1.23% → Excellent 
- Memory: 35.92% → Fair 
- Windows Disk: 76.0% → Warning 
- WSL Disk: 1.0% → Excellent 

## Author
JayDev-code