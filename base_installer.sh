#!/bin/bash

# Script to install all init software

sudo apt-get update -y

sudo apt-get install -y git terminator htop

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb

sudo apt-get install -y ffmpeg
sudo apt-get update -y
sudo apt-get install -y obs-studio
