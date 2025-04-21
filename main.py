import time
from datetime import datetime

def get_tasks():
    # Placeholder tasks - replace or expand later
    return [
        "Check AI music trends",
        "Review genre popularity",
        "Log daily status"
    ]

def log(message):
    with open("log.txt", "a") as file:
        file.write(f"[{datetime.now()}] {message}\n")
    print(f"[{datetime.now()}] {message}")

def run_manager():
    log("Manager Agent started.")
    tasks = get_tasks()

    for task in tasks:
        log(f"Performing task: {task}")
        time.sleep(1)  # Simulate doing something

    log("Manager Agent finished run.\n")

if __name__ == "__main__":
    run_manager()
