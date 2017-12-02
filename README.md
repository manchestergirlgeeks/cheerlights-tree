# cheerlights-tree

This repository contains the code for our workshop on 10th December. You'll need a Raspberry Pi Zero W, Blinkt GPIO header and a laser-cut Christmas tree to sit on top of it.

Here are the steps you'll need to take to set up our code on your Pi Zero W:

1. Download this repo (using the green button above and to the right). This will download a ZIP file onto your desktop. Unzip the contents of this file onto your desktop - you should have files called **mggtree.py**, **mggtree_fix.py** and **colours.csv**.

2. Launch a Terminal window (click the black rectangle at the top) and type the command:
    
    `pip install twython`

This will install the Twython package for Python.

3. Open the file mggtree_fix.py by double clicking on it (by default, this will launch in Thonny). Look through the code for lines with code comments (these will show up in grey) and replace the word SOMETHING on those lines with the correct code. Make sure you save your changes!

4. You can check your code is working. Go back to your terminal window and type:

    `python /home/pi/Desktop/mggtree_fix.py`

After a few seconds, the colour of the Blinkt should change to match the most recent #cheerlights tweet. Any tweet with the hashtag #cheerlights should trigger the colour change, and any colour in the list colours.csv will work. You can also use the word 'rainbow' in a #cheerlights tweet to get a rainbow effect.

If you don't want to clog up your timeline with **#cheerlights** tweets for your followers, start your tweet with **@mgg_tree** - our tree's Twitter account doesn't mind, and if you don't have a Twitter account of your own, ask one of our team to tweet from there with your chosen colour.

4. Go back to your terminal window and type
    
    `crontab -e`
    
This will load a text editor with your Crontab file - which tells the Pi what you'd like it to do each time the Pi boots. Use the arrow keys to go to the bottom of the file, and add the line (exactly!):

`@reboot python /home/pi/Desktop/mggtree_fix.py &`

Then press control-X to leave the editor, hit Y to say yes please save, and hit enter to save over the Crontab file. This will launch the code each time the Pi is powered up (although it may take some time to boot before it starts working).

Now you can unplug your Pi, fit it into the tree base and plug it in - it should run on its own whenever it's powered.
