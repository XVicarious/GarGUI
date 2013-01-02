import wx

class Advanced(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Advanced.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.numberOfDice = wx.TextCtrl(self, -1, "")
        self.label_1 = wx.StaticText(self, -1, "d")
        self.dieSize = wx.TextCtrl(self, -1, "")
        self.modifierAddition = wx.TextCtrl(self, -1, "")
        self.rollButton = wx.Button(self, -1, "Roll!!!!!")
        self.commonDie1 = wx.Button(self, -1, "1d4")
        self.commonDie2 = wx.Button(self, -1, "1d6")
        self.commonDie3 = wx.Button(self, -1, "1d20")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: Advanced.__set_properties
        self.SetTitle("GarGUI Advanced")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: Advanced.__do_layout
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_3 = wx.GridSizer(1, 3, 0, 0)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(self.numberOfDice, 0, wx.EXPAND, 0)
        sizer_3.Add(self.label_1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_3.Add(self.dieSize, 0, wx.EXPAND, 0)
        sizer_3.Add(self.modifierAddition, 0, wx.EXPAND, 0)
        sizer_3.Add(self.rollButton, 0, wx.EXPAND, 0)
        sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)
        grid_sizer_3.Add(self.commonDie1, 0, wx.EXPAND, 0)
        grid_sizer_3.Add(self.commonDie2, 0, wx.EXPAND, 0)
        grid_sizer_3.Add(self.commonDie3, 0, wx.EXPAND, 0)
        sizer_2.Add(grid_sizer_3, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_2)
        sizer_2.Fit(self)
        self.Layout()
        # end wxGlade