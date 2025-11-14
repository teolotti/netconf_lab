import time
import random
import subprocess
import tempfile
import os
from datetime import datetime

def send_netconf_notification():
    iot_id = random.randint(1, 100)
    rssi = random.randint(-100, -30)
    aoa = round(random.uniform(0.0, 180.0), 2)
    ris_id = 1

    notification = f"""<notification xmlns="urn:ietf:params:xml:ns:netconf:notification:1.0">
    <eventTime>{datetime.utcnow().isoformat()}Z</eventTime>
    <iot-device xmlns="urn:ris">
        <ris-id>{ris_id}</ris-id>
        <iot-id>{iot_id}</iot-id>
        <rssi>{rssi}</rssi>
        <aoa>{aoa}</aoa>
    </iot-device>
    </notification>"""

    with tempfile.NamedTemporaryFile(delete=False, mode='w', suffix='.xml') as temp_file:
        temp_file.write(notification)
        temp_file_path = temp_file.name

    try:
        print(f"[RIS] Sending notification: RIS ID={ris_id}, IoT ID={iot_id}, RSSI={rssi}, AOA={aoa}")
        commands = f'notif --content {temp_file_path}\nquit\n'

        result = subprocess.run(
            ['netopeer2-cli'],
            input=commands,
            text=True,
            capture_output=True,
            timeout=10
        )

        if result.returncode == 0:
            print(f"[RIS] Notification sent successfully.")
        else:
            print(f"❌ Error sending notification (code: {result.returncode})")
            if result.stderr:
                print(f"   Stderr: {result.stderr.strip()}")
            if result.stdout:
                # Cerca messaggi di errore nell'output
                for line in result.stdout.split('\n'):
                    if 'error' in line.lower() or 'fail' in line.lower():
                        print(f"   Output: {line.strip()}")

    except subprocess.TimeoutExpired:
        print("❌ Error: Notification sending timed out.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    finally:
        if os.path.exists(temp_file_path):
            os.unlink(temp_file_path)

def main():
    print("===[RIS] NETCONF Notification Simulator Started===")

    notif_count = 0

    try:
        while True:
            send_netconf_notification()
            notif_count += 1
            print(f"[RIS] Total notifications sent: {notif_count}")
            time.sleep(10)
    except KeyboardInterrupt:
        print("\n[RIS] Simulator stopped by user.")
    except Exception as e:
        print(f"[RIS] Unexpected error in main loop: {e}")

if __name__ == "__main__":
    main()