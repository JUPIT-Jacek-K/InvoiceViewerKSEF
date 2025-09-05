import wx
from UI_Windows.winDialogs import winDiwinMessageBoxalogs, wxdlg_const

class winMain(wx.Frame):
    def __init__(self, parent, title):
        super(winMain, self).__init__(parent, title=title, size=(800, 600))
                
        self.Show()