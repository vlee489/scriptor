#!/bin/bash

if [ "$(id -u)" != "0" ]; then  #Check if script is being run as root
   echo "This script must be run as root" 1>&2
   exit 1
fi
if [ ! $? = 0 ]; then
   exit 1
else
   mkdir /boot/script/
   idir="/opt/scriptor"
   mkdir "$idir"
   cp -a services/. /etc/systemd/system/
   cp -a scripts/. "$idir/scripts/"
   for filename in services/*.service; do
       name=${filename##*/}
       systemctl enable $name
   done
fi