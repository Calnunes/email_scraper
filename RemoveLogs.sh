# This will keep a backup of the logs and clean the original logs folder
# When you run the script again, it will remove the backup and move the new logs to backup
rm -rf logs_bk
mkdir logs_bk
mv logs/* logs_bk/
