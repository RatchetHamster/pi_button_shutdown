Log Stored at: /var/log/shutdown_button.log

## To Update  
cd /home/pi/python/pi_button_shutdown  
git pull  
sudo reboot  

## To Install  
cd into /home/pi/python (if python doesn't exist, make it using mkrid)  
git clone this repo  

#Move .service file to correct location  
sudo mv /home/pi/python/pi_button_shutdown/pi_button_shutdown.service /etc/systemd/system/  

#Enable service at boot  
sudo systemctl daemon-reload  
sudo systemctl enable pi_button_shutdown  
sudo systemctl start pi_button_shutdown  

#Create logrotate limit on log file  
sudo nano /etc/logrotate.d/shutdown_button  
into the file put:  
/var/log/shutdown_button.log  
{  
    weekly  
    minsize 1M  
    maxsize 10M  
    rotate 4  
    missingok  
    notifempty  
}  
