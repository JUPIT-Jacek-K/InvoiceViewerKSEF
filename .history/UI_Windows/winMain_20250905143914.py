import wx
from UI_Windows.winDialogs import winMessageBox, wxdlg_const

class winMain(wx.Frame):
    def __init__(self, parent, title):
        super(winMain, self).__init__(parent, title=title, size=(1200, 800))
                
        self.Show()

