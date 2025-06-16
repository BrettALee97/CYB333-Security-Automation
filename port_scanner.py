# port_scanner.py

import socket
from datetime import datetime

# Function to scan a single port
def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((host, port))
            return result == 0
    except socket.gaierror:
        print("[ERROR] Hostname could not be resolved.")
        return False
    except socket.error:
        print("[ERROR] Could not connect to server.")
        return False

# Main scan function
def scan_ports(host, start_port, end_port):
    print(f"[INFO] Starting scan on {host} from port {start_port} to {end_port}")
    open_ports = []
    for port in range(start_port, end_port + 1):
        if scan_port(host, port):
            print(f"[OPEN] Port {port} is open")
            open_ports.append(port)
    print(f"[DONE] Scan completed. Open ports: {open_ports}")

# Input validation
try:
    target = input("Enter host to scan (127.0.0.1 or scanme.nmap.org): ").strip()
    start = int(input("Enter start port: "))
    end = int(input("Enter end port: "))

    if start < 0 or end > 65535 or start > end:
        raise ValueError("Invalid port range.")

    start_time = datetime.now()
    scan_ports(target, start, end)
    print(f"[TIME] Scan finished in {datetime.now() - start_time}")

except ValueError as ve:
    print(f"[INPUT ERROR] {ve}")
except KeyboardInterrupt:
    print("\n[EXIT] Scan interrupted by user.")