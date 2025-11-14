
FROM teolot16/netconf-server:latest

COPY ris.yang /opt/yang/ris.yang
RUN sysrepoctl -i /opt/yang/ris.yang
RUN pip install sysrepo

COPY startup.sh /opt/startup.sh
COPY notify.py /opt/notify.py
COPY notify_netconf.py /opt/notify_netconf.py
COPY notify_sysrepo.py /opt/notify_sysrepo.py
RUN chmod +x /opt/startup.sh

EXPOSE 830
CMD ["/opt/startup.sh"]
