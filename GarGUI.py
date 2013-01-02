__module_name__ = "GarGUI"
__module_version__ = "1.1.0"
__module_description__ = "A GUI Front-End for Gargoyle"

import wx, xchat, string, os, sys, ConfigParser

# Fix path to load GUI
path = os.path.dirname(os.path.abspath(__file__))
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
   
   def hideSettersMeth(self, event):
        self.frame_sizer.Hide(self.configSizer, recursive=True)
        self.Fit()
        self.hideSetters.Bind(wx.EVT_BUTTON, self.showSettersMeth)
        self.hideSetters.SetLabel("v")
   
   def showSettersMeth(self, event):
       try:
           self.frame_sizer.Show(self.configSizer, recursive=True)
           self.Fit()
       except Exception as e:
           wx.MessageBox(str(e))
       self.hideSetters.Bind(wx.EVT_BUTTON, self.hideSettersMeth)
       self.hideSetters.SetLabel("^")
   
   def initDieEdit(self, event):
       setcfg = self.initDieValue.GetValue()
       diceCFG.set("dice", "init", setcfg)
       xchat.command("savecfg")

   def hitDieEdit(self, event):
       setcfg = self.hitDieValue.GetValue()
       diceCFG.set("dice", "hit", setcfg)
       xchat.command("savecfg")
   
   def attackDieEdit(self, event):
       setcfg = self.attackDieValue.GetValue()
       diceCFG.set("dice", "attack", setcfg)
       xchat.command("savecfg")
   
   def attackButtonClick(self, event):
       if len(self.modifierAdd.GetValue()) == 0:
           if not "+" and "-" in aDie:
               roller = " !val %roll:" + aDie + "%"
               xchat.command(command + roller)
           else:
               if "+" in atkDie:
                   index = aDie.find('+')
               elif "-" in aDie:
                   index = aDie.find('-')
               roller = " !val %roll:" + aDie[0:index] + "%" + aDie[index:len(aDie)]
               xchat.command(command + roller)
       else:
           mod = self.modifierAdd.GetValue()
           roller = " !val %roll:" + aDie + "%+" + mod
           xchat.command(command + roller)
       
   def hitButtonClick(self, event):
       if len(self.modifierAdd.GetValue()) == 0:
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
       else:
           mod = self.modifierAdd.GetValue()
           roller = " !val %roll:" + hDie + "%+" + mod
           xchat.command(command + roller)
   
   def aboutButtonClick(self, event):
       wx.MessageBox("GarGUI " + __module_version__ + "\n\nGarGUI is a front-end for the IRC bot \"Gargoyle\" by CyberXZT.  GarGUI attempts to make the usage of Gargoyle easier by the simplification of the !val command to simple GUI buttons.  \nModes exist in GarGUI to utilize it in different ways.  The normal GUI is the most simple having just a few button for rolling Initiative, Hit Chance, and Attack.  The \"Advanced\" GUI allows users to fully modify each roll, with the ability to have a few common dice as quick settings.\n\n GarGUI is licensed unded the GNU GPL v3.  The full terms of this license can be found in the \"LICENSE\" file in GarGUI's directory.", "About", wx.OK | wx.ICON_INFORMATION)
   
   def initButtonClick(self, event):
       if len(self.modifierAdd.GetValue()) == 0:
           if not "+" or "-" in iDie:
               roller = " !val %roll:" + iDie + "%"
               xchat.command(command + roller)
           else:
               if "+" in iDie:
                   index = iDie.find('+')
               elif "-" in iDie:
                   index = iDie.find('-')
               roller = " !val %roll:" + iDie[0:index] + "%" + iDie[index:len(iDie)]
               xchat.command(command + roller)
       else:
           mod = self.modifierAdd.GetValue()
           roller = " !val %roll:" + iDie + "%+" + mod
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