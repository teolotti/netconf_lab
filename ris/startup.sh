#! /bin/bash

echo "[RIS] Starting sysrepo and Netopeer2 server..."
sysrepod &
netopeer2-server -d -v2 &


sleep 5
echo "[RIS] RIS NETCONF server is up and running on port 830."

#python3 /opt/notify.py