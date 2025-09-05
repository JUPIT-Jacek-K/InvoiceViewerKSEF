import wx
from UI.winMain import winMain

if __name__ == "__main__":
    app = wx.App()
    frame = frmSetupApp(None, "Instalacja systemu XYZ")
    frame.Show()
    app.MainLoop()