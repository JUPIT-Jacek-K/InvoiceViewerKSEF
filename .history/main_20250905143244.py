import wx
from UI_Windows.winMain import winMain

if __name__ == "__main__":
    app = wx.App()
    app_title = "Instalacja systemu XYZ"
    frame = winMain(None, "Instalacja systemu XYZ")
    frame.Show()
    app.MainLoop()