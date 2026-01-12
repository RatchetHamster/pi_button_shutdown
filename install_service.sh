#Move .service file to correct location
sudo mv /home/pi/python/pi_button_shutdown/pi_button_shutdown.service /etc/systemd/system/

#Enable service at boot
sudo systemctl daemon-reload
sudo systemctl enable pi_button_shutdown
sudo systemctl start pi_button_shutdown
