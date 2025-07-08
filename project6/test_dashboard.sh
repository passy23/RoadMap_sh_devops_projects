#!/bin/bash

echo " Running system load test to verify Netdata monitoring"

# Duration for stress test
DURATION=60  # seconds

# Check and install stress tool if not installed
if ! command -v stress &> /dev/null; then
    echo "stress tool not found. Installing..."
    sudo apt update && sudo apt install -y stress
fi

# Display current time for reference
echo " Starting test at: $(date)"
echo " Applying CPU, memory, and disk stress for $DURATION seconds..."

# Start stress test: CPU + Memory + Disk I/O
stress --cpu 2 --vm 1 --vm-bytes 256M --io 2 --timeout $DURATION

echo "✅ Load test completed at: $(date)"
echo "           "
echo " Open in browser: http://<your-server-ip>:19999"
