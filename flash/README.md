# Flash scripts to write your opentaxus badges

This directory has all of the flashing scripts and related files for development 
and production of your badges.


### Files

##### adafruit-circuitpython-seeeduino_xiao_rp2040-en_US-9.0.4.uf2

##### code.py

When all else fails, force the microcontroller to reset by writing this file
to CIRCUITPY/ when it shows up as storage on your computer

##### dock.scad

(OpenSCAD)[https://openscad.org/]
model for creating your own badge flashing rig. This plus a USB hub and a 
few cables lets you create a mass flashing rig.

##### flash-generic.py

A more generic flashing script for developers to be able to test out changes on whatever
system they typically code on.

##### flash.py

Linux specific flashing script.  Utilizes pyudev, so if you have that available this
will work well for you. This script has been thoroughly tested and used and is the
preferred method for mass flashing of badges.

##### flash_nuke.uf2

I think the name says it all :)
