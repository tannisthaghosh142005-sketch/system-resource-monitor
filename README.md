#### \# System Resource Monitoring \& Alerting Tool

A Python-based system monitoring tool that continuously tracks CPU, memory, disk, and network usage and generates alerts when predefined thresholds are exceeded.



###### \## Features

\- Real-time system resource monitoring

\- CPU, memory, disk, and network metrics collection

\- Threshold-based alert generation

\- Logging system for alerts

\- Automatic dataset generation for monitoring metrics

\- Config-driven thresholds



###### \## Tech Stack

\- Python

\- psutil

\- pandas

\- logging



##### \## Project Structure

**system-monitor/**

* config/

&nbsp;    config.json

* src/

&nbsp;    monitor.py

&nbsp;    alerts.py

&nbsp;    logger.py

&nbsp;    storage.py

&nbsp;    config\_loader.py

&nbsp;    main.py

* logs/

&nbsp;    system.log

* requirements.txt
* README.md



###### System Resource Monitoring \& Alerting Tool — Flowchart   

&nbsp;               ┌───────────────────────────┐

&nbsp;               │        main.py                    │

&nbsp;               │  (Monitoring Controller)          │

&nbsp;               └─────────────┬─────────────┘

&nbsp;                                 │

&nbsp;                                 ▼

&nbsp;               ┌───────────────────────────┐

&nbsp;               │        monitor.py                 │

&nbsp;               │  Collect System Metrics           │

&nbsp;               │  CPU / Memory / Disk              │

&nbsp;               │  Network / Processes              │

&nbsp;               └─────────────┬─────────────┘

&nbsp;                                 │

&nbsp;                                 ▼

&nbsp;               ┌───────────────────────────┐

&nbsp;               │       storage.py                  │

&nbsp;               │ Save Metrics to CSV               │

&nbsp;               │ metrics.csv dataset               │

&nbsp;               └─────────────┬─────────────┘

&nbsp;                                 │

&nbsp;                                 ▼

&nbsp;               ┌───────────────────────────┐

&nbsp;               │        alerts.py                  │

&nbsp;               │  Compare Metrics with             │

&nbsp;               │  Thresholds                       │

&nbsp;               └─────────────┬─────────────┘

&nbsp;                                 │

&nbsp;                                 ▼

&nbsp;               ┌───────────────────────────┐

&nbsp;               │      config\_loader.py             │

&nbsp;               │ Load Thresholds from              │

&nbsp;               │ config/config.json                │

&nbsp;               └─────────────┬─────────────┘

&nbsp;                                 │

&nbsp;                                 ▼

&nbsp;               ┌───────────────────────────┐

&nbsp;               │        logger.py                  │

&nbsp;               │  Write Alerts to Logs             │

&nbsp;               │ logs/system.log                   │

&nbsp;               └───────────────────────────┘

###### 

###### \## Installation

```bash

pip install -r requirements.txt



###### \## Run the Project

python src/main.py

###### 

###### \##Example Output



===== SYSTEM RESOURCE MONITOR =====

CPU Usage        : 12.7 %

Memory Usage     : 53.8 %

Disk Usage       : 57.0 %

Network Sent     : 262761698 bytes

Network Received : 123275455 bytes

Process Count    : 250

===================================



###### \##Future Improvements



* Email alerts
* Slack notifications
* Web dashboard
* Docker monitoring
