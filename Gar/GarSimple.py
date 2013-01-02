import wx

class Simple(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.initButton = wx.Button(self, -1, "Roll Initiative")
        self.hitButton = wx.Button(self, -1, "Roll Hit")
        self.attackButton = wx.Button(self, -1, "Roll Attack")
        self.aboutButton = wx.Button(self, -1, "About")
        self.settingButton = wx.Button(self, -1, "Settings")
        self.modifierAdd = wx.TextCtrl(self, -1, "")
        self.label_1 = wx.StaticText(self, -1, "Special Modifier", style=wx.ALIGN_CENTRE)
        self.initDieValue = wx.TextCtrl(self, -1, "")
        self.setInitDie = wx.Button(self, -1, "Set Initiative Die")
        self.hitDieValue = wx.TextCtrl(self, -1, "")
        self.setHitDie = wx.Button(self, -1, "Set Hit Die")
        self.attackDieValue = wx.TextCtrl(self, -1, "")
        self.setAttackDie = wx.Button(self, -1, "Set Attack Die")
        self.hideSetters = wx.Button(self, -1, "v")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MyFrame.__set_properties
        self.SetTitle("GarGUI")
        self.initDieValue.SetToolTipString("Default: 1d20")
        self.initDieValue.Hide()
        self.setInitDie.Hide()
        self.hitDieValue.Hide()
        self.setHitDie.Hide()
        self.setAttackDie.Hide()
        self.attackDieValue.Hide()
        self.hitDieValue.SetToolTipString("Default: 1d20")
        self.attackDieValue.SetToolTipString("Default: 2d6")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_2 = wx.GridSizer(4, 2, 0, 0)
        grid_sizer_1 = wx.GridSizer(3, 3, 0, 0)
        grid_sizer_1.Add(self.initButton, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.hitButton, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.attackButton, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.aboutButton, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.settingButton, 0, wx.EXPAND, 0)
        sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        grid_sizer_2.Add(self.modifierAdd, 0, wx.EXPAND, 0)
        grid_sizer_2.Add(self.label_1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_2.Add(self.initDieValue, 0, wx.EXPAND, 0)
        grid_sizer_2.Add(self.setInitDie, 0, wx.EXPAND, 0)
        grid_sizer_2.Add(self.hitDieValue, 0, wx.EXPAND, 0)
        grid_sizer_2.Add(self.setHitDie, 0, wx.EXPAND, 0)
        grid_sizer_2.Add(self.attackDieValue, 0, wx.EXPAND, 0)
        grid_sizer_2.Add(self.setAttackDie, 0, wx.EXPAND, 0)
        sizer_1.Add(grid_sizer_2, 1, wx.EXPAND, 0)
        sizer_1.Add(self.hideSetters, 0, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade