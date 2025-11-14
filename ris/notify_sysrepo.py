#!/usr/bin/env python3
import time
import random
import sysrepo
from datetime import datetime

def send_sysrepo_notification():
    """Invia una notifica usando sysrepo con il metodo corretto"""
    try:
        # Connetti a sysrepo
        conn = sysrepo.SysrepoConnection()
        sess = conn.start_session()
        
        # Genera dati casuali
        iot_id = random.randint(1, 1000)
        rssi = random.randint(-100, -30)
        aoa = round(random.uniform(0.0, 180.0), 2)
        ris_id = 1

        print(f"[RIS-Sysrepo] Sending notification: RIS={ris_id}, IoT={iot_id}, RSSI={rssi}, AOA={aoa}")

        # Prepara i dati della notifica come dictionary
        notification_data = {
            "ris-id": ris_id,
            "iot-id": iot_id, 
            "rssi": rssi,
            "aoa": aoa
        }
        
        # Invia la notifica usando il metodo corretto
        sess.notification_send("/ris:iot-device", notification_data)
        print("✅ Sysrepo notification sent successfully!")
        
        # Chiudi la sessione
        sess.stop()
        conn.disconnect()
        return True
        
    except sysrepo.SysrepoError as e:
        print(f"❌ Sysrepo error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def main():
    print("=== RIS Sysrepo Notification Simulator ===")
    print("Using Sysrepo notification_send() method")
    print("Sending notifications every 10 seconds...")
    print("Press Ctrl+C to stop\n")
    
    notification_count = 0
    success_count = 0
    
    try:
        while True:
            if send_sysrepo_notification():
                success_count += 1
            notification_count += 1
            
            print(f"[RIS] Statistics: {success_count}/{notification_count} successful\n")
            time.sleep(10)
            
    except KeyboardInterrupt:
        print(f"\n[RIS] Stopped after {notification_count} attempts ({success_count} successful)")
    except Exception as e:
        print(f"[RIS] Fatal error: {e}")

if __name__ == "__main__":
    main()