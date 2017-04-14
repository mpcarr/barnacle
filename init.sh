echo "init script"
sudo cp barnacle.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable barnacle.service
