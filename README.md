PiCoffee (a Raspberry Pi web server for controling your coffee pot)
======
This is a Raspberry Pi web server that allows a user to start/stop a coffee maker remotely.  By starting the brew in bed,
the time to the vital first cup is greatly reduced.

Video of code in action- Video shows a light being turned on/off but works with any AC Applicance.<br>
https://goo.gl/hqf7TJ


<pre>
Installing GPIO
sudo apt-get update
sudo apt-get -y install python-rpi.gpio

Installing sqlite3 
sudo apt-get install sqlite3

Installing Flask
To install flask you need to install pip. You can install it using the following command in your raspberry pi terminal.
sudo apt-get install python-pip
To install flask use the following command.
sudo pip install flask
</pre>
