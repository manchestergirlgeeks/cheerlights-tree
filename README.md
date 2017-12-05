# cheerlights-tree

This repository contains the code for our workshop on 10th December. You'll need a Raspberry Pi Zero W, Blinkt GPIO header and a laser-cut Christmas tree to sit on top of it.

Here are the steps you'll need to take to set up our code on your Pi Zero W:

1. Download this repo (using the green button above and to the right). This will download a ZIP file onto your desktop. Unzip the contents of this file onto your desktop - you should have files called **mggtree.py**, **mggtree_fix.py** and **colours.csv**.

2. Launch a Terminal window (click the black rectangle at the top) and type the command:
    
    `pip install twython`

This will install the Twython package for Python.

3. Open the file mggtree_fix.py by double clicking on it (by default, this will launch in Thonny). Look through the code for lines with code comments (these will show up in grey) and replace the word SOMETHING on those lines with the correct code. Make sure you save your changes!

(If you are using this repo without being present at the workshop, the correct version of the code is in mggtree.py. If you'd like to just use the correct version, you'll need to change the line in steps 4 and 5 to make sure you run the right code.)

4. You can check your code is working. Go back to your terminal window and type:

    `python /home/pi/Desktop/mggtree_fix.py`

After a few seconds, the colour of the Blinkt should change to match the most recent #cheerlights tweet. Any tweet with the hashtag #cheerlights should trigger the colour change, and any colour in the list colours.csv will work. You can also use the word 'rainbow' in a #cheerlights tweet to get a rainbow effect.

If you don't want to clog up your timeline with **#cheerlights** tweets for your followers, start your tweet with **@mgg_tree** - our tree's Twitter account doesn't mind, and if you don't have a Twitter account of your own, ask one of our team to tweet from there with your chosen colour.

5. Go back to your terminal window and type
    
    `crontab -e`
    
This will load a text editor with your Crontab file - which tells the Pi what you'd like it to do each time the Pi boots. Use the arrow keys to go to the bottom of the file, and add the line (exactly!):

`@reboot python /home/pi/Desktop/mggtree_fix.py &`

Then press control-X to leave the editor, hit Y to say yes please save, and hit enter to save over the Crontab file. This will launch the code each time the Pi is powered up (although it may take some time to boot before it starts working).

Now you can unplug your Pi, fit it into the tree base and plug it in - it should run on its own whenever it's powered.

6. The tree should work when connected to the wifi network it's currently on, but if you're going to take it home you'll need to teach it your home wifi name and password. Open the wifi config file by typing:

    `sudo nano /etc/wpa_supplicant/wpa_supplicant.conf`

You should be able to see the details of the current wifi network. You'll need to reproduce this exactly below what's there, as follows (inserting the relevant details):

`network={

    ssid="YOUR NETWORK SSID"
    
    psk="YOUR WIFI PASSWORD"
    
}`

Now press ctrl-X to close it, Y to say yes please save, and enter to confirm you'd like to save it in the same place. Now (fingers crossed!!) your Pi should work automatically when you get it home.

If you find it doesn't power up (you should wait a little while in case it's still loading), you may need to connect it to a monitor and keyboard/mouse to check it can connect to the wifi, and that the program runs ok.

Enjoy your #cheerlights tree!





