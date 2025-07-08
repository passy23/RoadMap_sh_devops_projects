#!/bin/bash

echo "Cleaning up Netdata"

echo "                                "

# Stop Netdata if it's running
if systemctl list-units --type=service | grep -q netdata; then
    echo " Stopping Netdata service..."
    sudo systemctl stop netdata
    sudo systemctl disable netdata
fi

# Remove common Netdata directories and configurations
echo "Removing Netdata files and directories..."
sudo rm -rf \
  /etc/netdata \
  /var/lib/netdata \
  /var/log/netdata \
  /usr/lib/netdata \
  /usr/share/netdata \
  /opt/netdata \
  /etc/systemd/system/netdata.service \
  /usr/sbin/netdata \
  /usr/local/lib/netdata



echo "                                         "
echo " Netdata and related files removed."

