# check_IP-for-ScPrime
Copy checkip.py anywhere you like
Remove the last line.
Edit  os.system('docker exec scprime01 spc host announce ' + ip + ':14282' ) to match your announce command. If neccessary add full path.
Create a cron job for the users that launches spd. Edit to suit your paths
0/5 * * * * systemd-cat -t "checkip-cron" /usr/bin/python3 /home/daniel/checkip/checkip.py
A ip.txt file will be created at /home/$USER/ taht will rgister ip changes.
