import random
import time
import psutil
import numpy as np

def simulate_ransomware():
    activity_log = []

    for i in range(10):
        action = random.choice([
            "Scanning files...",
            "Encrypting dummy file...",
            "Modifying file names...",
            "Creating ransom note..."
        ])
        activity_log.append(action)
        time.sleep(0.2)

    # Real-time system data
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    processes = len(psutil.pids())
    network = psutil.net_io_counters().bytes_sent / 1000000
    suspicious_flag = random.randint(0,1)

    features = [
        cpu_usage,
        memory_usage,
        disk_usage,
        processes,
        network,
        suspicious_flag
    ]

    return activity_log, features