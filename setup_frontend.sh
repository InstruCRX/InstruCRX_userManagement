#!/bin/bash
#
# setup the cyber range host VM with Node.js and npm

# remove present version of nodejs, if existing
sudo apt remove nodejs && \
sudo apt purge nodejs && \
sudo apt autoremove  && \

# recommended way to install Node.js 
# see https://github.com/nodesource/distributions#debinstall
curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -  && \
sudo apt-get install -y nodejs && \
npm install && \
cd ..
