FROM ubuntu:22.04

RUN dpkg --add-architecture i386
RUN apt-get -y update

# Install X11
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y xorg

# Install prerequisites
RUN apt-get install -y libz1 libncurses5 libbz2-1.0:i386 libstdc++6 libbz2-1.0 lib32stdc++6 lib32z1

# Install Java and other tools
RUN apt-get install -y curl unzip vim ant nano htop default-jdk
RUN apt install -y qemu-kvm

# Clean up
RUN apt-get clean
RUN apt-get purge

# Create user and permissions
RUN useradd -rm -d /home/dev -s /bin/bash -g root -G sudo -u 1000 dev
RUN groupadd -g 1000 dev
RUN newgrp dev
RUN adduser dev kvm

# dconf
RUN mkdir -p /.cache/dconf
RUN chmod 777 -R /.cache
RUN chown dev:dev -R /.cache
RUN mkdir -p /home/dev/.cache/dconf
RUN chmod 777 -R /home/dev/.cache
RUN chown dev:dev -R /home/dev/.cache

USER dev
WORKDIR /home/dev

