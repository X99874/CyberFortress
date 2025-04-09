```markdown
# CyberFortress - Utility Functions Documentation
------------------------------------------------
## Overview
The `utils.py` module contains utility functions that assist with various tasks related to cybersecurity operations, such as logging, networking operations, and data formatting.
------------------------------------------------
### Features:
- Logs the results of security scans.
- Provides helper functions for network operations like checking port status.
- Assists with data formatting for easier report generation.
------------------------------------------------
### Key Functions:
#### 1. **Logging Function**:
The `log_results` function records the results of scans and firewall tests, saving them to a log file.

```python
def log_results(data, filename="logs.txt"):
    with open(filename, "a") as f:
        f.write(data + "\n")
------------------------------------------------
2. Port Checking Function:
The check_port function checks if a specific port is open on a target IP.

import socket

def check_port(target_ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target_ip, port))
    if result == 0:
        return True  # Port is open
    else:
        return False  # Port is closed
------------------------------------------------
3. Formatting Function:
The format_report function formats the results of scans into a more readable format.
def format_report(results):
    formatted_results = "\n".join([f"Port {port}: {'Open' if status else 'Closed'}" for port, status in results])
    return formatted_results
------------------------------------------------
 How to Use:
You can import and use these utility functions in your main scripts, like scanner.py or firewall.py, to log results, check port statuses, and format reports.
------------------------------------------------
Example Usage:
from utils import log_results, check_port, format_report

# Example of using check_port function
is_open = check_port("192.168.1.1", 80)
print(f"Port 80 is {'open' if is_open else 'closed'}.")

# Example of logging the result
log_results("Port 80 is open", "logs.txt")

# Example of formatting a scan report
scan_results = [(80, True), (22, False), (443, True)]
formatted_report = format_report(scan_results)
print(formatted_report)
------------------------------------------------
Best Practices:
Use utility functions to reduce code duplication and keep the code clean.
Store logs securely and ensure proper access control.