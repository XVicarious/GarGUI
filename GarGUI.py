__module_name__ = "GarGUI"
__module_version__ = "1.0.0"
__module_description__ = "A Gargoyle GUI Front-end"

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
       dieRoll = "!val %roll:" + numDie + "d" + diceSize + "%" + modifier
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
       self.setInitDie.Bind(wx.EVT_BUTTON, self.initDiceEdit)
       self.setHitDie.Bind(wx.EVT_BUTTON, self.hitDiceEdit)
       self.setAttackDie.Bind(wx.EVT_BUTTON, self.hitDiceEdit)
   
   def hideSettersMeth(self, event):
        self.initDieValue.Hide()
        self.setInitDie.Hide()
        self.hitDieValue.Hide()
        self.setHitDie.Hide()
        self.setAttackDie.Hide()
        self.attackDieValue.Hide()
        self.hideSetters.Bind(wx.EVT_BUTTON, self.showSettersMeth)
        self.hideSetters.SetLabel("v")
   
   def showSettersMeth(self, event):
       self.initDieValue.Show()
       self.setInitDie.Show()
       self.hitDieValue.Show()
       self.setHitDie.Show()
       self.setAttackDie.Show()
       self.attackDieValue.Show()
       self.hideSetters.Bind(wx.EVT_BUTTON, self.hideSettersMeth)
       self.hideSetters.SetLabel("^")
   
   def initDiceEdit(self, event):
       try:
           setcfg = self.initDieValue.GetValue()
           diceCFG.set("dice", "init", setcfg)
           xchat.command("savecfg")
           #writeConfig()
       except Exception as e:
           wx.MessageBox(str(e))
   
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
               roller = "".join(["!val %roll:", aDie, "%"])
               xchat.command(" ".join(["msg", chan, roller]))
           else:
               if "+" in atkDie:
                   index = aDie.find('+')
               elif "-" in aDie:
                   index = aDie.find('-')
               atkDie1 = aDie[0:index]
               atkDie2 = aDie[index:len(aDie)]
               roller = "".join(["!val %roll:", atkDie1, "%", atkDie2])
               xchat.command(" ".join(["msg", chan, roller]))
       else:
           mod = self.modifierAdd.GetValue()
           roller = "".join(["!val %roll:", aDie, "%+", mod])
           xchat.command(" ".join(["msg", chan, roller]))
       
   def hitButtonClick(self, event):
       if len(self.modifierAdd.GetValue()) == 0:
           if not "+" and "-" in hDie:
               roller = "".join(["!val %roll:", hDie, "%"])
               xchat.command(" ".join(["msg", chan, roller]))
           else:
               if "+" in hDie:
                   index = hDie.find('+')
               elif "-" in hDie:
                   index = hDie.find('-')
               hitDie1 = hDie[0:index]
               hitDie2 = hDie[index:len(hDie)]
               roller = "".join(["!val %roll:", hitDie1, "%", hitDie2])
               xchat.command(" ".join(["msg", chan, roller]))
       else:
           mod = self.modifierAdd.GetValue()
           roller = "".join(["!val %roll:", hDie, "%+", mod])
           xchat.command(" ".join(["msg", chan, roller]))
   
   def aboutButtonClick(self, event):
       wx.MessageBox("GarGUI is by Brian Maurer aka XVicarious \nThis is open source and shit. Give me credit if you use it.\nGargoyle is a IRC bot for RPG games written by CyberXZT", "About", wx.OK | wx.ICON_INFORMATION)
   
   def initButtonClick(self, event):
       if len(self.modifierAdd.GetValue()) == 0:
           if not "+" or "-" in iDie:
               roller = "".join(["!val %roll:", iDie, "%"])
               xchat.command(" ".join(["msg", chan, roller]))
           else:
               if "+" in iDie:
                   index = iDie.find('+')
               elif "-" in iDie:
                   index = iDie.find('-')
               initDie1 = iDie[0:index]
               initDie2 = iDie[index:len(iDie)]
               roller = "".join(["!val %roll:", initDie1, "%", initDie2])
               xchat.command(" ".join(["msg", chan, roller]))
       else:
           mod = self.modifierAdd.GetValue()
           roller = "".join(["!val %roll:", iDie,"%+", mod])
           xchat.command(" ".join(["msg", chan, roller]))
       
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

def writeConfig():
   with open(path + "/dice.gar", "wb") as configfile:
       diceCFG.write(configfile)
       
def writeCfg(word, word_eol, userdata):
    writeConfig()

xchat.hook_command("gar", showGUI)
xchat.hook_command("savecfg", writeCfg)