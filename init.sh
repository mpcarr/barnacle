echo "init script"
pip install -r barnacle/requirements.txt
#apt-get install python-dev python-rpi.gpio
sudo chown root.gpio /dev/gpiomem
sudo chmod g+rw /dev/gpiomem
sudo chmod 666 /dev/i2c-0
#
#
#
sudo cp barnacle.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable barnacle.service
