import psutil
from datetime import datetime

def get_system_metrics():

    metrics = {
        "timestamp": datetime.now(),
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage("/").percent,
        "network_sent": psutil.net_io_counters().bytes_sent,
        "network_recv": psutil.net_io_counters().bytes_recv,
        "process_count": len(psutil.pids())
    }
    print(f"Time             : {metrics['timestamp']}")
    return metrics