import wx
from UI_Windows.winMain import winMain

if __name__ == "__main__":
    app = wx.App()
    frame = frmSetupApp(None, "Instalacja systemu XYZ")
    frame.Show()
    app.MainLoop()