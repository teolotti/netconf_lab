from ncclient import manager
import xml.etree.ElementTree as ET
import json
import time

DEVICE = {
    "host": "ris-netconf-server",
    "port": 830,
    "username": "root",
    "password": "root",
    "hostkey_verify": False
}

# Carico configurazione beam da JSON
with open("beams_config.json") as f:
    beam_list = json.load(f)

def build_config_xml(beams):
    # Crea l'elemento radice config
    config = ET.Element("config", xmlns="urn:ietf:params:xml:ns:netconf:base:1.0")
    
    # Crea elemento ris con il namespace corretto
    ris = ET.SubElement(config, "ris", xmlns="urn:ris")
    
    # Aggiungi ris-id
    ris_id = ET.SubElement(ris, "ris-id")
    ris_id.text = "1"
    
    # Aggiungi beams
    for b in beams:
        beam = ET.SubElement(ris, "beam")
        
        beam_id = ET.SubElement(beam, "id")
        beam_id.text = str(b["id"])
        
        direction = ET.SubElement(beam, "direction")
        direction.text = str(b["direction"])
        
        enabled = ET.SubElement(beam, "enabled")
        enabled.text = str(b["enabled"]).lower()
        
        power = ET.SubElement(beam, "power")
        power.text = str(b["power"])
    
    return ET.tostring(config, encoding='utf-8').decode()



with manager.connect(**DEVICE) as m:
    print("📡 Connessione al server NETCONF stabilita.\n")

    start = time.time()
    xml_config = build_config_xml(beam_list)

    print("XML da inviare:")
    print(xml_config)
    print()
    
    reply = m.edit_config(target="running", config=xml_config)
    end = time.time()
    print("✅ Configurazione aggiornata con successo.")
    print(reply)
    print(f"⏱ Tempo impiegato: {end - start:.2f} secondi.\n")
