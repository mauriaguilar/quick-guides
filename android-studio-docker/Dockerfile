FROM ubuntu:20.04

RUN dpkg --add-architecture i386
RUN apt-get -y update

# Download specific Android Studio bundle (all packages).
RUN apt-get install -y curl unzip

ADD ./android-studio-ide-201.6953283-linux.tar.gz /

# Install X11
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y xorg

# Install other useful tools
RUN apt-get install -y vim ant nano

# install Java
RUN apt-get install -y default-jdk

# Install prerequisites
RUN apt-get install -y libz1 libncurses5 libbz2-1.0:i386 libstdc++6 libbz2-1.0 lib32stdc++6 lib32z1

# Clean up
RUN apt-get clean
RUN apt-get purge

