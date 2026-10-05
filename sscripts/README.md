server-stats.sh is a Bash script that provides a quick snapshot of your Linux server’s performance. It monitors CPU usage, memory stats, disk usage, and the top resource-consuming processes.

Features
 CPU Usage: Real-time CPU utilization.
 Memory Stats: Total, used, and available memory, with usage percentages.
 Disk Usage: Disk space usage of the root (/) partition, with also percentage.
Top Processes:
Top 5 processes by CPU usage
Top 5 processes by Memory usage


Script Overview:
Uses top, grep, sed, and awk to extract CPU idle percentage and calculate actual usage.

Parses /proc/meminfo to get: MemTotal, MemAvailable.

Uses df -h / and df / to get: Human-readable disk size and Used and available disk space in KB.

Fetches the top 5 processes sorted by: CPU and Memory, through ps aux.

