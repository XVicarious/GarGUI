import wx

class Simple(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Simple.__init__
        kwds["style"] = wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.STAY_ON_TOP | wx.SYSTEM_MENU | wx.RESIZE_BORDER | wx.CLIP_CHILDREN
        wx.Frame.__init__(self, *args, **kwds)
        self.initButton = wx.Button(self, -1, "Roll Initiative")
        self.hitButton = wx.Button(self, -1, "Roll Hit")
        self.attackButton = wx.Button(self, -1, "Roll Attack")
        self.dieCount = wx.TextCtrl(self, -1, "")
        self.label_2 = wx.StaticText(self, -1, "d", style=wx.ALIGN_CENTRE)
        self.dieSize = wx.TextCtrl(self, -1, "")
        self.dieMod = wx.TextCtrl(self, -1, "")
        self.rollMisc = wx.Button(self, -1, "Roll")
        self.miscSizer_staticbox = wx.StaticBox(self, -1, "Misc Roll")
        self.initDieValue = wx.TextCtrl(self, -1, "")
        self.setInitDie = wx.Button(self, -1, "Set Initiative Die")
        self.hitDieValue = wx.TextCtrl(self, -1, "")
        self.setHitDie = wx.Button(self, -1, "Set Hit Die")
        self.attackDieValue = wx.TextCtrl(self, -1, "")
        self.setAttackDie = wx.Button(self, -1, "Set Attack Die")
        self.hideSetters = wx.Button(self, -1, "^")
        self.aboutButton = wx.Button(self, -1, "About")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Simple.__set_properties
        self.SetTitle("GarGUI")
        self.dieCount.SetMinSize((50, 42))
        self.dieSize.SetMinSize((50, 42))
        self.dieMod.SetMinSize((50, 42))
        self.initDieValue.SetToolTipString("Default: 1d20")
        self.hitDieValue.SetToolTipString("Default: 1d20")
        self.attackDieValue.SetToolTipString("Default: 2d6")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Simple.__do_layout
        frame_sizer = wx.BoxSizer(wx.VERTICAL)
        configSizer = wx.GridSizer(4, 2, 0, 0)
        self.miscSizer_staticbox.Lower()
        miscSizer = wx.StaticBoxSizer(self.miscSizer_staticbox, wx.HORIZONTAL)
        mainButtonSizer = wx.BoxSizer(wx.HORIZONTAL)
        mainButtonSizer.Add(self.initButton, 0, wx.EXPAND, 0)
        mainButtonSizer.Add(self.hitButton, 0, wx.EXPAND, 0)
        mainButtonSizer.Add(self.attackButton, 0, wx.EXPAND, 0)
        frame_sizer.Add(mainButtonSizer, 1, wx.EXPAND, 0)
        miscSizer.Add(self.dieCount, 0, wx.EXPAND, 0)
        miscSizer.Add(self.label_2, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        miscSizer.Add(self.dieSize, 0, wx.EXPAND, 0)
        miscSizer.Add(self.dieMod, 0, wx.EXPAND, 0)
        miscSizer.Add(self.rollMisc, 0, wx.EXPAND, 0)
        frame_sizer.Add(miscSizer, 1, wx.EXPAND, 0)
        configSizer.Add(self.initDieValue, 0, wx.EXPAND, 0)
        configSizer.Add(self.setInitDie, 0, wx.EXPAND, 0)
        configSizer.Add(self.hitDieValue, 0, wx.EXPAND, 0)
        configSizer.Add(self.setHitDie, 0, wx.EXPAND, 0)
        configSizer.Add(self.attackDieValue, 0, wx.EXPAND, 0)
        configSizer.Add(self.setAttackDie, 0, wx.EXPAND, 0)
        frame_sizer.Add(configSizer, 1, wx.EXPAND, 0)
        frame_sizer.Add(self.hideSetters, 0, wx.EXPAND, 0)
        frame_sizer.Add(self.aboutButton, 0, wx.EXPAND, 0)
        self.frame_sizer = frame_sizer
        self.configSizer = configSizer
        self.SetSizer(frame_sizer)
        frame_sizer.Fit(self)
        self.Layout()
        # end wxGlade