import wx

from UI_Windows.winDialogs import winMessageBox, wxdlg_const


class winMain(wx.MDIParentFrame):
    def __init__(self, parent, title):
        super(winMain, self).__init__(parent, title=title, size=(1200, 800))

        self.menuBar = wx.MenuBar()
        self.menuProgram = wx.Menu()
        
        self.menuOpen = self.menuProgram.Append(
            wx.ID_OPEN, "Otwórz plik faktury", "Otwórz plik faktury"
        )
        self.menuExit = self.menuProgram.Append(
            wx.ID_EXIT, "Zamknij\tAlt-F4", "Zamknij aplikację"
        )
        self.menuBar.Append(self.menuProgram, "&Program")

        self.menuHelp = wx.Menu()
        self.menuAbout = self.menuHelp.Append(
            wx.ID_ABOUT, "O programie\tF1", "Informacje o programie"
        )
        self.menuBar.Append(self.menuHelp, "&Pomoc")

        self.SetMenuBar(self.menuBar)

        self.Show()
        self.Bind(wx.EVT_MENU, self.menusEvents)
        self.Bind(wx.EVT_CLOSE, self.OnClose)

    def menusEvents(self, event):
        id = event.GetId()
        if id == wx.ID_EXIT:
            self.OnClose(event)
        elif id == wx.ID_OPEN:
            openFileDialog = wx.FileDialog(
                self,
                "Otwórz plik faktury",
                "",
                "",
                "Pliki faktur XML (*.xml)|*.xml",
                wx.FD_OPEN | wx.FD_FILE_MUST_EXIST,
            )
            id_op = openFileDialog.ShowModal()
            if id_op == wx.ID_OK:
                path = openFileDialog.GetPath()
                winInvoiceView
                print(f"Wybrano plik: {path}")
            openFileDialog.Destroy()
    

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
