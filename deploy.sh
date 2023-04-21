#!/bin/bash

# ref: https://askubuntu.com/a/30157/8698
if ! [ $(id -u) = 0 ]; then
    echo "The script need to be run as root." >&2
    exit 1
fi

if [ $SUDO_USER ]; then
    real_user=$SUDO_USER
else
    real_user=$(whoami)
fi

# Delete Old Data
sudo docker stop $(docker ps -aq)
sudo docker rm $(docker ps -aq)
sudo docker rmi $(docker images -aq)

# Build and Start Docker Container
docker build --pull --rm -f "Dockerfile" -t taxila "."
sudo docker run -p 80:8000 -d --restart unless-stopped --name taxila-django taxila
