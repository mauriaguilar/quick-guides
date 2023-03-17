#!/bin/bash

# Script to install all init software

sudo apt-get update -y

echo "common apps..." && sleep 5
sudo apt-get install -y git terminator htop gparted

echo "email?: " && read email && git config --global user.email "$email"
git config --global user.name "Mauricio Aguilar"

#echo "chrome..." && sleep 5
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb

# sudo apt-get install -y ffmpeg
# sudo apt-get update -y
# sudo apt-get install -y obs-studio


# sudo snap install postman

echo "Visual Studio: https://code.visualstudio.com/download"
#sudo dpkg -i *.deb

