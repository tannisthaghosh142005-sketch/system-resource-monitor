from config_loader import load_config

config = load_config()

CPU_THRESHOLD = config["cpu_threshold"]
MEM_THRESHOLD = config["memory_threshold"]
DISK_THRESHOLD = config["disk_threshold"]

def check_alerts(metrics):

    alerts = []

    if metrics["cpu"] > CPU_THRESHOLD:
        alerts.append(("CPU", "CRITICAL"))

    if metrics["memory"] > MEM_THRESHOLD:
        alerts.append(("MEMORY", "WARNING"))

    if metrics["disk"] > DISK_THRESHOLD:
        alerts.append(("DISK", "CRITICAL"))

    return alerts