# Usa direttamente un'immagine netopeer2 già configurata
FROM sysrepo/sysrepo-netopeer2:latest

# Copia il tuo modello YANG all'interno del container
COPY ris.yang /opt/yang/ris.yang

# Installa il modello nella sysrepo (in base alla directory usata da questa immagine)
RUN sysrepoctl -i /opt/yang/ris.yang

EXPOSE 830

CMD ["netopeer2-server", "-d", "-v2"]

