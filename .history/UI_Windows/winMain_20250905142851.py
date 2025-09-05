import wx
from UI_Windows.winDialogs import winDialogs, wxdlg_const

class winMain(wx.Frame):
    def __init__(self, parent, title):
        super(winMain, self).__init__(parent, title=title, size=(800, 600))
        
        # Example usage of winDialogs
        self.dialogs = winDialogs()
        self.dialogs.IconMessage(self, wxdlg_const.ICON_INFO)
        
        self.Show()