#!/bin/bash

echo " Installation of  Netdata..."

# Install dependencies
sudo apt update
sudo apt install -y curl

# Install Netdata (kickstart script)
bash <(curl -SsL https://my-netdata.io/kickstart.sh) --dont-wait

echo "Netdata installed. Visit http://<server-ip>:19999 to view dashboard."


