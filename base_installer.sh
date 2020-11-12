#!/bin/bash

# Script to install all init software

sudo apt-get update

sudo apt install git terminator htop minder

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb

sudo apt-get install ffmpeg
sudo apt-get update
sudo apt-get install obs-studio
