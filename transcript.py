import os
from datetime import datetime

LOG_FILE = "transcript.txt"


def log_command(command):
    """Save executed command with timestamp"""

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as file:
        file.write(f"[{now}] {command}\n")


def get_history():
    """Return all logged commands"""

    if not os.path.exists(LOG_FILE):
        return []

    with open(LOG_FILE, "r") as file:
        return file.readlines()


def clear_history():
    """Delete transcript history"""

    open(LOG_FILE, "w").close()