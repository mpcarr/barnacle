# barnacle
barnacle - a raspberry pi / volumio music system

TODO - explain hardware needed

1. Start with a fresh volumio imaged sd card
2. ssh to your raspberry pi

   ```
   ssh volumio@volumio.local
   ```
   password: ```volumio```

3. The volumio image already has the I2C Interface enabled. To identify the LCD screen use one of these commands

   ```sudo i2cdetect -y 0```  
   or  
   ```sudo i2cdetect -y 1```
   
   Which of these commands works depends of which raspberry pi you own. One of those commands will output a table like this:
   
   ![alt-text](https://cloud.githubusercontent.com/assets/6593426/25049325/421a2aa4-2139-11e7-9eaf-704951280f5e.png "i2cdetect")
   
   Note which of the the above commands gave you the table and note the address of your lcd screen. In the image above my lcd's address is 3f
   
4. Install python libraries

   ```
   apt-get update
   apt-get install python-virtualenv python-smbus python-dev python-rpi.gpio
   ```
5. Create a virtual enviroment for barnacle and activate it

   ```
   virtualenv --system-site-packages barnacle
   cd barnacle
   source bin/activate
   ```
   your command prompt should look like this
   ![alt-text](https://cloud.githubusercontent.com/assets/6593426/25050948/1e776d60-2142-11e7-9a46-d9fa40766c31.png "barnacle virtual enviroment")
   
6. Install barnacle
   ```
   git clone https://github.com/mpcarr/barnacle.git
   sh barnacle/init.sh
   sudo reboot
   ```
   
   
   
