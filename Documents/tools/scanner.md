# CyberFortress - Port Scanner Documentation
------------------------------------------------
## Overview
The Port Scanner module is designed to scan a target IP address for open ports and potential vulnerabilities. It identifies which ports on a target system are open and can be vulnerable to external attacks.
------------------------------------------------
### Features:
- Scans a target IP for open ports.
- Identifies vulnerable ports that could be targeted by attackers.
- Provides a detailed report on the status of each port (open/closed).
------------------------------------------------
### How It Works:
The scanner works by sending requests to specific ports on the target system. If the port is open, the system will respond, indicating that it’s accessible. If the port is closed or filtered by a firewall, the system won’t respond.
------------------------------------------------
### Example Usage:
Run the `scanner.py` script with the target IP address to perform a scan:
------------------------------------------------
```bash
python security/scanner.py <target-ip>
------------------------------------------------
Example:
python security/scanner.py 192.168.1.1
This will start scanning common ports and provide a report on the open ports on the target machine.
------------------------------------------------
Output:
The output of the scan will include a list of ports and their status (open or closed).
Example of output:
Scanning 192.168.1.1
Port 80: Open
Port 22: Closed
Port 443: Open
------------------------------------------------
Best Practices:
Always ensure that you have permission to scan a target IP.
Use the Port Scanner as part of a regular security audit process.
------------------------------------------------