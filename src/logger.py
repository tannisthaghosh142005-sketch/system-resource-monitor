import logging

logging.basicConfig(
    filename="logs/system.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def log_metrics(metrics):
    logging.info(f"METRICS: {metrics}")

def log_alert(alert):
    logging.warning(f"ALERT: {alert}")