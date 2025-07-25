#!/bin/bash


# OS Info
echo  " ******OS Information:******"
uname -a

# Uptime
echo "                                "
echo  " ****** Uptime:******"
uptime -p

# Load Average
echo "                          "
echo  "******Load Average (1, 5, 15 min):******"
uptime | awk -F'load average: ' '{print $2}'

# Logged In Users
echo "                               "
echo  " ******Currently Logged-in Users:******"
who

# CPU Usage
echo "                                 "
echo  " ******Total CPU Usage:******"
top -bn1 | grep "Cpu(s)" | \
awk '{print "Used: " 100 - $8 "%, Idle: " $8 "%"}'

# Memory Usage
echo "                              "
echo  " ******Memory Usage:******"
free -m | awk '/Mem:/ {
    used=$3; free=$4; total=$2;
    printf "Used: %d MB, Free: %d MB, Total: %d MB, Usage: %.2f%%\n", used, free, total, (used/total)*100
}'

# Disk Usage
echo "                             "
echo -e "  *******Disk Usage (root /):*******"
df -h / | awk 'NR==2 {
    print "Used: " $3 ", Free: " $4 ", Total: " $2 ", Usage: " $5
}'

# Top 5 CPU-consuming processes
echo "                                "
echo -e " *******Top 5 CPU-Consuming Processes:******"
ps -eo pid,ppid,cmd,%cpu --sort=-%cpu | head -n 6

# Top 5 Memory-consuming processes
echo "                                "
echo -e " ******Top 5 Memory-Consuming Processes:******"
ps -eo pid,ppid,cmd,%mem --sort=-%mem | head -n 6

# Failed login attempts (optional)
echo "                                  "
if [ -f /var/log/auth.log ]; then
    echo -e " ******Failed Login Attempts (last 24h):******"
    grep "Failed password" /var/log/auth.log | \
    awk -v d1="$(date --date="1 day ago" '+%b %_d')" '$0 ~ d1' | wc -l
fi


