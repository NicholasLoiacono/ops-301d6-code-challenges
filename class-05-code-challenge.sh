#!/bin/bash

# Script: Ops 301d6 Class 05 Ops Challenge Solution
# Author: Nicholas Loiacono
# Date: 03/17/2023
# Purpose: Compress log file
# Resources: Chat GPT

# Main

#!/bin/bash

# Set up the backup directory
backup_dir="/var/log/backups"

# Create the backup directory if it doesn't exist
if [ ! -d $backup_dir ]; then
  mkdir $backup_dir
fi

# Get the current date and time in the format YYYYMMDDHHMMSS
timestamp=$(date +"%Y%m%d%H%M%S")

# Get the file sizes of the log files before compression and print to the screen
syslog_size=$(du -sh /var/log/syslog | awk '{print $1}')
wtmp_size=$(du -sh /var/log/wtmp | awk '{print $1}')
echo "File size of /var/log/syslog before compression: $syslog_size"
echo "File size of /var/log/wtmp before compression: $wtmp_size"

# Compress the log files and move to the backup directory
syslog_backup="$backup_dir/syslog-$timestamp.zip"
wtmp_backup="$backup_dir/wtmp-$timestamp.zip"
zip -j $syslog_backup /var/log/syslog
zip -j $wtmp_backup /var/log/wtmp

# Clear the contents of the log files
cat /dev/null > /var/log/syslog
cat /dev/null > /var/log/wtmp

# Get the file sizes of the compressed files and print to the screen
syslog_backup_size=$(du -sh $syslog_backup | awk '{print $1}')
wtmp_backup_size=$(du -sh $wtmp_backup | awk '{print $1}')
echo "File size of $syslog_backup: $syslog_backup_size"
echo "File size of $wtmp_backup: $wtmp_backup_size"

# Compare the sizes of the original log files and the compressed files
if [ $syslog_size = $syslog_backup_size ]; then
  echo "/var/log/syslog was successfully compressed"
else
  echo "Error: /var/log/syslog was not compressed correctly"
fi

if [ $wtmp_size = $wtmp_backup_size ]; then
  echo "/var/log/wtmp was successfully compressed"
else
  echo "Error: /var/log/wtmp was not compressed correctly"
fi

# End