import time
import subprocess
import random
from datetime import datetime
import os
import sysrepo

#TODO fix with nettopeer cli

print("[RIS] IoT notification simulator started.")

def send_iot_notification():
    conn = sysrepo.SysrepoConnection()
    sess = conn.start_session()

    try:
        iot_id = random.randint(1, 100)
        rssi = random.randint(-100, -30)
        aoa = round(random.uniform(0.0, 180.0), 2)
        ris_id = 1

        values = [
            ("/ris:iot-device/ris-id", ris_id),
            ("/ris:iot-device/iot-id", iot_id),
            ("/ris:iot-device/rssi", rssi),
            ("/ris:iot-device/aoa", aoa),
        ]
        
        print(f"[RIS] Sending notification: RIS={ris_id}, IoT={iot_id}, RSSI={rssi}, AOA={aoa}")
        
        # Invia la notifica
        sess.event_notification(values)
        print("✅ Notifica inviata con successo!")
        
    except Exception as e:
        print(f"❌ Errore: {e}")
    finally:
        sess.stop()
        conn.disconnect()

# Invia una notifica ogni 10 secondi
while True:
    send_iot_notification()
    time.sleep(10)