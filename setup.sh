#!/bin/bash

sudo apt-get install python3

pip install Flask mysql-connector-python pyserial multiprocessing


# Install MariaDB server
sudo apt install mariadb-server

# Secure the installation
sudo mysql_secure_installation
