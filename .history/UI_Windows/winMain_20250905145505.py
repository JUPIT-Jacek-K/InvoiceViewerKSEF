import wx
from UI_Windows.winDialogs import winMessageBox, wxdlg_const

class winMain(wx.Frame):
    def __init__(self, parent, title):
        super(winMain, self).__init__(parent, title=title, size=(1200, 800))

        self.menuBar = wx.MenuBar()
        self.menuProgram = wx.Menu()
        self.menuExit = self.menuProgram.Append(wx.ID_EXIT, "Zamknij\tAlt-F4", "Zamknij aplikację")
        self.menuBar.Append(self.menuProgram, "&Program")   
        self.Show()
        self.Bind(wx.EVT_MENU, self.menusEvents)
        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def menusEvents(self, event):
        id = event.GetId()
        if id == wx.ID_EXIT:
            self.OnClose(event)

    def OnClose(self, event):
        msgMox = winMessageBox(
            "Czy zamknąć aplikację?",
            "Zamknięcie aplikacji",
            wxdlg_const.ID_YES_NO | wxdlg_const.ICON_ASK,
            self,
        )
        ii = msgMox.ShowModal()
        if ii == wxdlg_const.ID_YES:
            self.Destroy()
