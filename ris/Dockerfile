
FROM sysrepo/sysrepo-netopeer2:latest

COPY ris.yang /opt/yang/ris.yang
RUN sysrepoctl -i /opt/yang/ris.yang

COPY startup.sh /opt/startup.sh
COPY notify.py /opt/notify.py
RUN chmod +x /opt/startup.sh

EXPOSE 830
CMD ["/opt/startup.sh"]
