__module_name__ = "GarGUI"
__module_version__ = "1.2.1"
__module_description__ = "A GUI Front-End for Gargoyle"

version = 121

import wx, xchat, string, os, sys, ConfigParser
from urllib2 import urlopen

# Fix path to load GUI
path = os.path.dirname(os.path.abspath(__file__))
path2 = path
path = "".join([path, "/Gar"])
sys.path.append(path)

from GarSimple import Simple
from GarAdvanced import Advanced

print "\0034>>>>>",__module_name__, __module_version__, "has been loaded <<<<<\003"
print "Welcome to the GarGUI Suite.  GarGUI is a GUI front-end for the IRC RPG bot Gargoyle.  For help please ask XVicarious for now because there is no manual yet!"

# Read the configuration
diceCFG = ConfigParser.RawConfigParser()
diceCFG.read(path + "/dice.gar")
iDie = diceCFG.get("dice", "init")
hDie = diceCFG.get("dice", "hit")
aDie = diceCFG.get("dice", "attack")

# Extra variables to make life easier
command = "msg " + xchat.get_info("channel")
v = unicode('\u039B', "unicode_escape").encode("utf8")

class AdvancedWindow(Advanced):
    
   def __init__(self, *args, **kwds):
       Advanced.__init__(self, *args, **kwds)
       self.bindActions()
        
   def bindActions(self):
       self.rollButton.Bind(wx.EVT_BUTTON, self.rollAdv)
       self.commonDie1.Bind(wx.EVT_BUTTON, self.commonButton1)
       self.commonDie2.Bind(wx.EVT_BUTTON, self.commonButton2)
       self.commonDie3.Bind(wx.EVT_BUTTON, self.commonButton3)
       
   def commonButton1(self, event):
       xchat.command(command + " !val %roll:1d4%")
       
   def commonButton2(self, event):
       xchat.command(command + " !val %roll:1d6%")
       
   def commonButton3(self, event):
       xchat.command(command + " !val %roll:1d20%")

   def rollAdv(self, event):
       numDie = self.numberOfDice.GetValue()
       diceSize = self.dieSize.GetValue()
       modifier = self.modifierAddition.GetValue()
       if not "+" and "-" in modifier:
           modifier = "+" + modifier
           xchat.prnt("You failed to include a '+' or a '-' in your modifier value... Assuming '+'.")
       dieRoll = " !val %roll:" + numDie + "d" + diceSize + "%" + modifier
       xchat.command(command + dieRoll)

class SimpleWindow(Simple):
   
   def __init__(self, *args, **kwds):
       Simple.__init__(self, *args, **kwds)
       self.bindActions()
       self.initDieValue.ChangeValue(iDie)
       self.hitDieValue.ChangeValue(hDie)
       self.attackDieValue.ChangeValue(aDie)
       
   def bindActions(self):
       self.initButton.Bind(wx.EVT_BUTTON, self.initButtonClick)
       self.hitButton.Bind(wx.EVT_BUTTON, self.hitButtonClick)
       self.attackButton.Bind(wx.EVT_BUTTON, self.attackButtonClick)
       self.aboutButton.Bind(wx.EVT_BUTTON, self.aboutButtonClick)
       self.hideSetters.Bind(wx.EVT_BUTTON, self.showSettersMeth)
       self.setInitDie.Bind(wx.EVT_BUTTON, self.initDieEdit)
       self.setHitDie.Bind(wx.EVT_BUTTON, self.hitDieEdit)
       self.setAttackDie.Bind(wx.EVT_BUTTON, self.hitDieEdit)
       self.rollMisc.Bind(wx.EVT_BUTTON, self.rollMiscClick)
   
   def rollMiscClick(self, event):
       numDie = self.dieCount.GetValue()
       sizeDie = self.dieSize.GetValue()
       dieMod = self.dieMod.GetValue()
       if not "+" and "-" in dieMod:
           dieMod = "+" + dieMod
           xchat.prnt("You failed to include a '+' or a '-' in your modifier value... Assuming '+'.")
       dieRoll = " !val %roll:" + numDie + "d" + sizeDie + "%" + dieMod
       xchat.command(command + dieRoll)
   
   def hideSettersMeth(self, event):
       self.frame_sizer.Hide(self.configSizer, recursive=True)
       self.Fit()
       self.hideSetters.Bind(wx.EVT_BUTTON, self.showSettersMeth)
       self.hideSetters.SetLabel("V")
   
   def showSettersMeth(self, event):
       try:
           self.frame_sizer.Show(self.configSizer, recursive=True)
           self.Fit()
       except Exception as e:
           wx.MessageBox(str(e))
       self.hideSetters.Bind(wx.EVT_BUTTON, self.hideSettersMeth)
       self.hideSetters.SetLabel(v)
   
   def initDieEdit(self, event):
       setcfg = self.initDieValue.GetValue()
       diceCFG.set("dice", "init", setcfg)
       xchat.command("savecfg")
       iDie = setcfg

   def hitDieEdit(self, event):
       setcfg = self.hitDieValue.GetValue()
       diceCFG.set("dice", "hit", setcfg)
       xchat.command("savecfg")
       hDie = setcfg
   
   def attackDieEdit(self, event):
       setcfg = self.attackDieValue.GetValue()
       diceCFG.set("dice", "attack", setcfg)
       xchat.command("savecfg")
       aDie = setcfg
   
   def attackButtonClick(self, event):
       try:
           if not "+" and "-" in aDie:
               roller = " !val %roll:" + aDie + "%"
               xchat.command(command + roller)
           else:
               if "+" in aDie:
                   index = aDie.find('+')
               elif "-" in aDie:
                   index = aDie.find('-')
               roller = " !val %roll:" + aDie[0:index] + "%" + aDie[index:len(aDie)]
               xchat.command(command + roller)
       except Exception as e:
           wx.MessageBox(str(e))
       
   def hitButtonClick(self, event):
       if not "+" and "-" in hDie:
           roller = " !val %roll:" + hDie + "%"
           xchat.command(command + roller)
       else:
           if "+" in hDie:
               index = hDie.find('+')
           elif "-" in hDie:
               index = hDie.find('-')
           roller = " !val %roll:" + hDie[0:index] + "%" + hDie[index:len(hDie)]
           xchat.command(command + roller)
   
   def aboutButtonClick(self, event):
       wx.MessageBox("GarGUI " + __module_version__ + "\n\nGarGUI is a front-end for the IRC bot \"Gargoyle\" by CyberXZT.  GarGUI attempts to make the usage of Gargoyle easier by the simplification of the !val command to simple GUI buttons.  \nModes exist in GarGUI to utilize it in different ways.  The normal GUI is the most simple having just a few button for rolling Initiative, Hit Chance, and Attack.  The \"Advanced\" GUI allows users to fully modify each roll, with the ability to have a few common dice as quick settings.\n\n GarGUI is licensed unded the GNU GPL v3.  The full terms of this license can be found in the \"LICENSE\" file in GarGUI's directory.", "About", wx.OK | wx.ICON_INFORMATION)
   
   def initButtonClick(self, event):
       if not "+" and "-" in iDie:
           roller = " !val %roll:" + iDie + "%"
           xchat.command(command + roller)
       else:
           if "+" in iDie:
               index = iDie.find('+')
           elif "-" in iDie:
               index = iDie.find('-')
           roller = " !val %roll:" + iDie[0:index] + "%" + iDie[index:len(iDie)]
           xchat.command(command + roller)
       
def showGUI(word, word_eol, userdata):
   #path = raw(path)
   if __name__ == "__main__":
       app = wx.PySimpleApp(0)
       wx.InitAllImageHandlers()
       try:
           if word[1] == "derp":
               frame_1 = AdvancedWindow(None, -1, "")
               app.SetTopWindow(frame_1)
               frame_1.Show()
               app.MainLoop()
           if word[1] == "update":
               latest = urlopen("http://xvicario.us/gar/latest")
               latest = int(latest.read())
               if version == latest:
                   xchat.prnt("GarGUI: No Updates Found...")
               elif version < latest:
                   xchat.prnt("GarGUI: Update Found... Downloading.")
                   garLatest = urlopen("http://xvicario.us/gar/GarGUI.py")
                   xchat.prnt("GarGUI: Downloaded... Applying Update.")
                   garLatest = garLatest.read()
                   GarGUI = open(path2 + "/GarGUI.py", "w")
                   GarGUI.write(garLatest)
                   GarGUI.close()
                   xchat.prnt("GarGUI: Updated... Unloading module.  Please load GarGUI to finish the update.")
                   xchat.command("py unload GarGUI")
       except IndexError:
           frame_1 = SimpleWindow(None, -1, "")
           app.SetTopWindow(frame_1)
           frame_1.Show()
           app.MainLoop()

def writeCfg(word, word_eol, userdata):
   with open(path + "/dice.gar", "wb") as configfile:
       diceCFG.write(configfile)

xchat.hook_command("gar", showGUI)
xchat.hook_command("savecfg", writeCfg)