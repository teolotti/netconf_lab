# ===========================
# RIS-NETCONF Base Image
# ===========================
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /opt

# 1️⃣ Dipendenze
RUN apt-get update && apt-get install -y \
    git cmake build-essential pkg-config unzip ca-certificates \
    libpcre3-dev libpcre2-dev libssl-dev libssh-dev \
    libprotobuf-c-dev protobuf-c-compiler \
    libavl-dev libev-dev \
    libcurl4-openssl-dev \
    python3 python3-pip openssh-server sudo curl \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

# 2️⃣ Compila e installa lo stack NETCONF
RUN git clone https://github.com/CESNET/libyang.git && \
    cd libyang && mkdir build && cd build && \
    cmake -DCMAKE_INSTALL_PREFIX=/usr .. && make -j$(nproc) && make install && \
    cd /opt && git clone https://github.com/CESNET/libnetconf2.git && \
    cd libnetconf2 && mkdir build && cd build && \
    cmake -DCMAKE_INSTALL_PREFIX=/usr .. && make -j$(nproc) && make install && \
    cd /opt && git clone https://github.com/sysrepo/sysrepo.git && \
    cd sysrepo && mkdir build && cd build && \
    cmake -DCMAKE_INSTALL_PREFIX=/usr .. && make -j$(nproc) && make install && \
    cd /opt && git clone https://github.com/CESNET/Netopeer2.git && \
    cd Netopeer2 && mkdir build && cd build && \
    cmake -DCMAKE_INSTALL_PREFIX=/usr .. && make -j$(nproc) && make install

