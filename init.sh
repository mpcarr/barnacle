echo "init script"
apt-get install python-dev python-rpi.gpio
sudo chown root.gpio /dev/gpiomem
sudo chmod g+rw /dev/gpiomem



sudo cp barnacle.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable barnacle.service
