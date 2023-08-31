#!/bin/bash

printenv

# local directory to choose the file to download
REPERTOIRE="/home/pi/$1/"
# local file to send
FILE=`ls /home/pi/$1/ -got| grep \.jpg$ | head -1 |awk '{print $7}'`

echo $REPERTOIRE$FILE

# https://www.raspberrypi.org/forums/viewtopic.php?t=68541&p=500070
# https://www.raspberrypi.org/forums/viewtopic.php?f=91&t=51222

#authentication to access remote directory
USERNAME="User_serveur"
PASSWORD="password"
SERVER="IP_serveur"
 
# remote server directory to download the backup
BACKUPDIR="/SAV/time_lapse_pi/$1/"

echo "Attempting ftp upload~, ..."

cd $REPERTOIRE
ftp -in $SERVER <<EOMYF
user $USERNAME $PASSWORD
pwd
cd $BACKUPDIR
put $FILE
bye
EOMYF
