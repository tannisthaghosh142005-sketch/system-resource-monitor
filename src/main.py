import time
from monitor import get_system_metrics
from alerts import check_alerts
from logger import log_metrics, log_alert
from storage import save_metrics
from config_loader import load_config

config = load_config()
interval = config["monitor_interval"]

for i in range(30):

    metrics = get_system_metrics()

    print("SYSTEM METRICS:", metrics)
    print("\n===== SYSTEM RESOURCE MONITOR =====")
    print(f"CPU Usage        : {metrics['cpu']} %")
    print(f"Memory Usage     : {metrics['memory']} %")
    print(f"Disk Usage       : {metrics['disk']} %")
    print(f"Network Sent     : {metrics['network_sent']} bytes")
    print(f"Network Received : {metrics['network_recv']} bytes")
    print(f"Process Count    : {metrics['process_count']}")
    print("===================================\n")

    log_metrics(metrics)

    alerts = check_alerts(metrics)

    if alerts:
        for alert in alerts:
            print("ALERT:", alert)
            log_alert(alert)

    time.sleep(interval)