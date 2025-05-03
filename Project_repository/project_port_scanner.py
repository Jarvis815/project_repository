import socket
from datetime import datetime
#Set up the log file
log_file = "scan_log.txt"
with open(log_file, "a") as log:
    log.write("\n===== New Scan at {} =====\n".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
# Define the target IP address and ports to scan
target = "127.0.0.1" # Replace with your target IP address
ports_to_scan = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 3306,3389,8080] # Common ports to scan
# Define a dictionary of known vulnerable services
vulnerable_services = {
    21: "FTP - May allow anonymous login",
    23: "Telnet - Unencrypted access",
    445: "SMB - Vulnerable to exploits like EternalBlue",
   3306: "MySQL - Common target for weak creds",
   3389: "RDP - Remote Desktop, often brute-forced"
}
# Start scanning the ports
print(f"Scanning {target} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
for port in ports_to_scan:
    print(f"Debug: Scanning port {21}...")
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.1)  # Set a timeout for the connection attempt
    result = sock.connect_ex((target, port))  # Attempt to connect to the port
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if result == 0:
        message = f"[{timestamp}] Port {port} is OPEN"
#Check for known vulnerable services
        if port in vulnerable_services:
                    vuln_msg = f" WARNING: {vulnerable_services[port]} detected!"
                    message += f" | {vuln_msg}"
    else:
        message = (f"[{timestamp}] Port {port} is CLOSED")
print(message) # Print the result to the console
with open(log_file, "a") as log:
    log.write(message + "\n")  # Log the result to the file
    sock.close()  # Close the socket after checking the port