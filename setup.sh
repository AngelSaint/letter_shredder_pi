#!/bin/bash

sudo apt-get install python3

pip install Flask mysql-connector-python pyserial multiprocessing


# Install MariaDB server
sudo apt install mariadb-server

# Secure the installation
sudo mysql_secure_installation


# Log in to MySQL as root
sudo mysql -u root << EOF

# Create user and grant privileges
CREATE USER 'smunamala'@'localhost' IDENTIFIED BY 'raspberry';
GRANT ALL PRIVILEGES ON *.* TO 'smunamala'@'localhost';

EOF