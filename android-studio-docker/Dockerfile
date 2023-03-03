FROM ubuntu:22.04

RUN dpkg --add-architecture i386
RUN apt-get -y update

# Install X11
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y xorg

# Install prerequisites
RUN apt-get install -y libz1 libncurses5 libbz2-1.0:i386 libstdc++6 libbz2-1.0 lib32stdc++6 lib32z1

# Install Java and other tools
RUN apt-get install -y curl unzip usbutils adb vim ant nano htop default-jdk
RUN apt install -y qemu-kvm

# Clean up
RUN apt-get clean
RUN apt-get purge

RUN adduser root kvm
RUN newgrp kvm

# dconf
RUN mkdir -p /.cache/dconf
RUN chmod 777 -R /.cache
