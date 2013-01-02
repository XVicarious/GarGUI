GarGUI v1.0.0
----------------

Written by: Brian Maurer a.k.a XVicarious

GarGUI requires Python 2.7 and wxPython 2.8

GarGUI is a simple GUI written in Python (with wxPython) designed to simplify CyberXZT's overly complicated IRC bot for RPGs, called Gargoyle.  GarGUI takes Gargoyle's !val command and turns it into cake.
Below is a quick overview of each file of GarGUI.

GarGUI.py  --  The main file, load this into XChat
Gar/
    GarSimple.pyc  --  The simple, and default GUI for Gar
    GarAdvanced.pyc  --  The advanced, and derp GUI for Gar
    dice.gar  --  The configuration file for GarGUI that saves dice for the GarSimple GUI.
    
    
To start, type "/gar" this will open the GUI.
You will see a few buttons and a text field.  Each button represents a roll type for RPGs.  The text box is your modifier for the dice roll.  The final button on the bottom will bring up the settings for each the Initiative, Hit, and Attack dice.  To change them, change the text boxes, and then press the button next to the respective die to save the configuration.
Note that typing "/savecfg" in XChat's text field will also save the configuration.

To load up the advanced and derp GUI, type "/gar derp".
The advanced GUI gives more control over what you roll.  You can modify the dice every time you roll.  It also gives three options of common dice to roll without having to input anything else. In the near future these should be configurable.

END
