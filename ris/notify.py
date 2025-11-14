import time 
import subprocess 
import random 
print("[RIS] IoT notification simulator started.") 
def build_notification(): 
    iot_id = random.randint(1, 100) 
    rssi = random.randint(-100, -30) 
    aoa = random.uniform(0.0, 180.0)
    ris_id = 1
    notification = f"""
    <iot-device xmlns="urn:ris">
    <ris-id>{ris_id}</ris-id>
    <iot-id>{iot_id}</iot-id> 
    <rssi>{rssi}</rssi> 
    <aoa>{aoa:.2f}</aoa> 
    </iot-device> 
    """ 
    return notification 


while True: 
    notification = build_notification() 
    print(f"[RIS] Sending notification:\n{notification}") 
    subprocess.run(["sysrepocfg", "--notification=stdin", "--format=xml", "--module=ris"], input=notification, text=True, capture_output=True) 
    time.sleep(10)