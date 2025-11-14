import time
from datetime import datetime
from ncclient import manager

DEVICE = {
    "host": "ris-netconf-server",
    "port": 830,
    "username": "root",
    "password": "root",
    "hostkey_verify": False,
}

def print_notif(n):
    print("[Controller] --- notification @", datetime.utcnow().isoformat(), "---")
    # ncclient Notification object: preferisci xml quando possibile
    if hasattr(n, "xml"):
        print(n.xml)
    elif hasattr(n, "notification_xml"):
        print(n.notification_xml)
    else:
        print(repr(n))
    print("[Controller] -------------------------------")

print("[Controller] Subscribing to notifications from RIS server...")
with manager.connect(**DEVICE) as m:
    reply = m.create_subscription()
    print("[Controller] create_subscription reply:", reply)
    print("[Controller] Listening for notifications... (Press Ctrl+C to stop)")
    try:
        idle_count = 0
        while True:
            notif = m.take_notification(timeout=5)   # blocking up to 5s
            if notif:
                idle_count = 0
                print_notif(notif)
            else:
                idle_count += 1
                # show progress every 6 idle cycles (~30s)
                if idle_count % 6 == 0:
                    print(f"[Controller] No notif for {idle_count*5} seconds (still listening) @ {datetime.utcnow().isoformat()}")
    except KeyboardInterrupt:
        print("\n[Controller] Stopped listening for notifications.")
    except Exception as e:
        print("[Controller] Exception in listener:", repr(e))