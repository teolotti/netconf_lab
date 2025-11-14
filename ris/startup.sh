#!/bin/bash
set -e

echo "=== Starting RIS NETCONF Server ==="

# Ferma servizi esistenti
pkill -f sysrepo-plugind || true
pkill -f netopeer2-server || true
sleep 2

# DISINSTALLA completamente il modulo
echo "Removing existing ris module..."
sysrepoctl -u ris --force 2>/dev/null || true

# REINSTALLA il modulo con la nuova versione
echo "Installing updated ris YANG model (with notifications feature)..."
sysrepoctl -i /opt/yang/ris.yang

# ABILITA la feature "notifications" (non "notif"!)
echo "Enabling 'notifications' feature for ris module..."
sysrepoctl -c ris -e notifications

# Verifica che le notifiche siano abilitate
echo "Verifying notifications are enabled..."
sysrepoctl -l | grep ris

# Configura password per NETCONF
echo 'root:root' | chpasswd

# Avvia sysrepo-plugind
echo "Starting sysrepo-plugind..."
sysrepo-plugind -d -v 3 &
PLUGIND_PID=$!
echo "sysrepo-plugind PID: $PLUGIND_PID"

sleep 3

# Avvia netopeer2-server
echo "Starting netopeer2-server..."
netopeer2-server -d -v 3 &
SERVER_PID=$!
echo "netopeer2-server PID: $SERVER_PID"

# Attendi avvio completo
echo "Waiting for services to start..."
sleep 10

# Verifica finale
echo "Final status check:"
if sysrepoctl -l | grep -q "ris.*notifications"; then
    echo "✅ RIS module with 'notifications' feature ENABLED"
else
    echo "❌ RIS module without notifications feature"
    echo "Current status:"
    sysrepoctl -l | grep ris
    exit 1
fi



# Funzione di cleanup
cleanup() {
    echo ""
    echo "=== Shutting down RIS NETCONF Server ==="
    kill $NOTIFY_PID 2>/dev/null && echo "Stopped notification simulator"
    kill $SERVER_PID 2>/dev/null && echo "Stopped netopeer2-server" 
    kill $PLUGIND_PID 2>/dev/null && echo "Stopped sysrepo-plugind"
    wait
    echo "Shutdown complete"
    exit 0
}

trap cleanup SIGINT SIGTERM

echo ""
echo "=== RIS NETCONF Server is fully operational ==="
echo "✅ 'notifications' feature is ENABLED for ris module"
echo "NETCONF endpoint: localhost:830"
echo "Username: root, Password: root" 
echo "Press Ctrl+C to stop all services"

wait