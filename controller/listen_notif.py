from ncclient import manager

def notif_handler(notif):
    print("[Controller] Received Notification:")
    print(notif.xml)

print ("[Controller] Subscribing to notifications from RIS server...")

with manager.connect(
    host="ris-netconf-server", 
    port=830, 
    username="root", 
    password="root", 
    hostkey_verify=False,
) as m:
    m.create_subscription()
    print("[Controller] Listening for notifications... (Press Ctrl+C to stop)")
    try:
        while True:
            # Wait for a notification with a timeout (seconds)
            notif = m.take_notification(timeout=0.5)
            if notif:
                notif_handler(notif)
    except KeyboardInterrupt:
        print("\n[Controller] Stopped listening for notifications.")