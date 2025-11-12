from ncclient import manager
import xml.dom.minidom

DEVICE = {
    "host": "ris-netconf-server",
    "port": 830,
    "username": "root",
    "password": "root",
    "hostkey_verify": False
}

with manager.connect(**DEVICE) as m:
    print("📡 Connessione al server NETCONF stabilita.\n")

    # Richiede configurazione corrente
    reply = m.get_config(source="running")

    # Formatta XML per stampa leggibile
    xml_str = xml.dom.minidom.parseString(str(reply)).toprettyxml()
    print("Configurazione corrente della RIS:\n")
    print(xml_str)
