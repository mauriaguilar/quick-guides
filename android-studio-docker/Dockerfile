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

# Instll Dart, https://dart.dev/get-dart
# RUN apt-get update
# RUN apt-get install -y apt-transport-https wget
# RUN wget -qO- https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/dart.gpg
# RUN echo 'deb [signed-by=/usr/share/keyrings/dart.gpg arch=amd64] https://storage.googleapis.com/download.dartlang.org/linux/debian stable main' | tee /etc/apt/sources.list.d/dart_stable.list
# RUN apt-get update
# RUN apt-get install -y dart
# RUN echo 'export PATH="$PATH:/usr/lib/dart/bin"' >> ~/.bashrc

# Install Flutter (Dart is included), https://docs.flutter.dev/get-started/install/linux
RUN apt-get install -y bash curl file git unzip zip
# which mkdir rm xz-utilz 
RUN apt-get install -y libglu1-mesa
RUN git clone https://github.com/flutter/flutter.git -b stable
# Check dependencies
# RUN flutter doctor
# Install common dependencies
RUN apt-get install -y clang cmake ninja-build pkg-config libgtk-3-dev liblzma-dev wget
# Install chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt install -y fonts-liberation libu2f-udev xdg-utils
RUN dpkg -i google-chrome-stable_current_amd64.deb && rm *.deb

# user folder is binded, so the PATH variable is added from the Makefile
RUN echo 'export PATH="$PATH:/flutter/bin"' >> ~/.bashrc
RUN echo 'export PATH="$PATH:/android-studio/bin"' >> ~/.bashrc

RUN /flutter/bin/flutter config --android-studio-dir /android-studio
