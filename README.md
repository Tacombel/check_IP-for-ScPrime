# check_IP-for-ScPrime
Copy checkip.py anywhere you like

Open with a editor.

Edit  os.system('docker exec scprime01 spc host announce ' + ip + ':14282' ) to match your announce command. If neccessary add full path. You only need to edit the parts between '' In particular, ip is a variable so don't touch it. Beware of the space after announce.

Create a cron job for the user that launches spd. Edit to suit your paths

*/5 * * * * systemd-cat -t "checkip-cron" /usr/bin/python3 /home/daniel/checkip/checkip.py

A ip.txt file will be created at /home/$USER/ that will register ip changes.

Video in spanish explaning the procedure for windows.

Donations welcome:

SCP: 29397f5ac09162c48aeea537c4950d90a6b370899a2c8054a71e82ab4954228bb63e59c56464
