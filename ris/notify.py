import time
import subprocess
import random

print("[RIS] IoT notification simulator started.")

def build_notification():
    iot_id = random.randint(1, 100)
    rssi = random.randint(-100, -30)
    aoa = random.uniform(0.0, 180.0)
    notification = f"""<notification xmlns="urn:ietf:params:xml:ns:netconf:notification:1.0">
    <eventTime>{time.strftime("%Y-%m-%dT%H:%M:%S")}</eventTime>
    <iot-device xmlns="urn:ris">
        <id>{iot_id}</id>
        <rssi>{rssi}</rssi>
        <aoa>{aoa:.2f}</aoa>
    </iot-device>
    </notification>"""
    return notification

while True:
    notification = build_notification()
    print(f"[RIS] Sending notification:\n{notification}")
    subprocess.run(["sysrepocfg", "--notification=stdin", "--format=xml", "--datastore=running"], input=notification.encode())
    time.sleep(10)