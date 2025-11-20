FROM teolot16/netconf-server:latest

# Converti i fine riga durante la copia
COPY startup.sh /opt/startup.sh
RUN sed -i 's/\r$//' /opt/startup.sh && chmod +x /opt/startup.sh

COPY ris.yang /opt/yang/ris.yang
RUN sysrepoctl -i /opt/yang/ris.yang
RUN pip install sysrepo

COPY notify.py /opt/notify.py
COPY notify_netconf.py /opt/notify_netconf.py
COPY notify_sysrepo.py /opt/notify_sysrepo.py

EXPOSE 830
CMD ["/opt/startup.sh"]
