#!/bin/bash

# Check if log directory is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <log-directory>"
    exit 1
fi

LOG_DIR="$1"
ARCHIVE_DIR="$(dirname "$LOG_DIR")/archives"
TIMESTAMP=$(date '+%Y%m%d_%H%M%S')
ARCHIVE_PATH="${ARCHIVE_DIR}/logs_archive_${TIMESTAMP}.tar.gz"

# Create archive directory and tar.gz file
mkdir -p "$ARCHIVE_DIR"
tar -czf "$ARCHIVE_PATH" -C "$LOG_DIR" .

echo "$(date '+%Y-%m-%d %H:%M:%S') Archive created: $ARCHIVE_PATH" >> /home/passy/RoadMap_sh_devops_projects/project2/log_archive_history.log
