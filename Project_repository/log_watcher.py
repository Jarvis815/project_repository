import time
import os
log_file = "scan_log.txt"
# Function to monitor the log file for new entries
if not os.path.exists(log_file):
    print(f"Log file not found. Run the port scanner first.")
    exit(1)
print("Watching log file in real-time...\n")
with open(log_file, "r") as f:
    # Go to the end of the file
    f.seek(0, os.SEEK_END)
    while True:
        # Read new lines from the log file
        line = f.readline()
        if not line:
            time.sleep(0.5)  # Sleep briefly to avoid busy waiting
            continue
        # Print the new log entry to the console
        print(line.strip())